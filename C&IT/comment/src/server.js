const express = require("express");
const { Pool } = require("pg");

const createServer = (pool, port = 3000) => {
  const app = express();

  // Função para organizar os comentários em árvore
  function organizeComments(comments) {
    const commentMap = {};

    // Cria um mapa de todos os comentários, com id como chave
    comments.forEach(comment => {
      commentMap[comment.id] = { 
        id: comment.id, 
        text: comment.text, 
        parent_id: comment.parent_id, 
        children: [] 
      };
    });

    const rootComments = [];

    // Organiza os comentários em uma árvore com base no parent_id
    comments.forEach(comment => {
      const formattedComment = commentMap[comment.id];

      if (comment.parent_id === null) {
        // Comentário raiz, sem parent_id
        delete formattedComment.parent_id;
        rootComments.push(formattedComment);
      } else {
        // Comentário filho, associa ao parent_id
        const parentComment = commentMap[comment.parent_id];
        if (parentComment) {
          delete formattedComment.parent_id;  // Removendo o parent_id dos filhos também
          parentComment.children.push(formattedComment);
        }
      }
    });

    // Função para remover a chave "children" dos comentários sem filhos
    const cleanEmptyChildren = (comments) => {
      comments.forEach(comment => {
        if (comment.children && comment.children.length === 0) {
          delete comment.children;
        } else if (comment.children && comment.children.length > 0) {
          cleanEmptyChildren(comment.children);
        }
      });
    };

    // Limpa os comentários sem filhos
    cleanEmptyChildren(rootComments);

    return rootComments;
  }

  // Rota para buscar os comentários de um post específico
  app.get("/posts/:postId/comments", async (req, res) => {
    const postId = parseInt(req.params.postId, 10);

    try {
      // Consulta para buscar todos os comentários relacionados ao post
      const result = await pool.query(`
        WITH RECURSIVE CommentTree AS (
          SELECT id, text, parent_id
          FROM comments
          WHERE post_id = $1 AND parent_id IS NULL
          UNION ALL
          SELECT c.id, c.text, c.parent_id
          FROM comments c
          INNER JOIN CommentTree ct ON ct.id = c.parent_id
        )
        SELECT * FROM CommentTree
      `, [postId]);

      const comments = result.rows;

      if (comments.length === 0) {
        return res.status(404).send("No comments found for this post");
      }

      // Organiza os comentários na estrutura hierárquica
      const organizedComments = organizeComments(comments);

      // Retorna os comentários organizados
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

// Função para iniciar o servidor
const startServer = async () => {
  const pool = new Pool({
    connectionString: 'postgresql://postgres:brunao@localhost:5432/comment_system',
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
      CONSTRAINT fk_post FOREIGN KEY(post_id) REFERENCES posts(id)
    )
  `);

  // Inserção de dados
  await client.query(`
    INSERT INTO posts (text) VALUES ('post 1')
  `);
  await client.query(`
    INSERT INTO posts (text) VALUES ('post 2')
  `);
  await client.query(`
    INSERT INTO comments (text, post_id) VALUES ('comment 1.1', 1)
  `);
  await client.query(`
    INSERT INTO comments (text, post_id) VALUES ('comment 1.2', 1)
  `);
  await client.query(`
    INSERT INTO comments (text, parent_id) VALUES ('comment 1.1.1', 1)
  `);
  await client.query(`
    INSERT INTO comments (text, parent_id) VALUES ('comment 1.1.2', 1)
  `);
  await client.query(`
    INSERT INTO comments (text, post_id) VALUES ('comment 2.1', 2)
  `);
  await client.query(`
    INSERT INTO comments (text, post_id) VALUES ('comment 2.2', 2)
  `);

  client.release();

  // Criando e retornando o servidor
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
