# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    operations = [
		migrations.RunSQL(
    		"""
    		DROP TABLE IF EXISTS v_setor;
    		DROP TABLE IF EXISTS v_pessoa;
 
    		CREATE TABLE v_setor (
    			set_id serial not null,
    			set_nome character varying(500) not null,
    			set_sigla character varying(100) not null,
    			set_id_superior integer,
    			etr_id integer not null,
    			set_ativo integer not null
    		);

			CREATE TABLE v_pessoa(
				pes_matricula serial not null,
				pes_nome character varying(500) not null,
				set_id integer not null
			);
    		"""
		),
	]