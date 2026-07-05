#!/bin/bash

cp .env.example .env
docker run --env-file .env --network faraja-network -p 8000:8000 faraja-backend
