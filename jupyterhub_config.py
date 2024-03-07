c = get_config()

c.JupyterHub.authenticator_class = "dummy"

c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.hub_connect_ip = 'jupyterhub'

# built from ./notebook/Dockerfile
c.DockerSpawner.image = 'jupyter-notebook:4.0.2'

c.DockerSpawner.network_name = 'jupyterhub_default'

c.DockerSpawner.remove = True
