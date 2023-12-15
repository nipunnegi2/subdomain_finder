Subdomain Finder

Overview
Subdomain Finder is a Python-based tool designed to quickly discover subdomains for a given domain. It leverages threading to improve performance and allows users to specify a custom wordlist for subdomain enumeration.

Features
Fast subdomain discovery
Custom wordlist support
Multi-threading for improved performance
Verbose output option

Usage
To use the Subdomain Finder, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/nipunnegi2/subdomain_finder.git
Navigate to the project directory:

bash
Copy code
cd subdomain-finder
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the tool with the desired domain:

bash
Copy code
python subdomain_finder.py example.com -w wordlist.txt -t 500 -V
-w or --wordlist: Specify the path to your custom wordlist (default is wordlist.txt).
-t or --threads: Set the number of threads to use (default is 500).
-V or --verbose: Enable verbose output.
View the results:

bash
Copy code
Sub Domains Found -
https://subdomain1.example.com
https://subdomain2.example.com
...

Time taken - 10.24 seconds
Contributing
If you want to contribute to this project, please follow these guidelines...

License
This project is licensed under the MIT License.


Contact
For any inquiries, please contact nipunnegi2002@gmail.com
