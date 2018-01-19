#!/usr/bin/env python3
import os
import urllib.request
import json

data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

urls = [
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportWeapons.json", "weapons.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportUpgrades.json", "upgrades.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportManifest.json", "manifest.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportSentinels.json", "sentinels.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportResources.json", "resources.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportDrones.json", "drones.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportCustoms.json", "customs.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportFlavour.json", "flavour.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportKeys.json", "keys.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportGear.json", "gear.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportRelicArcane.json", "relicArcane.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportRegions.json", "regions.json"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportWarframes.json", "warframes.json"]
]

for url in urls:
    with urllib.request.urlopen(url[0] + url[1]) as webURL:
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        webJSON = json.loads(data.decode(encoding), strict=False)

        with open(os.path.join(data_dir, url[2]), "w") as file:
            file.write(json.dumps(webJSON, indent=4, sort_keys=True))
            print(url[1], "file has been saved as", url[2])

print("All JSON files have been saved.")
