from dotenv import load_dotenv
import os 
import argparse 
import requests 

load_dotenv() 
api_key = os.getenv("ABUSEIPDB_API_KEY") #  Look up the value stored under the name abuseipdb_api_key and save it in a variable 

if api_key: 
    print("Key loaded")
else: 
    print("Key missing") 

parser = argparse.ArgumentParser(description="Check an IP address on AbuseIPDB")
parser.add_argument("ip", help="The IP address to check")
args = parser.parse_args() 

print("Checking IP:", args.ip) 

url = "https://api.abuseipdb.com/api/v2/check" 

headers = {
    "key": api_key, 
    "Accept": "application/json" 
}

params = {
    "ipAddress": args.ip,
    "maxAgeInDays": 90 
} 

response = requests.get(url, headers=headers, params=params, timeout=10)

print("Status code:", response.status_code) 

data = response.json()["data"]

print()
print("Ip:            ", data["ipAddress"])
print("Abuse score:   ", data["abuseConfidenceScore"])
print("Country:       ", data["countryCode"])
print("ISP:           ", data["isp"])
print("Usage type:    ", data["usageType"])
print("Total reports: ", data["totalReports"])
print("Last reported: ", data["lastReportedAt"])

 
 


