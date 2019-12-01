# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2018 Scifabric LTD.
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

import json
import requests
from iiif_prezi.loader import ManifestReader
from flask import current_app

from .base import BulkTaskImport, BulkImportException


class BulkTaskLocalImporter(BulkTaskImport):
    """Class to import tasks from local storage"""

    importer_id = "localUploader"

    def __init__(self, localUploaderData):
        """Init method."""
        self.question = localUploaderData['question']
        self.filePaths = localUploaderData['localPaths']
        self.image_description = localUploaderData['description']

    def tasks(self):
        """Get tasks."""
        return self._get_task_data()

    def count_tasks(self):
        """Count number of tasks."""
        return len(self.tasks())

    def _get_task_data(self):
        data = []
        print "HERE GEHTS LOS"
        print self.image_description
        for x in range(len(self.filePaths)):
            row = {
                'question': self.question,
                'url': self.filePaths[x],
                'url_m': self.filePaths[x],
                'url_b': self.filePaths[x],
                'image_description': self.image_description[x]
            }
            row_finished = dict(info=row)
            data.append(row_finished)
        return data

