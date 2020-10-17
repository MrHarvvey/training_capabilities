# reset kanału, przez bramkę esb_ca_in


#import request
from xml.dom import minidom

CIF = 4141414
import xml.etree.ElementTree as ET

tresc_zapytania = '''<?xml version="1.0" ?>
<soapenv:Envelope xmlns:ext="http://www.softax.com.pl/tmub/ext" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Header>
      <ext:request-header>
         <ref-request-id>SFX-RO-DEV::54943:1473683815289 : 2016-09-12T02:36:55</ref-request-id>
         <!--Optional:-->
         <client-info>
            <!--Optional:-->
            <session-id>SFX-RO-DEV::54943:1473683815289</session-id>
         </client-info>
         <operator-info>
            <operator-id>OPERATOR</operator-id>
            <session-id>SFX-RO-DEV::54943:1473683815289</session-id>
         </operator-info>
      </ext:request-header>
   </soapenv:Header>
   <soapenv:Body>
      <ext:customer-auth-channel-reset-request>
          <external-id for="CIF">74733327</external-id>
          <channel>WWW</channel>
      </ext:customer-auth-channel-reset-request>
   </soapenv:Body>
</soapenv:Envelope>'''

myroot = ET.fromstring(tresc_zapytania)
for child in myroot[1]:
    CIF
    monika = child[0].text
    child[0].text = CIF

print(tresc_zapytania)

for line in tresc_zapytania:
  cif = 1475484
  output_line = line
  output_line = str.replace(output_line, CIF, cif)
  print(output_line)