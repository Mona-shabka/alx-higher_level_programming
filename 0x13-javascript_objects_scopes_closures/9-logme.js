#!/usr/bin/node
let m_count = 0;
exports.logMe = function (item) { console.log(`${m_count++}: ${item}`); };
