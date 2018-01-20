# Warframe Item Data

A repository of Warframe Items Data, use the latest information of Warframe game in your project.

[![npm](https://img.shields.io/npm/v/warframe-item-data.svg)](https://www.npmjs.com/package/warframe-item-data) [![npm](https://img.shields.io/npm/dt/warframe-item-data.svg)](https://www.npmjs.com/package/warframe-item-data) [![license](https://img.shields.io/github/license/IhToN/warframe-item-data.svg)](https://github.com/IhToN/warframe-item-data) [![](https://img.shields.io/github/issues-raw/IhToN/warframe-item-data.svg)](https://github.com/IhToN/warframe-item-data) [![GitHub last commit](https://img.shields.io/github/last-commit/IhToN/warframe-item-data.svg)](https://github.com/IhToN/warframe-item-data)

**Published version:**
```bash
npm i -S warframe-item-data@latest
```

**Recommended version:**
```bash
npm i -S https://github.com/IhToN/warframe-item-data.git
```

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
`itemThumbs.json` | `itemThumbs` | Relates item names with uniqueName and textureLocation
`keys.json` | `keys` | Stores any kind of key information such as Derelict or Mission keys.
`manifest.json` | `manifest` | Relates uniqueName and textureLocation
`regions.json` | `regions` | Store the information related to Solar Nodes.
`relicArcane.json` | `relicArcane` | Store relics and their drop data.
`resources.json` | `resources` | Store the resources information and their description.
`sentinels.json` | `sentinels` | Store the information of Sentinels, Kubrows and Kavats.
`upgrades.json` | `upgrades` | Store information about Warframe Auras and Weapon Stances.
`warframes.json` | `warframes` | Store information about Warframes themselves and Archwing
`weapons.json` | `weapons` | Store information about all the weapons ingame, not filtered by categories yet.
