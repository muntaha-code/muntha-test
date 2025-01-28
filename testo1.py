#sort function
def custom_sort(data):
    if (data, str):
        return ''.join(sorted(data))  
    elif isinstance(data, list):
        if all(isinstance(i, dict) for i in data): 
            return sorted(data, key=lambda x: str(x)) 
        else:
            return sorted(data)  # For a simple array
    elif isinstance(data, int):
        return int(''.join(sorted(str(data))))  # Sort digits in the integer
    else:
        raise TypeError("Unsupported data type")

print(custom_sort("bacd"))  
print(custom_sort([4, 2, 3, 1]))  
print(custom_sort([{"name": "John"}, {"name": "Alice"}]))
print(custom_sort(3142))

#reverse 
def reverse_string(input_string):
    return input_string[::-1]

input_str = "My fav dish is baryani"
print("Reversed String:", reverse_string(input_str))  

#Program to Count Total Words in a File 
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."
file_path = "readfile.txt"
print("Total Words:", count_words_in_file(file_path)) 



#  Request and Response Middleware
''
from flask import Flask, request , jsonify

app = Flask(__name__)
#request
@app.before_request
def before_request():
    print("Request URL:", request.url)
    print("request Header:", request.headers)
#response
@app.after_request
def after_request(response):# like a clint se ds http request , it logs the request and url and header, the request is riute
    response.header["Custom-Header"] = "processed"
    print("Response Header:", response.header)
    return response
@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
#Convert JSON File to CSV File**
import json
import csv
def json_to_csv(json_file, csv_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        #header
        if isinstance(data, list):
            header = data[0].key()
        else:
            headers = data.keys()
        # write to csv
        with open(csv_file, 'w', newline='' ) as file:
            writer = csv.DictWriter(file,fieldname=headers) 
            writer .writeheader()
            if isinstance(data, list):
                writer.writerows(data) 
            else: 
                writer.writerow(data)
        print(f"data converted to{csv_file}.")  
    except Exception as e:
        print(f"Error:{e}")
            
        
        