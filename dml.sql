use cajero;
select * from Usuario;
insert into Usuario (dni, contraseña, rol) values ("admin", "0000", 1);


create user Administrador identified by "passwd000";
GRANT ALL ON cajero TO Administrador WITH GRANT OPTION;
insert into Usuario (dni, contraseña) values ("78502329", "1234");


use mysql;
select * from user where user = "Administrador";

