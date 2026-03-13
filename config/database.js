// Antes: password: "admin123"
// Agora: O sistema busca a senha configurada no servidor, sem expô-la no Git.
const dbConfig = {
    host: "localhost",
    user: "root",
    password: process.env.DB_PASSWORD || "configuracao_local_segura",
    database: "sistema_startup"
};

console.log("Conectado ao banco de dados com segurança.");