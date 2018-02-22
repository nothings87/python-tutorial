#!/usr/bin/env python3

import requests, json

URL = 'http://localhost:3000/DVRS/post-json.cgi'

sample = {
    "resultCode" : 200,
    "resultMessage" : "success",
    "filelist" : [ 
        { "video1" : "check" }, 
        { "video2" : "no" } 
    ],
    "morelist" : [
        {
            "type" : "dir",
            "name" : "Video",
            "mimeType" : "",
            "fileLength" : 0,
            "playType" : 0
        },
        {
            "type" : "file",
            "name" : "video1.mp4",
            "mimeType" : "video/mp4",
            "fileLength" : 12000,
            "playTime" : 240
        }
    ]
}


sample_json_data = json.dumps(sample);

# sample_json_data = json.load(open('sample01.json'))

# Generate JSON from python data structure
# response = requests.post(URL, data=json.dumps(sample));
response = requests.post(URL, data=sample_json_data);

print(">>>status code");
print(response.status_code);

print("");
print(">>>response");
print(response.text);

