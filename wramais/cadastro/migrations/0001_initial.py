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
    			set_id serial primary key,
    			set_nome character varying(500) not null,
    			set_sigla character varying(100) not null,
    			set_id_superior integer,
    			set_ativo boolean not null, 
                set_tipo character varying(1)
    		);

			CREATE TABLE v_pessoa(
				pes_matricula serial primary key,
				pes_nome character varying(500) not null,
				set_id integer not null
			);

    		"""
		),
	]