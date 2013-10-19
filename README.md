digfont
=======

A font search website


To Contribute

* Fork the repo
* First we virtualenv setup.

```sh
$ sudo easy_install virtualenv
```
* Inside the repo, install your virtual enviornment.

```sh
virtualenv venv
```
* Initialize and activate virtualenv.

```sh
$ cd venv
$ . bin/activate
```
* Install requirements. Before that you would be actually inside venv directory so cd .. out of it to the base of the project.

```sh
$ sudo pip install -r requirements.txt
```
* Start the webserver.

```sh
$ foreman start -f Procfile.dev
```

