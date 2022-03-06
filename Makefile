up:
	docker build -t spark_with_mysql_jar ./spark
	docker compose up -d

down:
	docker compose down

init_db:
	docker exec -it data_has_power-mysql-1 chmod +x /wait-for-it.sh
	docker exec -it data_has_power-mysql-1 /bin/bash /wait-for-it.sh -t 60 localhost:3306 -- /bin/bash -c "mysql -uroot -proot < /data/application/init_tables.sql"

submit:
	docker exec -it data_has_power-spark-1 spark-submit /src/main.py


all: up init_db submit