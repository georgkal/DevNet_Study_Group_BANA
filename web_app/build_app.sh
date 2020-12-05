docker build -t web_app1 .
docker run --name Web_App -d -p 8081:8081 web_app1
