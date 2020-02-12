--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: conferences; Type: TABLE; Schema: public; Owner: eder
--

CREATE TABLE public.conferences (
    id integer NOT NULL,
    title text NOT NULL,
    summary text NOT NULL,
    date date NOT NULL,
    hour time without time zone NOT NULL,
    creation_date date NOT NULL,
    personid integer
);


ALTER TABLE public.conferences OWNER TO eder;

--
-- Name: conferences_id_seq; Type: SEQUENCE; Schema: public; Owner: eder
--

CREATE SEQUENCE public.conferences_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.conferences_id_seq OWNER TO eder;

--
-- Name: conferences_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: eder
--

ALTER SEQUENCE public.conferences_id_seq OWNED BY public.conferences.id;


--
-- Name: speakers; Type: TABLE; Schema: public; Owner: eder
--

CREATE TABLE public.speakers (
    personid integer NOT NULL,
    name text NOT NULL,
    lastname text NOT NULL,
    description text NOT NULL,
    job text NOT NULL,
    status boolean NOT NULL
);


ALTER TABLE public.speakers OWNER TO eder;

--
-- Name: speakers_id_seq; Type: SEQUENCE; Schema: public; Owner: eder
--

CREATE SEQUENCE public.speakers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.speakers_id_seq OWNER TO eder;

--
-- Name: speakers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: eder
--

ALTER SEQUENCE public.speakers_id_seq OWNED BY public.speakers.personid;


--
-- Name: conferences id; Type: DEFAULT; Schema: public; Owner: eder
--

ALTER TABLE ONLY public.conferences ALTER COLUMN id SET DEFAULT nextval('public.conferences_id_seq'::regclass);


--
-- Name: speakers personid; Type: DEFAULT; Schema: public; Owner: eder
--

ALTER TABLE ONLY public.speakers ALTER COLUMN personid SET DEFAULT nextval('public.speakers_id_seq'::regclass);


--
-- Data for Name: conferences; Type: TABLE DATA; Schema: public; Owner: eder
--

COPY public.conferences (id, title, summary, date, hour, creation_date, personid) FROM stdin;
9	dfgfnhh	jh,jk,jh	2020-03-02	12:00:00	2020-02-12	15
\.


--
-- Data for Name: speakers; Type: TABLE DATA; Schema: public; Owner: eder
--

COPY public.speakers (personid, name, lastname, description, job, status) FROM stdin;
14	dfghjk	dfghjk	dfghjk	dfghjk	t
15	dsfdgfhgf	;jh,hj,gh	bfgbgfngf	bgdgfbxb	t
\.


--
-- Name: conferences_id_seq; Type: SEQUENCE SET; Schema: public; Owner: eder
--

SELECT pg_catalog.setval('public.conferences_id_seq', 9, true);


--
-- Name: speakers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: eder
--

SELECT pg_catalog.setval('public.speakers_id_seq', 15, true);


--
-- Name: conferences conferences_pkey; Type: CONSTRAINT; Schema: public; Owner: eder
--

ALTER TABLE ONLY public.conferences
    ADD CONSTRAINT conferences_pkey PRIMARY KEY (id);


--
-- Name: speakers speakers_pkey; Type: CONSTRAINT; Schema: public; Owner: eder
--

ALTER TABLE ONLY public.speakers
    ADD CONSTRAINT speakers_pkey PRIMARY KEY (personid);


--
-- Name: conferences personid; Type: FK CONSTRAINT; Schema: public; Owner: eder
--

ALTER TABLE ONLY public.conferences
    ADD CONSTRAINT personid FOREIGN KEY (personid) REFERENCES public.speakers(personid) ON DELETE CASCADE;


--
-- Name: speakers personid; Type: FK CONSTRAINT; Schema: public; Owner: eder
--

ALTER TABLE ONLY public.speakers
    ADD CONSTRAINT personid FOREIGN KEY (personid) REFERENCES public.speakers(personid) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

