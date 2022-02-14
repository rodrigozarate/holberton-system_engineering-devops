# POSTMORTEM
## Issue Summary
### duration of the outage
#### 14:34:17 (-5 GMT Bogota Lima)
#### 16:11:09 (-5 GMT Bogota Lima)
### Impact
#### Web Server down (http 500) server error
#### 100% affected
### Root cause
#### PHP verison change from 5.6 to 7.3 on hosting provider
## Timeline
### Detection
#### 14:40:03 (-5 GMT Bogota Lima)
#### Direct message complaint to support from user
### Actions taken
#### Conecction to site from web browser
##### Verification of 500 error from end
#### Conection to other sites hosted on the same hosting provider account
##### Verification of 500 error from end on some sites
#### Matching common configuration of sites down
##### Use of PHP on Backend
##### PHP Version 5.6 compatible
### Misleading investigation
#### ISP blackout on location
#### Cache clearing
### Escalated to
#### Rodrigo Zárate IT suport
### Resolution
#### Downgrade of PHP versión from 7.3 to 5.6
## Root cause and resolution
### Cause
Files connect.php consulta_aseguradoras.php consulta_servicios.php consulta_ciudades.php consulta_filales.php consulta_tarifas.php and many others contain code not compatible with php 7
function handler(Exception $e) { ... }
set_exception_handler('handler');
Changes to the handling of indirect variables, properties, and methods

| Expression | PHP 5 interpretation | PHP 7 interpretation |
| ---------- | -------------------- | -------------------- |
| Foo::$bar['baz']() | Foo::{$bar['baz']}() | (Foo::$bar)['baz']()|
#### Resolution
Use of CP to downgrade of PHP versión from 7.3 to 5.6 on the affected server

Double check of service online on support end

Contact user and double check service online on user end
## Corrective and preventative measures
### Client was informed about php changes and end of Long Term Support
### Plan of code migration was given to the client
### Hosting provider was informed about the fix requirement of PHP 5.6
