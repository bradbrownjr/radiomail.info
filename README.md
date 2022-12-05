# About
General ham radio reference platform for Winlink and packet radio email gateways. This pulls information from online sources to provide to operators who are without Internet access.

# Requirements
- Remote operator emails the application's address with a command, application, and values in the subject; body is not required and encouraged to be left blank or as small as possible
- Applicaiton will poll for new email w/ SMTP every X minutes
- For each *new* email run the appropriate function to respond to the command contained within the subject, and mark the email read or delete it (probably cleanest to delete them upon use)
- If an application command's value isn't entered and there is no default, an error response should be provided, and the email marked for deletion
- Applications will be individual modules
	- facilitates reuse across pollers
	- each module will contain variables to populate the ``help {command}`` requests and ``Catalog`` list
- For each, log the time, sender, subject, and body of request to /var/log/radiomailinfo.log (this can be accomplished at cron.d by funneling stdout to /var/log/radiomail.log)
- Stretch: APRS gateway / APRS-IS API interface
- Stretch: A telnet, AXIP, or API interface for packet radio

# Todo
- [X] Build command list
- [X] Install Proxmox on NAS
- [X] Build VM running Linux
- [X] Identify a domain
- [X] Setup hosting of mailbox
- [X] Setup hosting of info page
- [X] Find an imap library for Python
- [X] Setup mail checker and test
- [ ] Build out general commands
- [ ] Build out applications
- [ ] Publish and market

# General commands
- Catalog / index - Lists all available applications and their commands
- Help {app} - Get info on specific applications
- About / Info - Information about this service
- Test - Provides brief response to confirm receipt, to include time of receive and time of execution
- {application} {app-command} - Execute an application and its available commands

# Applications

## Callsign
- QRZ {callsign} - Lookup name, address, QSL info
- Path {mygrid} {callsign} - Get direction and distance between your location and the remote operator

## WX
- Forecast {Today*, Tomorrow, 10-day} {zipcode, gridsquare, nearest city}
- Almanac {sunrise, sunset, moonrise, moonset, planets in view, all*}

## Satellite
- Keplers - Fresh satellite keplers table (large file)
- Passes - Next hour of all celestial passes

## DX Cluster
- Last # (def 10)

## Bandplan
Format e.g.:  ``10m basic US General
- Band (e.g.: 10m) / All (Bands)
- Basic* (no frequency allocations) / Full (with frequency allocations)
- Country {US*, CA, *etc*}
- Class {(}Technician, General, Extra, all*}

## Conditions
- none, pulls HamQSL.net report

## Location
- gridsquare {lat} {long}
- town {gridsquare}
- latlong {gridsquare}

## Nets
- On {band}
- Upcoming {band} - Next hour

## Repeaters
- Near {gridsquare} {band} {# of (10*)} - Pulls nearest repeaters

## Clubs
- Near {gridsquare, state, country}

## Wiki
- Topic {short*, full}

## Bulletins
- Category {TBD}
- Source {ARRL, WX, List}

## Book
Pulls chapters from public domain literature
- List {genre, author}
- Read {book's title} {Chapter (1*)}

## News
Top ten news stories of the day

# Installation
This project is still in the early proof-of-concept stage, and no guarantee is made of its functionality.
Config file ``config.py`` should be created within the folder with the executables (bin/)

```python
imap_servername = ""
imap_username = ""
imap_password = ""
```
