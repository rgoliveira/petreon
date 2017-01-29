# Petreon [![Build Status](https://travis-ci.org/rgoliveira/petreon.svg?branch=master)](https://travis-ci.org/rgoliveira/petreon) 
![Petreon Logo](/assets/petreon.png)

This is a project that aids the creation of a platform for Non-Profit Organizations that targets dog adoption/donation campaigns via a web interface. We're currently in early stages of design and development.

## What's going on

- Current project status and what's being worked on can be seen at our public Trello board - [Platform Development](https://trello.com/b/a8WBTniU/platform-development) - and at the [issue tracker of this repository](https://github.com/rgoliveira/petreon/issues).
- To get in touch with the dev team, you're welcome to join our Discord server: [Programming Discussions](https://discord.gg/9zT7NHP).

## Development Guide

### Requirements

- [Docker](https://www.docker.com/) and [Compose](https://docs.docker.com/compose/install/)
- [node & npm](https://nodejs.org/en/)
  - Or you could use `nvm` to easily switch between node versions: [\*nix & mac](https://github.com/creationix/nvm), [windows](https://github.com/coreybutler/nvm-windows)
  
### Running a local instance

- To get started with the API, run `docker-compose up` from the repository root. This will start the `postgres` container and the application container. You can then edit the files inside `api/`. If the API container is running flask's debug server, your changes should be automatically reloaded.
- To get started with the frontend, go to the `frontend` folder, run `npm install` to get all the dependencies, and then `npm start` to launch the development server.


## Provided to you by the team number one
![Team One Flag](/assets/team_flag.png)
