const { Pool } = require("pg");

const dbUrl = "postgresql://postgres:brunao@localhost:5432/comment_system"; // Substitua com as suas credenciais reais
const pool = new Pool({ connectionString: dbUrl });

pool.connect()
  .then(() => console.log("Conexão com o banco de dados bem-sucedida!"))
  .catch((err) => console.error("Erro ao conectar ao banco de dados", err.stack));
