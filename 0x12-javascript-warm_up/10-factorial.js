#!/usr/bin/node

function factorial (n) {
  if (isNaN(parseInt(n))) {
    return 1;
  } else if (parseInt(n) === 0 || parseInt(n) === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const value = process.argv[2];
const result = factorial(value);
console.log(result);
