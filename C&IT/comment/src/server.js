const express = require("express");
const { Pool } = require("pg");

const createServer = (pool, port = 3000) => {
  const app = express();

  // Função para organizar os comentários de forma recursiva em árvore
  function organizeComments(comments) {
    const commentMap = {};

    // Cria um objeto para cada comentário com uma lista vazia de filhos
    comments.forEach(comment => {
      commentMap[comment.id] = { 
        id: comment.id, 
        text: comment.text, 
        children: [] 
      };
    });

    const rootComments = [];

    // Organiza os comentários em estrutura hierárquica
    comments.forEach(comment => {
      const formattedComment = commentMap[comment.id];

      if (comment.parent_id === null) {
        // Se não tiver parent_id, é um comentário raiz
        rootComments.push(formattedComment);
      } else {
        // Se tiver parent_id, adiciona-o ao pai correspondente
        const parentComment = commentMap[comment.parent_id];
        if (parentComment) {
          parentComment.children.push(formattedComment);
        }
      }
    });

    // Remove a chave "children" dos comentários sem filhos de forma recursiva
    const cleanEmptyChildren = (comments) => {
      comments.forEach(comment => {
        if (comment.children.length === 0) {
          delete comment.children;
        } else {
          // Chamada recursiva para remover "children" em níveis mais profundos
          cleanEmptyChildren(comment.children);
        }
      });
    };
    cleanEmptyChildren(rootComments);

    return rootComments;
  }

  // Rota para buscar os comentários de um post específico
  app.get("/posts/:postId/comments", async (req, res) => {
    const postId = parseInt(req.params.postId, 10);

    try {
      // Recupera os comentários para o post
      const result = await pool.query(
        'SELECT id, text, parent_id FROM comments WHERE post_id = $1 ORDER BY id',
        [postId]
      );

      const comments = result.rows;

      if (comments.length === 0) {
        // Retorna 404 se não encontrar comentários
        return res.status(404).send("No comments found for this post");
      }

      // Organiza os comentários em uma estrutura hierárquica
      const organizedComments = organizeComments(comments);

      // Retorna os comentários organizados em JSON
      res.json({ data: organizedComments });
    } catch (error) {
      console.error(error);
      res.status(500).send("Internal Server Error");
    }
  });

  const server = app.listen(port, () =>
    console.log(`[server] listening on port ${port}`)
  );

  return {
    app,
    close: () =>
      new Promise(resolve => {
        server.close(() => {
          resolve();
          console.log("[server] closed");
        });
      }),
  };
};

// Conexão com o banco de dados e criação do servidor
const startServer = async () => {
  const pool = new Pool({
    connectionString: 'postgresql://postgres:brunao@localhost:5432/comment_system', // Substitua com suas credenciais
  });

  const client = await pool.connect();

  // Limpeza e criação das tabelas
  await client.query("DROP TABLE IF EXISTS comments");
  await client.query("DROP TABLE IF EXISTS posts");
  await client.query(`
    CREATE TABLE IF NOT EXISTS posts (
      id SERIAL PRIMARY KEY,
      text VARCHAR NOT NULL
    )
  `);
  await client.query(`
    CREATE TABLE IF NOT EXISTS comments (
      id SERIAL PRIMARY KEY,
      text VARCHAR NOT NULL,
      parent_id INT,
      post_id INT,
      CONSTRAINT fk_post
        FOREIGN KEY(post_id)
        REFERENCES posts(id)
    )
  `);

  // Inserção de dados de exemplo
  await client.query(`
    INSERT INTO posts (text) VALUES ('post 1')
  `);
  await client.query(`
    INSERT INTO posts (text) VALUES ('post 2')
  `);
  await client.query(`
    INSERT INTO comments (text, post_id)
    VALUES ('comment 1.1', 1)
  `);
  await client.query(`
    INSERT INTO comments (text, post_id)
    VALUES ('comment 1.2', 1)
  `);
  await client.query(`
    INSERT INTO comments (text, parent_id, post_id)
    VALUES ('comment 1.1.1', (SELECT id FROM comments WHERE text = 'comment 1.1'), 1)
  `);
  await client.query(`
    INSERT INTO comments (text, parent_id, post_id)
    VALUES ('comment 1.1.2', (SELECT id FROM comments WHERE text = 'comment 1.1'), 1)
  `);
  await client.query(`
    INSERT INTO comments (text, post_id)
    VALUES ('comment 2.1', 2)
  `);
  await client.query(`
    INSERT INTO comments (text, post_id)
    VALUES ('comment 2.2', 2)
  `);

  client.release();

  // Criando o servidor
  const server = createServer(pool);
  return server;
};

// Inicia o servidor
startServer().then(server => {
  console.log("Servidor iniciado");
}).catch(err => {
  console.error("Erro ao iniciar o servidor", err);
});

module.exports = { createServer };
