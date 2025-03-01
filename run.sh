#!/usr/bin/env bash

podman run -d --restart "unless-stopped"  --env-file .env colectivos_ws/extract:latest 