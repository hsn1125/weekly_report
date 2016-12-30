#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views import application

if __name__ == "__main__":
    application.run(
        host=application.config["SERVER_HOST"], 
        port=application.config["SERVER_PORT"])
	