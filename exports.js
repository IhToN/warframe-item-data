const customs = require('./data/customs.json').ExportCustoms;
const drones = require('./data/drones.json').ExportDrones;
const flavour = require('./data/flavour.json').ExportFlavour;
const gear = require('./data/gear.json').ExportGear;
const keys = require('./data/keys.json').ExportKeys;
const manifest = require('./data/manifest.json').Manifest;
const regions = require('./data/regions.json').ExportRegions;
const relicArcane = require('./data/relicArcane.json').ExportRelicArcane;
const resources = require('./data/resources.json').ExportResources;
const sentinels = require('./data/sentinels.json').ExportSentinels;
const upgrades = require('./data/upgrades.json').ExportUpgrades;
const warframes = require('./data/warframes.json').ExportWarframes;
const weapons = require('./data/weapons.json').ExportWeapons;

const en_US = {
    customs,
    drones,
    flavour,
    gear,
    keys,
    manifest,
    regions,
    relicArcane,
    resources,
    sentinels,
    upgrades,
    warframes,
    weapons,
};

module.exports = {
    en_US,
    customs,
    drones,
    flavour,
    gear,
    keys,
    manifest,
    regions,
    relicArcane,
    resources,
    sentinels,
    upgrades,
    warframes,
    weapons,
};
