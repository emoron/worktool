CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY,
    order_number TEXT NOT NULL,
    item_name TEXT NOT NULL,
    status_order TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    ord_id TEXT NOT NULL,
    ord_dt DATE NOT NULL,
    qt_ordd INT NOT NULL
);

CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY,
    date_of_rainy DATE NOT NULL,
    was_rainy TEXT NOT NULL
)