--
-- PostgreSQL database dump
--

-- Dumped from database version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: board_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.board_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.board_id_seq OWNER TO root;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: board; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.board (
    id integer DEFAULT nextval('public.board_id_seq'::regclass),
    name text,
    date_creation date,
    date_modification date
);


ALTER TABLE public.board OWNER TO root;

--
-- Name: task_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.task_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.task_id_seq OWNER TO root;

--
-- Name: task; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.task (
    id integer DEFAULT nextval('public.task_id_seq'::regclass),
    header text,
    description text,
    status boolean,
    date_creation date,
    date_modification date,
    board_id integer
);


ALTER TABLE public.task OWNER TO root;

--
-- PostgreSQL database dump complete
--

