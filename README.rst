ESTE PROJETO FOI ARQUIVADO EM DETRIMENTO DESTE NOVO AQUI: https://github.com/CMCuritiba/ramais


Aplicação Ramais CMC
####################

Aplicação Django para controle de ramais Câmara Municipal de Curitiba



.. section-numbering::


ATENÇÃO
=======
Esta versão já possui variáveis de ambiente configuradas para o Decouple.
Por motivos de segurança, o arquivo .env com estas variáveis não está versionado, portanto favor requisitar o mesmo com os responsáveis.

Comandos Django úteis
=====================

Instalar componentes via bower
------------------------------

.. code-block:: bash

    $ python manage.py bower_install


Gerar e comprimir arquivos css e js
-----------------------------------

.. code-block:: bash

    $ python manage.py collectstatic


Pacotes a instalar no servidor (deploy)
=======================================

For pip/virtualenv python-pip , python-virtualenv
For PostgreSQL postgresql , postgresql-contrib , libpq-dev , python-dev    


:License: MIT
