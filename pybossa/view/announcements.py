# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2017 Scifabric LTD.
#
# PYBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PYBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PYBOSSA.  If not, see <http://www.gnu.org/licenses/>.
"""Announcements view for PYBOSSA."""
from flask import Blueprint, current_app
from flask import render_template
from flask_login import login_required, current_user
from pybossa.cache import users as cached_users
from pybossa.util import handle_content_type
from pybossa.util import admin_required
from pybossa.core import announcement_repo


blueprint = Blueprint('announcements', __name__)

@blueprint.route('/')
@login_required
@admin_required
def show_announcements():
    """Show all announcements"""
    announcements = announcement_repo.get_all_announcements()
    response = dict(template="",
                    announcements=announcements)
    return handle_content_type(response)
