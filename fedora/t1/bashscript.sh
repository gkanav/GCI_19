#!/bin/bash

steghide embed -cf image.jpeg -ef secret.txt

sleep 5

steghide extract -sf image.jpeg

