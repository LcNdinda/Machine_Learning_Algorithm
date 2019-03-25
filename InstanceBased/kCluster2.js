var medicines=[[1,1],[2,1],[4,3],[5,4]];

// Centroids
var c1 = medicines[0];
var c2 = medicines[1];

var obj=[];
// determine euclideanDistance
for(var i=0;i<medicines.length;i++){
  let temp=[];
  temp[0] = Math.pow(medicines[i][0] - c1[0], 2) + Math.pow(medicines[i][1] - c1[1], 2);
  temp[1] = Math.pow(medicines[i][0] - c2[0], 2) + Math.pow(medicines[i][1] - c2[1], 2);
  //obj[i]=[temp[0],temp[1]];
  if(temp[0]<temp[1]){
    obj[i]=[1,0];
  }else{
    obj[i]=[0,1]
  }
}

console.log(obj);
