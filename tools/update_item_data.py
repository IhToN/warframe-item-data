#!/usr/bin/env python3
import os
import urllib.request
import json
import codecs

data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

urls = [
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportCustoms.json", "customs.json", "ExportCustoms"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportDrones.json", "drones.json", "ExportDrones"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportFlavour.json", "flavour.json", "ExportFlavour"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportGear.json", "gear.json", "ExportGear"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportKeys.json", "keys.json", "ExportKeys"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportManifest.json", "manifest.json", "Manifest"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportRelicArcane.json", "relicArcane.json",
     "ExportRelicArcane"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportResources.json", "resources.json", "ExportResources"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportSentinels.json", "sentinels.json", "ExportSentinels"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportUpgrades.json", "upgrades.json", "ExportUpgrades"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportRegions.json", "regions.json", "ExportRegions"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportWarframes.json", "warframes.json", "ExportWarframes"],
    ["http://content.warframe.com/MobileExport/Manifest/", "ExportWeapons.json", "weapons.json", "ExportWeapons"],
]

itemThumbs = []
manifest = []

for url in urls:
    with urllib.request.urlopen(url[0] + url[1]) as webURL:
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        webJSON = json.loads(data.decode(encoding), strict=False)

        with open(os.path.join(data_dir, url[2]), "w") as file:
            file.write(json.dumps(webJSON, indent=4, sort_keys=True))
            print(url[1], "file has been saved as", url[2])

        if url[3] != 'Manifest':
            for elem in webJSON[url[3]]:
                itemThumbs.append({'name': elem['name'], 'uniqueName': elem['uniqueName']})
        else:
            manifest = webJSON[url[3]]

for item in itemThumbs:
    print('Loading image for', item['name'])
    for elem in manifest:
        if elem['uniqueName'] == item['uniqueName']:
            item.update({'textureLocation': elem['textureLocation']})
            break

with open(os.path.join(data_dir, 'itemThumbs.json'), "w") as file:
    file.write(json.dumps(itemThumbs, indent=4, sort_keys=True))
    print("All item, as long as their uniqueName and their textureLocation have been saved in",
          'itemThumbs.json')

print("All JSON files have been saved.")
