# FC-Palermo-Project

This project is part of EECE430 course.

The main repository is on @EECE430-group1

A website and managemnet system for a football club (FC Palermo). 
A user can sign in as an admin or as a fan/member.
The admin can access the management system and functionalities (like adding/updating/removing events and tickets).
The fans/members can register/login to access all available features (club's schedule, available tickets, etc).

## What we used:

- For database manipulation: SQL with Python and Jinja (via a Flask application)
- Any IDE with Python interpreter (spyder recommended)
- A database engine to implement SQL standards: PostgreSQL, and pgAdmin as the management tool

## To run the project:

In order to be able to run the project on your pc, you will need to:

- Download pgAdmin4 and PostgreSQL:
   - pgAdmin4: https://www.pgadmin.org/download/
   - PostgreSQL: https://www.postgresql.org/download/

- Please use the following credentials to create the server:
   - Host Name/address : localhost 
   - Port : 5432
   - Maintenance database : postgres
   - Username : postgres
   - Password : Anar19672001 (If you used a different password, you will need to update it in app.py)

- Create a new database and call it 'Palermo' (Again, if you used a different name, you will need to update it in app.py)

- Using the query tool, create the following tables:
```
create table schedule(
	e_id varchar(3) not null,
	title varchar(50) not null,
	description varchar(255) not null,
	e_date varchar(10) not null,
	e_time varchar(11) not null,
	location varchar(30) not null,
	primary key (e_id)
);

create table tickets(
	t_id varchar(3) not null,
	title varchar(30) not null,
	t_date varchar(10) not null,
	t_time varchar(11) not null,
	price numeric(5,2) not null,
	loc varchar(30) not null,
	rem int not null,
	primary key(t_id)
);

create table admins(
	email varchar(35) not null,
	username varchar(8) not null,
	pass varchar(12) not null,
	primary key(username)
);

create table coaches (
	c_id varchar(2) not null,
	c_name varchar(25) not null,
	start_date varchar(4) not null,
	end_date varchar(7),
	age int not null,
	primary key(c_id)
);

create table players (
	p_id varchar(2) not null,
	name varchar(25) not null,
	role varchar(20) not null,
	age int not null,
	primary key(p_id)
);

create table users (
	email varchar(35) not null,
	username varchar(8) not null,
	pass varchar(12) not null,
	country varchar(20) not null,
	dob varchar(10) not null,
	primary key(username)
);
```

- You will also need to populate each table:
  - populating tables example:
`insert into tickets values('13', 'FC Palenka vs FC Palermo', '17/05/2022', '08:00-09:30', 50, 'Camp Nou Stadium', 73);`

- Install the following in the project's directory:
```
pip install psycopg2
pip install flask
```

- Finally, run:
```
run flask
localhost:5000
```























