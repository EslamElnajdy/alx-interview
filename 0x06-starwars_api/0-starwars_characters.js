#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];

const api = `https://swapi-api.alx-tools.com/api/films/${arg}`;

function fetchJson (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function getCharactersOfFilms (api) {
  try {
    const filmData = await fetchJson(api);
    return filmData.characters;
  } catch (err) {
    console.error('Error fetching film data', err);
  }
}

async function getCharacters (apiOfChar) {
  try {
    const charData = await fetchJson(apiOfChar);
    console.log(charData.name);
  } catch (err) {
    console.error('Error fetching Characters data');
  }
}

async function main () {
  const characters = await getCharactersOfFilms(api);

  if (characters) {
    for (const chr of characters) {
      await getCharacters(chr);
    }
  }
}

main();
