# Warframe Item Data

[![Supported by Warframe Community Developers](https://raw.githubusercontent.com/WFCD/banner/master/banner.png)](https://github.com/WFCD "Supported by Warframe Community Developers")

A repository of Warframe data for use with warframe-worldstate-parser

## Usage

```javascript
var itemData = require('warframe-item-data');
var warframes = itemData.warframes;

var firstOne = warframes[0];
var wfName = firstOne.name;
var wfUniqueName = firstOne.uniqueName;
```

## Available data and formatting

JSON | Data Accessor | Description
--- |--- | --- 
`customs.json` | `customs` | Stores customization items as skins, syndanas, sigils...
`drones.json` | `drones` | Stores extractos information.
`flavour.json` | `flavour` | Stores colours, glyphs and animation sets.
`gear.json` | `gear` | Stores gear items information.
`keys.json` | `keys` | Stores any kind of key information such as Derelict or Mission keys.
`manifest.json` | `manifest` | Relates uniqueName and textureLocation
`regions.json` | `regions` | Store the information related to Solar Nodes.
`relicArcane.json` | `relicArcane` | Store relics and their drop data.
`resources.json` | `resources` | Store the resources information and their description.
`sentinels.json` | `sentinels` | Store the information of Sentinels, Kubrows and Kavats.
`upgrades.json` | `upgrades` | Store information about Warframe Auras and Weapon Stances.
`warframes.json` | `warframes` | Store information about Warframes themselves and Archwing
`weapons.json` | `weapons` | Store information about all the weapons ingame, not filtered by categories yet.
