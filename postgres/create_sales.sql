CREATE TABLE IF NOT EXISTS sales.sales (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    sale_price NUMERIC(10, 2) NOT NULL,  -- Ajuste a precisão e escala conforme necessário
    FOREIGN KEY (customer_id) REFERENCES users.users(id),
    FOREIGN KEY (product_id) REFERENCES products.products(id)
);
