#-*- coding: utf-8 -*-

# Include Fat Jar to Run Spark webframework.
import sys
sys.path.append("./target/spark-fatjar-1.0-SNAPSHOT.jar")

host = '0.0.0.0'
port = 8080

# Import and set host & port.
from spark import Spark
Spark.setIpAddress(host)
Spark.setPort(port)

# Set Handler.
def handle_get(req, res):
    text = req.queryParams("text")
    if text is None:
        text = req.params(":text")
    if text is None or text == "":
        res.status(404)
        return "Not Found"
    print("GET /strlen:", text)
    res.type("text/plain")
    return str(len(text))

def handle_post(req, res):
    import json
    try:
        data = json.loads(req.body())
        text = data.get("text", "")
        print("POST /strlen (JSON type):", text)
        res.type("application/json")
        return json.dumps({"len": len(text)})
    except Exception as e:
        res.status(500)
        res.type("application/json")
        return json.dumps({"error": str(e)})

# Set Route
Spark.get("/strlen", handle_get)
Spark.get("/strlen/:text", handle_get)
Spark.post("/strlen", handle_post)

print('Starting Server %s:%d' % (host, port))
