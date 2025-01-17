#!/bin/bash

# Build Fat Jar with spark-core
# - https://github.com/perwendel/spark
mvn clean package -DskipTests

# Check server. :)
jython server.py
