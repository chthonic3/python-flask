// 將所有的enddate提取出來，因為html用for迴圈所以用querySelectorAll提取
var n=document.querySelectorAll('#enddate')
//計算enddate數量
var nn=n.length
//將所有button提取
var b=document.querySelectorAll('#button')

for(var i =0 ; i<nn ;i++){
    //因為為串列，所有要用[i]做索引值，並將其內文顯示
    var nnn=n[i].innerHTML
    //當內文為'None'當下那個enddate不顯示，如果不是'None'也就是有日期就將button不顯示
    if (nnn=='None'){
        n[i].style.display='none'
    }else{
        b[i].style.display='none'
    }
}