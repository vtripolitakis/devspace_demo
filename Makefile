.PHONY: clean up down build

clean:
	devspace cleanup images

build:
	devspace build

up:
	devspace dev

down:
	devspace purge

