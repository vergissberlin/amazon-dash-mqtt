# deploy-button
Deploy your software by push a button

## Docker
```bash
docker run -d --name dasher --net=host -v $(pwd)/config.json:/root/dasher/config clemenstyp/dasher-docker
```

## resin.io

To get this project up and running, you will need to signup for a resin.io account here and set up a device, have a look at our Getting Started tutorial. Once you are set up with resin.io, you will need to clone this repo locally:

$ git clone git@github.com:vergissberlin/deploy-button.git
Then add your resin.io application's remote repository to your local repository:

$ git remote add resin git remote add resin gh_vergissberlin@git.resin.io:gh_vergissberlin/amazondash.git

and push the code to the newly added remote:
$ git push resin master
