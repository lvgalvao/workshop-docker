CREATE TABLE IF NOT EXISTS products.products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL  -- Ajuste a precisão e escala conforme necessário
);
