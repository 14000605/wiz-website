# Cheese Wizards Webapp

> Webapp that helps users plan out the strategies to win the cheese wizards tournament. This is for a hackathon.

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
```

## Additional Notes
### Front-End
 * Using Vue.js
     * Don't create any files in the ./static folder, this is where all static files are eventually collected (see vuedj/settings.py for more info)
     * We are using vue-router, see https://vuejs.org/v2/guide/routing.html
     * Source Directory: ./src (create files, modify files here)

### Back-End:
* Using django
     * Source directory: ./app

