#!/usr/bin/env python3
import os
import urllib.request
import json

data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

export_full_url = False

mainUrl = "http://content.warframe.com/MobileExport/"

urls = [
    [mainUrl + "Manifest/", "ExportCustoms.json", "customs.json", "ExportCustoms"],
    [mainUrl + "Manifest/", "ExportDrones.json", "drones.json", "ExportDrones"],
    [mainUrl + "Manifest/", "ExportFlavour.json", "flavour.json", "ExportFlavour"],
    [mainUrl + "Manifest/", "ExportGear.json", "gear.json", "ExportGear"],
    [mainUrl + "Manifest/", "ExportKeys.json", "keys.json", "ExportKeys"],
    [mainUrl + "Manifest/", "ExportManifest.json", "manifest.json", "Manifest"],
    [mainUrl + "Manifest/", "ExportRelicArcane.json", "relicArcane.json", "ExportRelicArcane"],
    [mainUrl + "Manifest/", "ExportResources.json", "resources.json", "ExportResources"],
    [mainUrl + "Manifest/", "ExportSentinels.json", "sentinels.json", "ExportSentinels"],
    [mainUrl + "Manifest/", "ExportUpgrades.json", "upgrades.json", "ExportUpgrades"],
    [mainUrl + "Manifest/", "ExportRegions.json", "regions.json", "ExportRegions"],
    [mainUrl + "Manifest/", "ExportWarframes.json", "warframes.json", "ExportWarframes"],
    [mainUrl + "Manifest/", "ExportWeapons.json", "weapons.json", "ExportWeapons"],
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
                print(elem)
                itemThumbs.append({'name': elem['name'], 'uniqueName': elem['uniqueName']})
                if 'description' in elem:
                    itemThumbs[-1].update({'description': elem['description']})
        else:
            manifest = webJSON[url[3]]

for item in itemThumbs:
    print('Loading image for', item['name'])
    for elem in manifest:
        if elem['uniqueName'] == item['uniqueName']:
            texture = elem['textureLocation'].replace('\\', '/')
            if export_full_url:
                item.update({'textureLocation': mainUrl + texture})
            else:
                item.update({'textureLocation': texture})
            break

with open(os.path.join(data_dir, 'itemThumbs.json'), "w") as file:
    file.write(json.dumps(itemThumbs, indent=4, sort_keys=True))
    print("All item, as long as their uniqueName and their textureLocation have been saved in",
          'itemThumbs.json')

print("All JSON files have been saved.")
