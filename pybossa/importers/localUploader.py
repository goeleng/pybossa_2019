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
        current_app.logger.info(localUploaderData)
        self.question = localUploaderData['question']
        self.filePaths = localUploaderData['localPaths']

    def tasks(self):
        """Get tasks."""
        return self._get_task_data()

    def count_tasks(self):
        """Count number of tasks."""
        return len(self.tasks())

    def _get_task_data(self):
        data = []
        for path in self.filePaths:
            row = {
                'question': self.question,
                'url': path,
                'url_m': path,
                'url_b': path
            }
            row_finished = dict(info=row)
            data.append(row_finished)
        return data

