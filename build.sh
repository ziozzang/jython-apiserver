#!/bin/bash

mvn clean package -DskipTests
jython server.py
