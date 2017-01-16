#!/bin/sh
# develop env initialize shell
### yum update all
yum -y update

### stop firewall
systemctl stop firewalld
systemctl disable firewalld

# install Development Tools
yum -y groupinstall "Development Tools"
yum -y install readline-devel zlib-devel bzip2-devel sqlite-devel openssl-devel

### set timezone
timedatectl set-timezone Asia/Tokyo

### install apach webserver
systemctl restart network.service
yum install -y httpd
systemctl start  httpd.service
systemctl enable httpd.service

### remove mariadb
yum -y remove mariadb-libs.x86_64

# install & start mysql
yum -y localinstall http://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
yum -y install mysql-community-server
echo skip-grant-tables >> /etc/my.cnf
systemctl start mysqld.service
mysql -uroot -e "use mysql; UPDATE user SET authentication_string=password('password') WHERE user='root';flush privileges;"
sed -i "s/skip-grant-tables//g" /etc/my.cnf

#### install git
yum -y install git

### install & upgrade pip
yum -y install python-pip
pip install --upgrade pip
