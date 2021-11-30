#!/usr/local/bin/node

console.log("Content-type: text/html\n\n")
console.log("<h3>Hello, CGI form Node.js Script</h3>")

const fac = n => n < 2 ? 1 : n * fac(n - 1)

console.log(fac(10))