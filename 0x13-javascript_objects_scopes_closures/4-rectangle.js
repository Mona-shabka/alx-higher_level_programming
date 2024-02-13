#!/usr/bin/node
module.exports = class Rectangle {
  constructor (x, y) {
    if (x > 0 && y > 0) { [this.width, this.height] = [x, y]; }
  }

  print () {
    for (let m = 0; m < this.height; m++) console.log('X'.repeat(this.width));
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
