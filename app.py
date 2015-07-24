# Copyright (C) 2014 Daichi Teruya (@maruuusa83)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License.
#
# This program is destributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import os
import sys
import hashlib, hmac
from flask import Flask, request
import json


### Settings ###
LISTEN_PATH   = '/hook/';
LISTEN_PORT   = 8100;
SECRET        = 'secret';

UPDATE_SCRIPT = './on-update.sh';


### Body ###
app = Flask(__name__);

@app.route(LISTEN_PATH, methods=['POST'])
def index():
	if request.method == 'POST':
		push = request.data;
		payload  = json.loads(push);

		# Prepare for verifying of "secure"
		hashdata = request.headers.get('X-Hub-Signature');
		hasher = hmac.new(SECRET, push, hashlib.sha1);
		myhashdata = 'sha1=' + str(hasher.hexdigest());

		if (hashdata == myhashdata): # Verifying "secure"
			if (payload['ref'] == 'refs/heads/master'): # on master
				os.system(UPDATE_SCRIPT + ' ' + payload['repository']['name']);
	return "ok.";

if __name__ == '__main__':
	app.run(port=LISTEN_PORT);

