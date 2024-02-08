# website
This project shows how to create website in Flask. All data is stored in a JSON file.

You need to run the following commands:
1) Clone the repository: <br> 
`git clone https://github.com/IgorVolokho99/CRUD_EXAMPLE.git`
2) Create a docker image. Open CMD and in the root folder of project enter the following command: <br>
`docker build -t my-flask-app .` <br>
3) Start the container. Enter the following command to start the container: <br>
`docker run -p 5000:5000 my-flask-app`