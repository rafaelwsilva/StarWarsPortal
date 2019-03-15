<?php

namespace App\Controllers;

use GuzzleHttp\Client;
use GuzzleHttp\RequestOptions;

class Drill {
    
    ## DRILL SETTING
    private $DRILL_URL = "http://localhost:8047/";
        
    public function getCharactersName()
    {
        $client = new Client([
            'base_url' => $this->DRILL_URL,
            'defaults' => [
                'headers' => ['Content-Type' => 'application/json'],
            ]
        ]);

        $query_json = [
            "queryType" => "SQL", 
            "query" => "SELECT chars.name FROM mongo.starwarsportal.`characters` AS chars ORDER BY chars.name"
        ];
    
        $res = $client->post($this->DRILL_URL.'query.json', [ 
            'json' => $query_json
        ]);
        
        return $this->create_response($res);
    }
 
    public function getCharByName($name)
    {
        $client = new Client([
            'base_url' => $this->DRILL_URL,
            'defaults' => [
                'headers' => ['Content-Type' => 'application/json'],
            ]
        ]);

        $query_json = [
            "queryType" => "SQL", 
            "query" => "SELECT * FROM mongo.starwarsportal.`characters` AS chars WHERE LOWER (chars.name)=LOWER ('{$name}')"
        ];

        $res = $client->post($this->DRILL_URL.'query.json', [ 
            'json' => $query_json
        ]);

        return $this->create_response($res);
    }

    public function create_response($res){
        $json = json_decode($res->getBody()->getContents(),true);
        return $json["rows"];
    }
      
}