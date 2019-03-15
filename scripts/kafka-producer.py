import json, os, time, sys
import requests
from kafka import KafkaProducer

class Producer():

    # SWAPI Settings
    URL_SWAPI = 'https://swapi.co/api/people/'
    JSON_PATH = os.path.dirname(os.path.abspath(__file__)) + '/../api-data/'
    JSON_FILE = JSON_PATH+'characters.json'

    #Kafka Settings
    TOPIC_NAME = 'starWarsPortal'
    KAFKA_SERVERS = ['localhost:9092']

    """
        Function used to convert characters result into JSON File. 
        The Json File will be placed on '<project_path>/api-data/characters.json'
    """
    def readChars(self, URL = URL_SWAPI):
        chars = []

        # Create path if it doesn't exist
        if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '/../api-data/') is False:
            os.mkdir(self.JSON_PATH)

        r = requests.get(URL)
        data = r.json() 
        chars = data["results"]

        ## Read the chars until the last page 
        if data["next"] is not None:
            chars.extend(self.readChars(data["next"]))
        
        with open(self.JSON_FILE, 'w') as outfile:  
            json.dump(chars, outfile)

        return chars
 
    """
        Function used to read the JSON file with all characters 
    """
    def readJsonFile(self):

        # Create file if it doesn't exist
        if os.path.exists(self.JSON_FILE) is False:
            self.readChars()

        with open(self.JSON_FILE) as f:
            data = json.load(f)

        return data

    def run(self):
        
        producer = KafkaProducer(bootstrap_servers=self.KAFKA_SERVERS,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        
        print("Producer running...\n")
        characters = self.readJsonFile()

        for char in characters:
            print("Sending character \"{}\"".format(char["name"]))
            producer.send(self.TOPIC_NAME, json.dumps(char)) ## Output the characters for a queue
            time.sleep(0.01)

if __name__ == "__main__":
    #Instance and run the class
    try:
        Producer().run()
    except KeyboardInterrupt:
        sys.exit()