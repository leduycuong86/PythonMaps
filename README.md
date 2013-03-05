Installation
===================
Follow the below two steps to get the server up and running :).


Submodule Config
----------------
1. Clone repo with above urls.
2. Clone and sync submodles
	1. Setup: `git submodule init`
	2. Sync: `git submodule update`


Webserver Config
----------------
1. Create your virtual environment: ```virtualenv --distribute venv```
2. Source your environment: ```source venv/bin/activate```
3. Install python requirements: ```pip install -r requirements.txt```
4. Install Heroku Toolbelt:
	- Ubuntu: ```wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh```
	- MacOSX: [https://toolbelt.heroku.com/download/osx](https://toolbelt.heroku.com/download/osx)
	- Windows: good luck…
5. Get GoogleMaps API key ([Getting your key](https://developers.google.com/maps/documentation/javascript/tutorial#api_key))
6. Insert into a new file called `.env` the following: `GOOGLE_MAPS_API_KEY='<YOUR API KEY>'` where `'<YOUR API KEY>'` is your API key within single quotes
5. Execute foreman: ```foreman start```
6. Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the mapping server.

Copyright
========

Copyright (c) 2013 Wyatt Johnson <wyatt@wyattjohnson.ca>

Permission to use, copy, modify, and distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.