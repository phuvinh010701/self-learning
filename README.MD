# Building Modern Python Application On AWS
---

## Week1

* What is AWS - Amazone Web Services

* API? - Application programing interface

* SDKs? - Software developments kits

* AWS CLI in AWS Cloud9 python environment (like terminal in Linux/Windows/MacOS)

* API gateway: create, pulishing, maintain, monitor, secure API

## Week2

* Main types in API Gateway: REST API, HTTP API (WebSocket API)

* 6 mechanism for controlling and managing access to arrest API: SSL certificates, CORS, AWS WAF, API keys, resources policies, endpoint policies

* CORS: browser security, ensure only clients from origin url that are allowed to query API

* AWS WAF (Web application firewall): protect API from common web exploits, be configured to filter traffic based on rules that you define

    * First: create API key in API gateway send it to clients. When clients send a request it insert API key in HTTP header. (clear text in request)