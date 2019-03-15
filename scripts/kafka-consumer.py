import sys,json
import pymongo
from kafka import KafkaConsumer


 
class Consumer():
    
    ## Kafka Settings
    TOPIC_NAME = 'starWarsPortal'
    KAFKA_SERVERS = ['localhost:9092']

    ### MongoDB Settings
    MONGODB_SERVER = 'mongodb://localhost:27017/'
    DB_NAME = 'starwarsportal'
    COLLECTION_NAME = 'characters'

    def run(self):
        
        consumer = KafkaConsumer (self.TOPIC_NAME, 
                                  bootstrap_servers = self.KAFKA_SERVERS, 
                                  auto_offset_reset = 'latest', # earliest or latest
                                  enable_auto_commit=False,
                                  value_deserializer=lambda m: json.loads(m))
        
        print("Consumer running...\n")
        
        # Setup mongo connection
        client = pymongo.MongoClient(self.MONGODB_SERVER)
        db = client[self.DB_NAME]
        dbCollection = db[self.COLLECTION_NAME]
        
        print("MongoDB connected...\n\nConsuming messages from topic \"{}\":".format(self.TOPIC_NAME))

        for message in consumer:
            char = json.loads(message.value)
            try:
                # insert into new collection
                dbCollection.create_index([("name", pymongo.ASCENDING)], unique=True)
                dbCollection.insert_one(char).inserted_id
                print ("Character \"{}\" inserted on mongoDB".format(char["name"]))

            except pymongo.errors.DuplicateKeyError:
                # skip document because it already exists in new collection
                continue
  
    def insertIntoMongo(self):
        return True

if __name__ == "__main__":
    #Instance and run the class
    try:
        Consumer().run()
    except KeyboardInterrupt:
        sys.exit()

