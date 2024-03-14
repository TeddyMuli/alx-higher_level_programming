#!/usr/bin/node

function add(a, b) {
    const result = parseInt(a) + parseInt(b);
    console.log(result);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

add(arg1, arg2);
