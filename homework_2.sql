--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

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
-- Name: dearden; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dearden (
    id integer,
    title character varying(30),
    director character varying(25),
    actors character varying(100),
    year smallint,
    book_author character varying(20)
);


ALTER TABLE public.dearden OWNER TO postgres;

--
-- Name: terminator_movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.terminator_movies (
    id integer,
    title character varying(50),
    director character varying(50),
    actors character varying(100),
    year smallint
);


ALTER TABLE public.terminator_movies OWNER TO postgres;

--
-- Name: topmovies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.topmovies (
    title character varying(50),
    year smallint,
    director character varying(50),
    actors character varying(200)
);


ALTER TABLE public.topmovies OWNER TO postgres;

--
-- Data for Name: dearden; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dearden (id, title, director, actors, year, book_author) FROM stdin;
25	Fight Club	David Fincher	Edward Norton, Brad Pitt, Helena Bonem Carter, Meat Loaf	1999	Chuck Palahniuk
\.


--
-- Data for Name: terminator_movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.terminator_movies (id, title, director, actors, year) FROM stdin;
5	Terminator: Dark Fate	Tim Miller	Linda Hamilton, Arnold Schwarznegger, Mackenzie Davis, Natalia Reyes	2019
1	Terminator	James Cameron	Arnold Schwarznegger, Linda Hamilthon, Michael Biehn	1984
2	Terminator 2:Judgement Day	James Cameron	Arnold Schwarznegger, Linda Hamilthon, Edward Furlong	1991
3	Terminator 3:Rise of the Machines	Jonathan Mostow	Arnold Schwarznegger, Nick Stahl, Kristanna Loken	2003
4	Terminator Salvation	John Brancato, Michael Ferris	Christian Bale, Sam Worthinghton, Moon Bloodgood, Helena Bonem Carter	2009
\.


--
-- Data for Name: topmovies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.topmovies (title, year, director, actors) FROM stdin;
The Shawshank Redemption	1994	Frank Darabont	Tim Robbins, Morgan Freeman
The Silence of the Lambs	1991	Jonathan Demme	Jodie Foster, Anthony Hopkins, Lawrence A. Bonney
Interstellar	2014	Christopher Nolan	Matthew McConaughey, Anne Hathaway, Jessica Chastain
Matrix	1999	The Wachowski Brothers or Sisters xD	Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving
One Flew Over the Cuckoos Nest	1975	Milos Forman	Jack Nicholson, Louise Fletcher, Michael Berryman
Avengers:Endgame	2019	Anthony Russo, Joe Russo	Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson and others...
\.


--
-- PostgreSQL database dump complete
--

