import csv
import json
import subprocess

def post_data_to_api(url, payload):
    curl_command = ['curl', '-X', 'POST', '-H', 'Content-Type: 
application/json', '-d', payload, url]
    subprocess.run(curl_command)

def csv_to_json(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Set variables from CSV data
            variable1 = row['Column1']
            variable2 = row['Column2']
            variable3 = row['Column3']
            
            # Create JSON payload
            payload = json.dumps({
                'variable1': variable1,
                'variable2': variable2,
                'variable3': variable3
            })
            
            # Call the API with cURL
            api_url = 'http://example.com/api'  # Replace with your API endpoint
            post_data_to_api(api_url, payload)

# Usage example
csv_file_path = 'data.csv'  # Replace with your CSV file path
csv_to_json(csv_file_path)
