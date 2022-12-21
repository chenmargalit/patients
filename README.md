To Run the project please operate according to the following steps:

1. Run the docker compose file
2. enter http://0.0.0.0:8000/inference?patientId=<someId>&text=<someText>
* note you should change the someId to a number and someText to any text you wish.


Considerations to mention:
I floundered between using a persistent db such as postgres and a much faster cache like Redis. I ended up choosing Postgres because of its persistency. In real life that decision would probably be made according to product priorities.