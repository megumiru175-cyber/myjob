const hour = new Date().getHours();

if(hour >=4 && hour <11){
document.getElementById('aisatu').textContent ="おはようございます。"
}else if(hour >=11 && hour<17){
    document.getElementById('aisatu').textContent ="こんにちは。"
}else{
document.getElementById('aisatu').textContent ="お疲れ様です。"
}
