wget https://github.com/demogorgonz/RaspberryPi-CPUminer/archive/refs/heads/master.zip

unzip master.zip

ls 

cd RaspberryPi-CPUminer-master/

ls 

sudo bash build.sh

./minerd

./minerd -h

./minerd -a scrypt -o stratum+tcp://us.litecoinpool.org:3333 -u #(NOMRE DE USUARIO).#(NOMBRE DE LA MAQUINA) -p #(CONTRASEÑA)
