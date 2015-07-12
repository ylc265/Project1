# Project1
Getting Started From Nothing To Running

## Install Homebrew

`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
`

## Install Python 3
`brew install python3`

## Install Virtual Environment
`pip install virtualenv`

## Install Solr
Download tar file [solr-4.10.2.tgz](http://archive.apache.org/dist/lucene/solr/4.10.2/)
Unpack:
`tar -xvf solr-4.10.2.tgz`
Run Solr:
`java -jar solr-4.10.2/example/start.jar`

## Install Postgres [Video Tutorial Here](https://www.youtube.com/watch?v=XB-D5p_FnnA)
Install:

`brew install postgres`

Initialize:

`initdb /usr/local/var/postgres -E utf8`

Run Postgres:

`pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start`

Create database:

`createdb <database_name> (this database_name has to be the same in settings.py)`

## Starting Website
Create a directory using virtual environment:

`virtualenv -p python3 <dir_name>`

In directory, activate virtual environment:

`source bin/activate`

Get Django project from github:

`git clone http://github.com/ylc265/Project1`

Install Dependencies:

`pip install -r requirements.txt`

Run Migrations:

`python manage.py migrate`

Build solr schema:

`python manage.py build_solr_schema > solr-4.10.2/example/solr/collection1/conf/schema.xml`

Start the website server:

`python manage.py runserver`

Go to website:

`127.0.0.0:8000/frontpage`


