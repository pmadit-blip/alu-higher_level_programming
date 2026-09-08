#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const [userId, occ] of Object.entries(dict)) {
  if (newDict[occ] === undefined) {
    newDict[occ] = [];
  }
  newDict[occ].push(userId);
}
console.log(newDict);
