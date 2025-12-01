# NTD Challenge

## Getting Started

You will need to configure several issues in order to run it locally. The following tutorial is for 
ubuntu or Linux-based OS only:

### Prerequisites

### Docker & make install instructions ##
To deploy locally or remotely you'll need:
- [docker-engine](https://docs.docker.com/engine/installation/linux/ubuntulinux/)
- [make](https://www.gnu.org/software/make/)

### Installation
1. Clone the repo
   ```sh
   git clone git@github.com:kevinr1299/ntd_challenge.git
   ```
2. create file `.env`, clone from `.env.template ` or run the command
   ```sh
   cp .env.template .env
   ```

   In it, replace the following values:
   - DOCKER_BUILD_TARGET=...
   For this, it needs to be one of the stages defined in the Dockerfile
3. run deploy command according to your needs
   ```sh
   make deploy
   ```
   For the dev stage, it's recommended to use the menu in VS Code to open the Dev-container

## Troubleshooting

### Run coverage

To run the next command. It's needed to build the `develop` target

```bash
make test
```

### Update depedencies
If you are in the dev container and want to add a new dependency, add it to uv and install it in the Python of the container, execute `make update-depedencies`, for example:
```bash
uv add requests
make update-depedencies
```

## Built With
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Gunicorn](https://gunicorn.org/)
