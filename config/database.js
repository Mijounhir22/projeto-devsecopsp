// Remediação: Abstração de credenciais via Variáveis de Ambiente
const dbConfig = {
    host: "localhost",
    user: "root",
    // A senha real não fica no código. O sistema busca no ambiente ou usa um fallback seguro.
    password: process.env.DB_PASSWORD || "configuracao_local_segura",
    database: "sistema_startup"
};

console.log("Infraestrutura de banco de dados carregada com sucesso.");

module.exports = dbConfig;