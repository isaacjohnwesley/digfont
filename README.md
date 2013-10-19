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
* Install requirements

```sh
$ sudo pip install -r requirements.txt
```
* Start the webserver. Come to the base folder and run

```sh
$ foreman start -f Procfile.dev
```

