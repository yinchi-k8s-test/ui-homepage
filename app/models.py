"""Service SQLModel Model."""

from sqlmodel import Field, SQLModel


class Service(SQLModel, table=True):
    """A registered service to be displayed on the homepage of the cluster's web service.
    (Here we specifically mean the web service exposed by the `web` entrypoint of the Traefik
    proxy service.)"""

    name: str = Field(
        title='Name',
        description='A human-readable name, e.g. "phpMyAdmin".',
        max_length=256
    )

    cluster_name: str = Field(
        title='Cluster name',
        description="""\
Name of the service on the cluster. Must be unique. In many cases, this will be an auxiliary
UI service to a data-store service, e.g. `ds-mariadb-phpmyadmin`. In such
cases, the core service's cluster name should form the prefix of the current service's name.""",
        primary_key=True,
        max_length=256
    )

    protocol: str = Field(
        title='Protocol',
        description='Protocol for the service, i.e. HTTP or HTTPS.',
        default='http',
        max_length=256
    )

    port: int = Field(
        ge=1024,   # Avoid privledged ports
        lt=30000,  # Stay below start of Kubernetes NodePort range
        title='Port',
        description="""\
Port on the host machine to access the service. Expose the service on this port using
`kubectl port-forward`."""
    )

    path: str = Field(
        title='Path',
        description="""\
Path to the service's front page. The full URL to be displayed on the homepage will be
`http://<hostname>:<port>/<path>`.""",
        max_length=1024
    )
