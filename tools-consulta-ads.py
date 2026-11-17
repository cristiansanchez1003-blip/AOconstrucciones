"""Consulta de solo lectura a Google Ads (GAQL) para AO Construcciones.
Respaldo para cuando el conector google-ads no esta disponible. No modifica nada.
Uso (con el Python del conector):
  "C:/Users/cristian1/.codex/mcp/google-ads-mcp/.venv/Scripts/python.exe" -I -X utf8 tools-consulta-ads.py consultas.txt
En consultas.txt: primera linea = nombre, luego la consulta GAQL; separar consultas con una linea "---".
"""
import json, os, sys

os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS",
    r"C:\Users\cristian1\.codex\credentials\google-ecosystem\authorized-user.json")
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", "espiritu-digital")

import google.auth
from google.ads.googleads.client import GoogleAdsClient
from google.protobuf.json_format import MessageToDict

CUSTOMER = "3656571293"
creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/adwords"])
client = GoogleAdsClient(credentials=creds, use_proto_plus=True, login_customer_id="5347879097")
svc = client.get_service("GoogleAdsService")

text = open(sys.argv[1], encoding="utf-8").read()
for q in [x.strip() for x in text.split("\n---\n") if x.strip()]:
    name, _, query = q.partition("\n")
    rows = []
    try:
        for batch in svc.search_stream(customer_id=CUSTOMER, query=query):
            for r in batch.results:
                rows.append(MessageToDict(type(r).pb(r), preserving_proto_field_name=True))
    except Exception as e:
        msg = getattr(e, "failure", None)
        print(f"### {name}: ERROR {msg.errors[0].message if msg else e}")
        continue
    print(f"### {name} ({len(rows)} filas)")
    for r in rows:
        print(json.dumps(r, ensure_ascii=False))
