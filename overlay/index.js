async function loadData(event) {
    const res = await fetch('/getdata')

    const data = await res.json()

    render(data)
}

function render(data){
    document.getElementById('p1-points').innerText = data.p1points
    document.getElementById('p2-points').innerText = data.p2points

    document.getElementById('p1-name').innerText = data.p1name
    document.getElementById('p2-name').innerText = data.p2name

    document.getElementById('p1-charIcon').src = `./img/Stock Icons/${data.p1char}/${data.p1color}.png`
    document.getElementById('p2-charIcon').src = `./img/Stock Icons/${data.p2char}/${data.p2color}.png`

    document.getElementById('p1-port').src = `./img/Port Icons/${data.p1port}.png`
    document.getElementById('p2-port').src = `./img/Port Icons/${data.p2port}.png`

    document.getElementById('BoX').innerText = data.bo

    document.getElementById('roundName').innerText = data.round
}   

setInterval(function() {

    loadData()
  }, 2000);