create database if not exists BD_ERP;

use BD_ERP;

create if not exists table clientes(
id int auto_increment,
nome varchar(50),
email varchar(50),
telefone varchar (50),
cpf varchar(50),

primary key(id_cliente)
);

create if not exists table quarto(
id int auto_increment,
numero int,
tipo varchar(30),
preco decimal(10, 2),

primary key(id_quarto)
);

create if not exists table reserva(
id_reserva int auto_increment,
id_cliente int,
id_quarto int,

data_checkin date,
data_checkout date,
estatus varchar(20),

foreign key (id_cliente) references clientes(id),
foreign key (id_quarto) references quarto(id)
);

create if not exists table funcionario(
id int auto_increment,
nome varchar(50),
cargo varchar(100),
cpf varchar(13),

primary key (id)
);

create if not exists table servicos(
id int auto_increment,
nome varchar (50),
preco decimal (10,2)

primary key(id)
);

create if not exists table pagamento(
id int auto_increment,
id_reserva int,
metodo varchar(50),
valor decima(10, 2)

primary key(id),
foreign key (id_reserva) references reserva(id)
);

create if not exists table reserva_quarto(
id_reserva int,
id_servico int, 
quantidade int,

foreign key (id_reserva) references reserva (id),
foreign key (id_servico) references servicos (id)
);