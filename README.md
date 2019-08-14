# Cheese Wizards Webapp

> Webapp that helps users plan out the strategies to win the cheese wizards tournament as part of the cheese wizards hackathon.

## Project Setup

* We used this tool: https://github.com/NdagiStanley/vue-django to help us configure our vue-django stack. Note that Some modifications were made to suite our needs.

## Build setup notes for the team

``` bash
cd cheese-wizards-webapp

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# deploy at localhost:8000 using docker (Make sure you run npm install before this)
docker-compose build && docker-compose up

# Destroy using docker
docker-compose down

# Quick deploy front/back end
sh deploy.sh
```

## Additional Notes
### Front-End:
 * Using Vue.js
     * Put all your resources ie. image, fonts in ./cheese-wizards-webapp/static directory
     * You can reference these resources from any part of your app with in the cheese-wizards-webapp directory as follows:
         * /staticfiles/......
     * We are using vue-router, see https://vuejs.org/v2/guide/routing.html
     * Source Directory: ./cheese-wizards-webapp/src (create files, modify files here)

### Back-End:
* Using django
     * Source directory: ./cheese-wizards-webapp/app
     * Settings file can be found in ./cheese-wizards-webapp/vuedj
     * If you used pip to install any python/django dependencies, please include it in requirements.txt

