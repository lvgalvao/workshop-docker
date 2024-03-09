-- Criação da tabela 'users'
CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    birthdate DATE NOT NULL
);

-- Criação da tabela 'products'
CREATE TABLE IF NOT EXISTS public.products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL  -- Ajuste a precisão e escala conforme necessário
);

-- Criação da tabela 'sales'
CREATE TABLE IF NOT EXISTS public.sales (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    sale_price NUMERIC(10, 2) NOT NULL,  -- Ajuste a precisão e escala conforme necessário
    FOREIGN KEY (customer_id) REFERENCES public.users(id),
    FOREIGN KEY (product_id) REFERENCES public.products(id)
);
