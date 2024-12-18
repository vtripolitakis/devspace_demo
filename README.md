# Devspace demo setup

## Set up context and namespace
`devspace use context your_kubernetes_context`

`devspace use namespace your_kubernetes_namespace`

## Build images
`make build`

## Run devspace
`make up`

You should see two services (backend at port 5000 powered by Flask and frontend at port 5173 powered by Vite)

## Stop devspace
Press Ctrl + C to exit and then issue: `make down`

## Cleanup images (if needed)
`make clean`