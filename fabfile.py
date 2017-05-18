from __future__ import with_statement
from fabric.api import abort, local, task, run, local, env, cd, sudo, prefix
from fabric.colors import red, green
from contextlib import contextmanager
import os  


PROJECT_NAME = 'wramais'
WEBAPPS = '/usr/share/webapps'
PROJECT_ROOT = WEBAPPS + '/%s' % PROJECT_NAME
REPO = 'git@gitlab.cmc.pr.gov.br:desenv/wramais.git'

env.hosts = []

@task
def localhost():
	env.hosts = ['localhost']
	env.environment = 'localhost'
	env.virtualenv = '/home/alexandre.odoni/personal/python/env-chamados-cmc/'
	env.activate = '/bin/bash /home/alexandre.odoni/personal/python/env-chamados-cmc/bin/activate'

@task
def staging():
	env.hosts = ['192.168.56.101']
	env.environment = 'staging'	
	env.user = 'django'
	env.virtualenv = '/usr/share/envs/wramais'
	env.activate = 'source /usr/share/envs/wramais/bin/activate'
	env.wwwdata = 'www-data'
	env.python_location = '/usr/bin/python3.5'

@task
def production():
	env.hosts = []
	env.environment = 'production'	
	env.user = 'www-data'
	env.virtualenv = ''
	env.activate = ''

# NÃO MUDE NADA ABAIXO !!!!!!!

def clean():
	''' Limpa Python bytecode '''
	sudo('find . -name \'*.py?\' -exec rm -rf {} \;')

def chown():
	''' Seta permissões ao usuário/grupo corretos '''
	sudo('chown -R {}:{} {}'.format(env.wwwdata, env.wwwdata, PROJECT_ROOT))

def cria_webapps():
	sudo('mkdir -p {}'.format(WEBAPPS))
	sudo('chown -R {}:{} {}'.format(env.user, env.wwwdata, WEBAPPS))

def restart():
	sudo('supervisorctl reread')
	sudo('supervisorctl reload')
	sudo('service memcached restart')
	sudo('service nginx restart')

@contextmanager
def source_virtualenv():
	with prefix(env.activate):
		yield

@task
def testa_local():
	local('clear')
	result = local("./manage.py test --settings=config.settings.test")
	if result.failed:
		print(red("Algum teste falhou", bold=True))
	else:
		print(green("Todos testes passaram. Pronto para atualizar git "))

@task
def verifica():
	with cd(PROJECT_ROOT):	
		with source_virtualenv():
			run('./manage.py check')

@task
def pull_master():
	with cd(PROJECT_ROOT):
		run('git pull origin master')

@task
def install_production():
	with cd(PROJECT_ROOT):
		with source_virtualenv():
			''' Ativa o ambiente virtual '''
			run(env.activate)

			''' Instala todos os pacotes no servidor '''
			sudo('pip install -r requirements/production.txt')		


@task
def bootstrap():
	# Atualiza código para o servidor de aplicação

	# Este comando instala todos os pacotes necessários no servidor
	
	#sudo('apt-get update && apt-get install git supervisor nginx memcached libjpeg8-dev postgresql libpq-dev python-dev python-pip python-virtualenv libfreetype6-dev libncurses5-dev libxml2-dev libxslt1-dev zlib1g-dev')
	sudo('apt-get update')
	sudo('apt-get install git')
	sudo('apt-get install supervisor')
	sudo('apt-get install nginx')
	sudo('apt-get install memcached')
	sudo('apt-get install libpq-dev')
	sudo('apt-get install python-dev')
	sudo('apt-get install python3.5-dev')
	sudo('apt-get install python-pip')
	sudo('apt-get install python-virtualenv')
	sudo('apt-get install libfreetype6-dev')
	sudo('apt-get install libncurses5-dev')
	sudo('apt-get install libxml2-dev')
	sudo('apt-get install libxslt1-dev')
	sudo('apt-get install zlib1g-dev')
	sudo('apt-get install libffi-dev')
	sudo('apt-get install libsasl2-dev')
	sudo('apt-get install libldap2-dev')
	sudo('apt-get install libssl-dev')

	# Cria os diretórios e permissões necessários 
	cria_webapps()	
	run('mkdir -p {}'.format(PROJECT_ROOT))
	run('git clone {} {}'.format(REPO, PROJECT_ROOT))

	with cd(PROJECT_ROOT):
		# Atualiza servidor com última versão do master
		run('git pull origin master')

		# Cria o ambiente virtual do projeto 
		sudo('virtualenv --python={} {}'.format(env.python_location, env.virtualenv))

		with source_virtualenv():
			# Ativa o ambiente virtual 
			run(env.activate)

			# Instala todos os pacotes no servidor 
			sudo('pip install -r requirements.txt')

	# Acerta o usuário/grupo
	chown()