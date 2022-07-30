--liquibase formatted sql

--changeset robert.julianto:add-table-user
CREATE TABLE ${database.defaultSchemaName}.user
(
    id BIGSERIAL NOT NULL
        CONSTRAINT user_pk
            PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by VARCHAR DEFAULT USER,
    updated_at TIMESTAMPTZ,
    updated_by VARCHAR,
    CONSTRAINT user_unique UNIQUE(email)
);

--changeset robert.julianto:add-table-admin
CREATE TABLE ${database.defaultSchemaName}.admin
(
    id BIGSERIAL NOT NULL
        CONSTRAINT admin_pk
            PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by VARCHAR DEFAULT USER,
    updated_at TIMESTAMPTZ,
    updated_by VARCHAR,
    CONSTRAINT admin_unique UNIQUE(email)
);

--changeset robert.julianto:add-table-event
CREATE TABLE ${database.defaultSchemaName}.event
(
    id BIGSERIAL NOT NULL
        CONSTRAINT event_pk
            PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    date_time TIMESTAMPTZ NOT NULL,
    venue VARCHAR NOT NULL,
    venue_address VARCHAR NOT NULL,
    venue_latitude DOUBLE PRECISION,
    venue_longitude DOUBLE PRECISION,
    city VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    pic VARCHAR NOT NULL,
    pic_contact VARCHAR NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by VARCHAR DEFAULT USER,
    updated_at TIMESTAMPTZ,
    updated_by VARCHAR
);

--changeset robert.julianto:add-index-event-name
CREATE INDEX event__name__idx
    ON ${database.defaultSchemaName}.event(name);

--changeset robert.julianto:add-table-reservation
CREATE TABLE ${database.defaultSchemaName}.reservation
(
    id BIGSERIAL NOT NULL
        CONSTRAINT reservation_pk
            PRIMARY KEY,
    event_id BIGINT NOT NULL
        CONSTRAINT reservation__event_id__fk
            REFERENCES ${database.defaultSchemaName}.event,
    user_id BIGINT NOT NULL
        CONSTRAINT reservation__user_id__fk
            REFERENCES ${database.defaultSchemaName}.user,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by VARCHAR DEFAULT USER,
    updated_at TIMESTAMPTZ,
    updated_by VARCHAR
);

--changeset robert.julianto:add-index-reservation-event_id
CREATE INDEX reservation__event_id__idx
    ON ${database.defaultSchemaName}.reservation(event_id);

--changeset robert.julianto:add-index-reservation-user_id
CREATE INDEX reservation__user_id__idx
    ON ${database.defaultSchemaName}.reservation(user_id);

--changeset robert.julianto:add-table-email
CREATE TABLE ${database.defaultSchemaName}.email
(
    id BIGSERIAL NOT NULL
        CONSTRAINT email_pk
            PRIMARY KEY,
    event_id BIGINT NOT NULL
        CONSTRAINT email__event_id__fk
            REFERENCES ${database.defaultSchemaName}.event,
    subject VARCHAR NOT NULL,
    content VARCHAR NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by VARCHAR DEFAULT USER,
    updated_at TIMESTAMPTZ,
    updated_by VARCHAR
);

--changeset robert.julianto:add-index-email-event_id
CREATE INDEX email__reservation_id__idx
    ON ${database.defaultSchemaName}.email(event_id);
