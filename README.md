# jython-apiserver
simple jython api server to integrate legacy java code.

this code is very simple using/conversion from JAVA library or code into JSON/POST or GET APIs.

# test
```
curl -X POST -H "Content-Type: application/json" -d '{"text":"some-text"}' http://localhost:8080/strlen
curl http://localhost:8080/strlen?text=some-text
curl http://localhost:8080/strlen/some-text
```

# License
MIT
