$ mysql -u root -h localhost -p <pass>

CREATE DATABASE retail_db;
USE retail_db;
CREATE USER 'retail_dba'@'%' IDENTIFIED BY 'retail_dba';
GRANT ALL PRIVILEGES ON retail_db.* TO 'retail_dba'@'%';

// https:
//www.cyberciti.biz/faq/how-to-delete-remove-user-account-in-mysql-mariadb/

cargar los datos:

$ mysql -u retail_dba -p retail_db < retail_db-data.sql