DROP DATABASE IF EXISTS cajero;
CREATE DATABASE cajero;
use cajero;


create table Usuario (
identificador int primary key auto_increment,
dni varchar(9),
contraseña varchar(10),
fecha_alta timestamp not null default current_timestamp,
fecha_inactivacion timestamp not null default current_timestamp,
rol varchar(10)
);


create table Sesion (
identificador int primary key  auto_increment,
identificador_usuario int,
fecha_inicio_sesion date,
fecha_fin_sesion timestamp not null default current_timestamp,
FOREIGN KEY (identificador_usuario) REFERENCES Usuario(identificador)
);


create table Transaccion (
identificador int primary key  auto_increment,
identificador_usuario int,
importe int,
fecha_transaccion date,
FOREIGN KEY (identificador_usuario) REFERENCES Usuario(identificador)
);






