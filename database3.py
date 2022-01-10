import mysql.connector

db = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : 'SampleDB'
}

cnt = mysql.connector.connect(**db)
crs = cnt.cursor()

# table = """Create table products(
#     productCode varchar(15) NOT NULL,
#     productName varchar(70) NOT NULL,
#     productLine varchar(50) NOT NULL,
#     productScale varchar(10) NOT NULL,
#     productVendor varchar(50) NOT NULL,
#     productDescription text NOT NULL,
#     quantityInStock smallint(6) NOT NULL,
#     buyPrice decimal(10,2) NOT NULL,
#     MSRP decimal(10,2) NOT NULL,
#     PRIMARY KEY (productCode)
# ) engine = InnoDB
# """ 

# crs.execute(table)
# print("berhasil")

# data = "insert into products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# isi_data =  [
# ]
# for i in isi_data:
#     crs.execute(data, i)
#     cnt.commit() 

# print("Berhasil memasukan data")

crs.execute("alter table customers add constraint fk_customers_employee foreign key(salesRepEmployeeNumber) references employees(employeeNumber) on update cascade")
print("Berhasil")