WINC BED CONTINOUS DEPLOYMENT

Short overview.
This assignment required that I set up a CD (continuous deployment) pipeline. In short, a developer writes some new code on their local machine, pushes this new code to the repository on github, github then uses a action to automatically test the code, and (if these tests are successful) uploads the new code to the server which is running the application.

THREE COMPONENTS OF THE SOLUTION

SSH server access
I have set-up a SSH key which allows github actions to access the server at digital ocean which is required to execute the necessary scripts on the server. The SSH key has been added to githubs "secrets" so that it can be used inside github actions without compromising the keys contents.

Main.py
Code for pushing with use of Flask. With Flask we publish hello world to app using fuction app.route. The main route goes to Hello, World!

Requirements.txt
Github actions run-pipeline gets stored in this documents. You see this in the run-pipeline.yml file with the sentence: pip install -r requirements.txt

SOME PROBLEMS

SSH keys
Figuring out i had to login as root on droplet server and generate a public/private key took me a while.

Connecting GitHub and Digital Ocean.
The necessary steps I had to take to make the connection with github. By looking on google i found https://medium.com/swlh/how-to-deploy-your-application-to-digital-ocean-using-github-actions-and-save-up-on-ci-cd-costs-74b7315facc2. This link helped me to get the connection started.

Working Git actions
I had an issue with getting my gitactions working.
Some workflow names where incorrect.
Before I found the link above I didn't get the connection working with droplet to update the site. Fixing the names so the test did run. Creating the correct connection with github and adding the right secrets

In the end i didn't struggle too much with this assignment. Had some help from Google and Chatgpt to solve some small issues.
