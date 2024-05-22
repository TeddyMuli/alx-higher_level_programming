#!/usr/bin/node

const arg = process.argv[2];

const number = parseInt(arg);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let row = '';
  for (let j = 0; j < number; j++) {
    row += 'X';
  }
  console.log(row);
  }
}
