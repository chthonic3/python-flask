// 利用li標籤來顯示不同廠區div
var container=document.querySelectorAll('#container>div')
// console.log(container)
var event_li=document.querySelectorAll('#tab>li')
// console.log(event_li)
var currentindex=0
for(var i=0;i<event_li.length;i++){
    event_li[i].num=i
    // console.log(this.num)
    event_li[i].onclick=function(){
        container[currentindex].style.display='none'
        var index_other=this.num
        container[index_other].style.display='flex'
        container[index_other].style
        currentindex=index_other
    }
}


// 依照讀入的資料分別代入指定位置
function loction(){
    // 定義機型變數
    let machineTyp=document.querySelectorAll('#machineTyp1')
    // 定義機號變數
    let machineNo=document.querySelectorAll('#machineNo1')
    // 定義廠區
    let place=document.querySelectorAll('#place1')
    // 位置
    let loc=document.querySelectorAll('#loc1')
    //let data=document.getElementById('data1')//
    //抓總數有幾筆資料
    var machineLen=machineTyp.length;
    var str ='';
    for(var i =0 ; i<machineLen ;i++){
        var machineTyptxt =machineTyp[i].innerHTML;
        var machineNotxt =machineNo[i].innerHTML;
        var placetxt=place[i].innerHTML;
        var loctxt =loc[i].innerHTML;
            let a = placetxt+"_"+loctxt+"_1"
            let b = placetxt+"_"+loctxt+"_2"
            let link =placetxt+"_"+loctxt
            let aa = document.getElementById(a).textContent = machineTyptxt
            let bb = document.getElementById(b).textContent = machineNotxt
            document.getElementById(link).addEventListener('click', function() {
                location.href = "/"+aa+"/"+bb
            }, false);
            
        }
}
loction();

