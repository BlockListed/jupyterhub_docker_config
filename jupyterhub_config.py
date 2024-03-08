c = get_config()

c.JupyterHub.authenticator_class = "generic-oauth"

# assumes oauth provider run with:
# docker run --rm -it -p 127.0.0.1:8080:8080 ghcr.io/navikt/mock-oauth2-server:2.1.1

provider = "http://192.168.178.96:8080/default"
c.GenericOAuthenticator.authorize_url = f"{provider}/authorize"
c.GenericOAuthenticator.token_url = f"{provider}/token"
c.GenericOAuthenticator.userdata_url = f"{provider}/userinfo"
c.GenericOAuthenticator.scope = ["openid", "somescope", "otherscope"]

# these are the defaults. They can be configured at http://localhost:8080/default/debugger
c.GenericOAuthenticator.client_id = "debugger"
c.GenericOAuthenticator.client_secret = "someSecret"

# 'sub' is the first field in the login form
c.GenericOAuthenticator.username_claim = "sub"

c.GenericOAuthenticator.allow_all = True
c.GenericOAuthenticator.admin_users = {"admin"}

c.GenericOAuthenticator.enable_auth_state = True

c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.hub_connect_ip = 'jupyterhub'

# built from ./notebook/Dockerfile
c.DockerSpawner.image = 'jupyter-notebook:4.0.2'

c.DockerSpawner.network_name = 'jupyterhub_default'

c.DockerSpawner.remove = True

def access_token_hook(spawner, auth_state):
    spawner.log.info("print auth state")
    spawner.log.info(auth_state['access_token'])

    spawner.env['OAUTH_ACCESS_TOKEN'] = auth_state['access_token']

c.DockerSpawner.auth_state_hook = access_token_hook
