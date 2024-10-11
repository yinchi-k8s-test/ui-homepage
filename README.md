# Homepage

This repo contains the code for creating a Docker container to host a homepage for our Kubernetes cluster. The homepage contains a set of links to the public services of the cluster, as read from a MariaDB database.

### Setup

Copy `secret.example.env` to `secret.env` and edit the connection string in `DB_URL`.

- If the MariaDB database server is exposed (e.g. via `kubectl port-forward`), it is possible to run the homepage app directly outside of Kubernetes.
- If running via Kubernetes only, then the value of `DB_URL` in `secret.env` does not matter as it will be overridden by the environment variable set by the Helm chart.

### Local development server

To run the homepage app in a development server, first install `uv` from <https://docs.astral.sh/uv/getting-started/installation/>.  Next, ensure that your MariaDB instance is exposed via `kubectl port-forward` and edit `secret.env` accordingly.

Finally, from the repo root:
```bash
uv run python -m app.ui
```

> [!NOTE]
> This will launch the app using Plotly Dash's built-in development server.  For production purposes, the `Dockerfile` uses `gunicorn` instead.

### Docker container

Our Kubernetes cluster has its own container registry at `http://localhost:32000`. To build the Docker container and deploy to the Kubernetes cluster:
```bash
docker buildx build . -t localhost:32000/ui-homepage:latest --push
```

See the [corresponding README.md file](https://github.com/yinchi-k8s-test/microk8s/tree/main/ui-homepage) in the `microk8s` repo.  Note that the Docker container serves the homepage app from port `8000`.
