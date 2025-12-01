#########
#ACTIONS#
#########

build: ##@commands Build all containers
	docker compose build

start-all-containers: ##@commands Start all containers
	docker compose up -d

deploy:
	DOCKER_BUILD_TARGET=production make build start-all-containers


#############
#DEVELOPMENT#
#############
test:
	pytest --cov

update-depedencies:
	uv pip compile --group dev pyproject.toml -o requirements.lock
	uv pip sync --system requirements.lock
	rm requirements.lock
