#Para instalar ejecutar los siguientes comandos:
sudo apt install python3-pip
sudo pip3 install locustio==0.14.6
sudo pip3 install odoo-client-lib

#Para ejecutar la prueba estandar se debe configurar odoo con
workers = 0

#El comando de ejecucion es el siguiente:
python3 /usr/local/bin/locust -f OdooLocust/test.py Seller
