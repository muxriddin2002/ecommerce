let timer = document.querySelectorAll('.li-countdown')

for (let i of timer) {
    let end_time =new Date(i.dataset.endtime)

    let day = i.children[0],
        hour = i.children[1],
        minut = i.children[2],
        second = i.children[3]

    updateTime(end_time,day,hour,minut,second)





}


function updateTime(end_time,day,hour,minut,second) {

    setInterval(function (){
        let timeNow = new Date()
        let time = end_time - timeNow

         let d = Math.floor(time/1000/60/60/24),
            h = Math.floor(time/1000/60/60)%24,
            m = Math.floor(time/1000/60)%60,
            s = Math.floor(time/1000)%60

        day.innerHTML = d < 10 ? '0'+d + '<span>day:</span>': d + '<span>day:</span>'
        hour.innerHTML = h < 10 ? '0'+h + '<span>hour:</span>': h + '<span>hour:</span>'
        minut.innerHTML = m <10 ? '0'+m + '<span>min:</span>': m + '<span>min:</span>'
        second.innerHTML = s < 10 ? '0'+s + '<span>sec:</span>': s + '<span>sec:</span>'

    },1000)
}


