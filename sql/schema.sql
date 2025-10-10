CREATE DATABASE wms;

CREATE SCHEMA IF NOT EXISTS stg;

CREATE SCHEMA IF NOT EXISTS wh;

CREATE TABLE IF NOT EXISTS stg.receive (
	id serial PRIMARY KEY,
	po_date date,
	po_number VARCHAR(50),
	po_number_client VARCHAR(50),
	warehouse VARCHAR(10),
	received_date date,
	inbound_date date,
	client_name TEXT,
	sku VARCHAR(100),
	description TEXT,
	brand VARCHAR(100),
	category VARCHAR(100),
	unit VARCHAR(20),
	lwh VARCHAR(50),
	l_cm NUMERIC,
	w_cm NUMERIC,
	h_cm NUMERIC,
	weight_g NUMERIC,
	quantity_new INT,
	quantity_damaged INT,
	qty_per_case INT,
	po_status VARCHAR(50),
	completed_ib_date BOOLEAN,
	product_value NUMERIC,
	client_reference_code VARCHAR(100),
	client_code VARCHAR(20),
	po_extra_service TEXT,
	created_at TIMESTAMP DEFAULT current_timestamp,
	reference_source VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS stg.packed (
	id serial PRIMARY KEY,
	so_date date,
	so_number VARCHAR(50),
	so_number_client VARCHAR(100),
	biztype VARCHAR(50),
	so_status VARCHAR(50),
	warehouse VARCHAR(10),
	packed_date date,
	client_name TEXT,
	sku VARCHAR(100),
	description TEXT,
	brand VARCHAR(100),
	category VARCHAR(100),
	unit VARCHAR(20),
	lwh VARCHAR(50),
	l_cm NUMERIC,
	w_cm NUMERIC,
	h_cm NUMERIC,
	weight_g NUMERIC,
	packed_qty INT,
	cancelled_note TEXT,
	so_extra_service TEXT,
	client_reference_code VARCHAR(100),
	client_code VARCHAR(20),
	shipping_service VARCHAR(20),
	created_at TIMESTAMP DEFAULT current_timestamp,
	reference_source VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS stg.load_tracking (
	id serial PRIMARY KEY,
	table_name VARCHAR(50),
	file_name VARCHAR(100),
	load_date TIMESTAMP DEFAULT current_timestamp,
	record_count INT,
	UNIQUE (table_name, file_name)
);