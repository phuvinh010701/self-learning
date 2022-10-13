# Building Modern Python Application On AWS
---

## Week1

* What is AWS - Amazone Web Services

* API? - Application programing interface

* SDKs? - Software developments kits

* AWS CLI in AWS Cloud9 python environment (like terminal in Linux/Windows/MacOS)

* API gateway: create, pulishing, maintain, monitor, secure API

## Week2

* Main types in API Gateway: REST API, HTTP API, (WebSocket API)

* 6 mechanism for controlling and managing access to arrest API: SSL certificates, CORS, AWS WAF, API keys, resources policies, endpoint policies

* CORS: browser security, ensure only clients from origin url that are allowed to query API

* AWS WAF (Web application firewall): protect API from common web exploits, be configured to filter traffic based on rules that you define

    * First, create API key in API gateway send it to clients. When clients send a request it insert API key in HTTP header. (clear text in request)

## Week3

* AWS Lamda: is a computer service let u run code without provisioning or managing servers

* Lambda function: packaging of the code that processes events

* Event: is a JSON formatted docment containing data for a function to process

* Concurrency: is the number of requests a function is serving at any given time

* Trigger: is resource or configuration that invokes a function

* 2 ways to invoke lambda function: invok directly by calling API, set up triggers to invoke 

* AWS Lambda Push/ Pull Modelshuts (when setting up a trigger):
	* push model is where a trigger sends an event to lambda, which invokes lambda function. (resource-based policy must allow trigger to invoke lambda f)
	* pull model AWS lambda pulls the event from the event source then invokes the lambda function.

* SQS allows messages to build up in a queue and then code would process those messages

* asynchronous vs synchronous lambda functions. For example s3 invokes lambda asynchronously, client -> api gateway -> invoke lambda synchronously

## Week4

* A state machine is a collection of states which allow you to perform the tasks in sequence

* States are individuals elements of the state machine that make decisions base on inputs, perform actions, and provide output.

* Tasks represent one unit of work done through activities or aws services. Task like a worker

* 8 types of state of function

	Task: do something
	Choice: make some decisions
	Parallel: execute somework in parallel
	Map: execute portions of u state machine concurrently from array
	Pass: trouble shooting, build stick machine
	Wait: Add sleep statements
	Success and Failure: stop execution
