function Medicine(weightIndex, ph){
  this.weightIndex = weightIndex;
  this.ph = ph;

}

var euclideanDistance = function(x1, y1, x2, y2){
  var x = x2 - x1;
  var y = y2-y1;
  var z = (x*x) + (y*y);
  return Math.sqrt(z);
}

var medicineA = new Medicine(1,1);
var medicineB = new Medicine(2,1);
var medicineC = new Medicine(4,3);
var medicineD = new Medicine(5,4);

var K = 2;
var c1 = medicineA;
var c2 = medicineB;
