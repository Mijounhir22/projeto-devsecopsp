const dbConfig = {
    host: "localhost",
    user: "root",
    password: process.env.DB_PASSWORD || "chave_segura_placeholder",
    database: "sistema_startup"
};
module.exports = dbConfig;
