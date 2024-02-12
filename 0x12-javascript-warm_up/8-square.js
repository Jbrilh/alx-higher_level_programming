#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const size = Number(process.argv[2]);

  for (let i = 0; i < size; i++) {
	  let row = '';
	  for (let j = 0; j < size; j++) {
		row += 'X';
	  }
	  console.log(row);
  }
}
