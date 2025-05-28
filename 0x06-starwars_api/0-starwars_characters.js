#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
        if (error) {
                console.error(error);
                return;
        }

        const filmData = JSON.parse(body);
        const characters = filmData.characters;

        const printCharacter = (index) => {
                if (index >= characters.length) return;

                request(characters[index], (err, res, charBody) => {
                        if (!err) {
                                const character = JSON.parse(charBody);
                                console.log(character.name);
                                printCharacter(index + 1);
                        }
                });
        };

        printCharacter(0);
});
