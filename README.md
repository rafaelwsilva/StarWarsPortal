# Star Wars Portal

A very simple project showing the sending of a message to an [Apache Kafka](https://kafka.apache.org/) topic, the consumption of the same message with the insertion of that message into [MongoDB](https://www.mongodb.com/). Finishing with the consuption of mongoDB using [Apache Drill](https://drill.apache.org).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

In order to run this project you must have these tools installed:

- Composer
- Python
- An webserver (i.e. Apache2)
- MongoDB
- Apache Kafka
- Apache Drill
- Java
- Zookeeper

## Installation

### Clone

Clone this repo to your local machine using https://github.com/rafaelwsilva/StarWarsPortal

### Configuration

If you will not run the `mongoDB`, `Apache Kafka` and `Apache Drill` at the same host of webserver, you must change the following files. You also can change the topic, database and collection name as desired.

> `scripts/kafka-consumer.py`

```python
## Kafka Settings
TOPIC_NAME = 'starWarsPortal'
KAFKA_SERVERS = ['localhost:9092']

### MongoDB Settings
MONGODB_SERVER = 'mongodb://localhost:27017/'
DB_NAME = 'starwarsportal'
COLLECTION_NAME = 'characters'
```

> `scripts/kafka-producer.py`

```python
#Kafka Settings
TOPIC_NAME = 'starWarsPortal'
KAFKA_SERVERS = ['localhost:9092']
```

> `app/api/src/Controllers/Drill.php`

```php
private $DRILL_URL = "http://localhost:8047/";
```

### Setup

> Start mongoDB server. The database will be created during script execution

```shell
sudo service mongoDB start
```

> Dowload and start the Kafka server (keep this server running).

```shell
sudo apt update
sudo apt install openjdk-8-jdk zookeeperd
sudo service zookeeper start
cd ~
wget http://ftp.unicamp.br/pub/apache/kafka/2.1.0/kafka_2.11-2.1.0.tgz 
tar -xzf kafka_2.11-2.1.0.tgz
cd kafka_2.11-2.1.0
bin/kafka-server-start.sh config/server.properties
```

> Using another terminal, dowload and start the Apache Drill (keep this server running).

```shell
cd ~
wget http://apache.mirrors.hoobly.com/drill/drill-1.15.0/apache-drill-1.15.0.tar.gz
tar -xvzf apache-drill-1.15.0.tar.gz
cd apache-drill-1.15.0
bin/drill-embedded
```

> Install python dependencies using pip

```shell
cd <project_path>/scripts
pip install -r requirements.txt
```

> Copy the content of folder `app` to webserver folder. (i.e.: for apache2 the fokder is `/var/www/html` )

```shell
cd <project_path>
sudo mkdir /var/www/html/starWarsPortal
sudo cp <project_path>/app/* /var/www/html/starWarsPortal
```

> Go to webserver folder and install the dependencies using composer

```
cd /var/www/html/starWarsPortal/api
composer install
```

### Running

This sequence must be respected.

> Start the kafka consumer

    python scripts/kafka-consumer.py

> Using another terminal, run the kafka producer

    python scripts/kafka-producer.py

> Access the `http://localhost/starWarsPortal/` and you will see  the Star Wars characters list, if you click on some of them you have more info about him.

### API Endpoing

> Also are available two endpoints to get the characters details as JSON format

- GET `api/chars`

```shell
$ curl -XGET http://localhost/starWarsPortal/api/chars/yoda
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1961  100  1961    0     0  15201      0 --:--:-- --:--:-- --:--:-- 15201[{"name":"Ackbar"},{"name":"Adi Gallia"},{"name":"Anakin Skywalker"},{"name":"Arvel Crynyd"},{"name":"Ayla Secura"},{"name":"BB8"},{"name":"Bail Prestor Organa"},{"name":"Barriss Offee"},{"name":"Ben Quadinaros"},{"name":"Beru Whitesun lars"},{"name":"Bib Fortuna"},{"name":"Biggs Darklighter"},{"name":"Boba Fett"},{"name":"Bossk"},{"name":"C-3PO"},{"name":"Captain Phasma"},{"name":"Chewbacca"},{"name":"Cliegg Lars"},{"name":"Cord\u00e9"},{"name":"Darth Maul"},{"name":"Darth Vader"},{"name":"Dexter Jettster"},{"name":"Dooku"},{"name":"Dorm\u00e9"},{"name":"Dud Bolt"},{"name":"Eeth Koth"},{"name":"Finis Valorum"},{"name":"Finn"},{"name":"Gasgano"},{"name":"Greedo"},{"name":"Gregar Typho"},{"name":"Grievous"},{"name":"Han Solo"},{"name":"IG-88"},{"name":"Jabba Desilijic Tiure"},{"name":"Jango Fett"},{"name":"Jar Jar Binks"},{"name":"Jek Tono Porkins"},{"name":"Jocasta Nu"},{"name":"Ki-Adi-Mundi"},{"name":"Kit Fisto"},{"name":"Lama Su"},{"name":"Lando Calrissian"},{"name":"Leia Organa"},{"name":"Lobot"},{"name":"Luke Skywalker"},{"name":"Luminara Unduli"},{"name":"Mace Windu"},{"name":"Mas Amedda"},{"name":"Mon Mothma"},{"name":"Nien Nunb"},{"name":"Nute Gunray"},{"name":"Obi-Wan Kenobi"},{"name":"Owen Lars"},{"name":"Padm\u00e9 Amidala"},{"name":"Palpatine"},{"name":"Plo Koon"},{"name":"Poe Dameron"},{"name":"Poggle the Lesser"},{"name":"Quarsh Panaka"},{"name":"Qui-Gon Jinn"},{"name":"R2-D2"},{"name":"R4-P17"},{"name":"R5-D4"},{"name":"Ratts Tyerell"},{"name":"Raymus Antilles"},{"name":"Rey"},{"name":"Ric Oli\u00e9"},{"name":"Roos Tarpals"},{"name":"Rugor Nass"},{"name":"Saesee Tiin"},{"name":"San Hill"},{"name":"Sebulba"},{"name":"Shaak Ti"},{"name":"Shmi Skywalker"},{"name":"Sly Moore"},{"name":"Tarfful"},{"name":"Taun We"},{"name":"Tion Medon"},{"name":"Wat Tambor"},{"name":"Watto"},{"name":"Wedge Antilles"},{"name":"Wicket Systri Warrick"},{"name":"Wilhuff Tarkin"},{"name":"Yarael Poof"},{"name":"Yoda"},{"name":"Zam Wesell"}]

```

- GET `api/ chars/{name}`

```shell
$ curl -XGET http://localhost/starWarsPortal/api/chars/yoda
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   642  100   642    0     0   3689      0 --:--:-- --:--:-- --:--:--  3689[{"films":"[\"https:\/\/swapi.co\/api\/films\/2\/\",\"https:\/\/swapi.co\/api\/films\/5\/\",\"https:\/\/swapi.co\/api\/films\/4\/\",\"https:\/\/swapi.co\/api\/films\/6\/\",\"https:\/\/swapi.co\/api\/films\/3\/\"]","homeworld":"https:\/\/swapi.co\/api\/planets\/28\/","gender":"male","skin_color":"green","edited":"2014-12-20T21:17:50.345000Z","created":"2014-12-15T12:26:01.042000Z","mass":"17","vehicles":"[]","url":"https:\/\/swapi.co\/api\/people\/20\/","hair_color":"white","birth_year":"896BBY","eye_color":"brown","species":"[\"https:\/\/swapi.co\/api\/species\/6\/\"]","starships":"[]","name":"Yoda","_id":"[B@563a8704","height":"66"}]

```
