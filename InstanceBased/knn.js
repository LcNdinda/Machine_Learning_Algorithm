var queryX = 3;
var queryY = 7;


var Euclidean  = function(x1, x2, y1, y2){
  var x = x2 - x1;
  var y = y2-y1;
  var z = (x*x) + (y*y);
  return Math.sqrt(z)

}


var k = 3;
var sample1X = 7;
var sample1Y = 7;
var label1 = "Bad";
var KNN1 = Euclidean(queryX, queryY, sample1X, sample1Y);
var result1 = KNN1

var sample2X = 7;
var sample2Y = 4;
var label2 = "Bad";
var KNN2 = Euclidean(queryX, queryY, sample2X, sample2Y);
var result2 = KNN2;

var sample3X = 3;
var sample3Y = 4;
var label3 = "Good";
var KNN3 = Euclidean(queryX, queryY, sample3X, sample3Y);
var result3 = KNN3

var sample4X = 1;
var sample4Y = 4;
var label4 = "Good";
var KNN4 = Euclidean(queryX, queryY, sample4X, sample4Y);
var result4 = KNN4

var data = [
  [result1, label1],
  [result2, label2],
  [result3, label3],
  [result4, label4],
]

// Sort Results in Ascending order.
var array2 = data.sort(([res1], [res2]) => res1 - res2);
var slicedArray = array2.slice(0, k);
var votes = slicedArray.reduce((acc, [_, label]) => ({
  ...acc,
  [label]: (acc[label] || 0) + 1
}), {})


let label, cc = -1;
for(const [label_, count] of Object.entries(votes)){
  if(count > cc){
    cc = count
    label = label_
  }
}
console.log(label)











// var sample1 = [7, 7, "Bad"];
// var sample2 = [7, 4, "Bad"];
// var sample3 = [3, 4, "Good"];
// var sample4 = [1, 4, "Good"];
// var queryInstance = [3, 7,];
