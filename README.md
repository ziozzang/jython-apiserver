# Jython based simple API server example
Very Simple API server with Jython using spark-core. it looks like flask server, but java. this technics are very useful when you integrate legacy java code with other platform.

This code is very simple using/conversion from JAVA library or code into JSON/POST or GET APIs.

This code can be simple starting point to reuse old java code. ;)


# tested env.
- tested on OpenJDK 8 env.

# test as client
```
curl -X POST -H "Content-Type: application/json" -d '{"text":"some-text"}' http://localhost:8080/strlen
curl http://localhost:8080/strlen?text=some-text
curl http://localhost:8080/strlen/some-text
```


# License
MIT
