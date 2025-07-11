-- Create database schema
CREATE TABLE IF NOT EXISTS us_states (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    abbreviation VARCHAR(2) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS canadian_provinces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    abbreviation VARCHAR(2) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    code VARCHAR(3) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS user_records (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- drop table if exists user_records CASCADE;
-- SELECT create_iceberg_sync('user_records'::regclass);              

-- Insert sample data for US states
INSERT INTO us_states (name, abbreviation) VALUES 
('Alabama', 'AL'),
('Alaska', 'AK'),
('Arizona', 'AZ'),
('Arkansas', 'AR'),
('California', 'CA'),
('Colorado', 'CO'),
('Connecticut', 'CT'),
('Delaware', 'DE'),
('Florida', 'FL'),
('Georgia', 'GA'),
('Hawaii', 'HI'),
('Idaho', 'ID'),
('Illinois', 'IL'),
('Indiana', 'IN'),
('Iowa', 'IA'),
('Kansas', 'KS'),
('Kentucky', 'KY'),
('Louisiana', 'LA'),
('Maine', 'ME'),
('Maryland', 'MD'),
('Massachusetts', 'MA'),
('Michigan', 'MI'),
('Minnesota', 'MN'),
('Mississippi', 'MS'),
('Missouri', 'MO'),
('Montana', 'MT'),
('Nebraska', 'NE'),
('Nevada', 'NV'),
('New Hampshire', 'NH'),
('New Jersey', 'NJ'),
('New Mexico', 'NM'),
('New York', 'NY'),
('North Carolina', 'NC'),
('North Dakota', 'ND'),
('Ohio', 'OH'),
('Oklahoma', 'OK'),
('Oregon', 'OR'),
('Pennsylvania', 'PA'),
('Rhode Island', 'RI'),
('South Carolina', 'SC'),
('South Dakota', 'SD'),
('Tennessee', 'TN'),
('Texas', 'TX'),
('Utah', 'UT'),
('Vermont', 'VT'),
('Virginia', 'VA'),
('Washington', 'WA'),
('West Virginia', 'WV'),
('Wisconsin', 'WI'),
('Wyoming', 'WY')
ON CONFLICT (name) DO NOTHING;

-- Insert sample data for Canadian provinces
INSERT INTO canadian_provinces (name, abbreviation) VALUES 
('Alberta', 'AB'),
('British Columbia', 'BC'),
('Manitoba', 'MB'),
('New Brunswick', 'NB'),
('Newfoundland and Labrador', 'NL'),
('Northwest Territories', 'NT'),
('Nova Scotia', 'NS'),
('Nunavut', 'NU'),
('Ontario', 'ON'),
('Prince Edward Island', 'PE'),
('Quebec', 'QC'),
('Saskatchewan', 'SK'),
('Yukon', 'YT')
ON CONFLICT (name) DO NOTHING;

-- Insert sample data for countries
INSERT INTO countries (name, code) VALUES 
('United States', 'USA'),
('Canada', 'CAN'),
('Mexico', 'MEX'),
('United Kingdom', 'GBR'),
('France', 'FRA'),
('Germany', 'DEU'),
('Italy', 'ITA'),
('Spain', 'ESP'),
('Japan', 'JPN'),
('Australia', 'AUS'),
('Brazil', 'BRA'),
('India', 'IND'),
('China', 'CHN'),
('Russia', 'RUS'),
('South Africa', 'ZAF')
ON CONFLICT (name) DO NOTHING;
