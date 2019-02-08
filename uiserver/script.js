


var table = populateTable(7, 52, function (id) {
    console.log('You clicked', id)

    var td = document.getElementById(id);

    var oldIndex = "abcde".indexOf(td.className);
    var newIndex = (oldIndex + 1) % 5;

    td.className = "abcde"[newIndex];
})


function populateTable(rows, cols, cb) {

    // Classnames can't start with an integer..
    var i2classdict = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
    }

    var table = document.getElementById("table");

    var i = 0;

    for (var r = 0; r < rows; r++) {
        var tr = table.appendChild(document.createElement('tr'));

        for (var c = 0; c < cols; c++) {
            var td = tr.appendChild(document.createElement('td'))
            td.classList.add("abcde"[Math.floor(Math.random() * 5)])
            td.id = i;

            td.addEventListener('click', (function (i) {
                return function () {
                    cb(i);
                }
            })(i), false)
            i++;
        }

    }
    return table
}


function submit() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);

    xhr.onreadystatechange = function (e) {
        if (xhr.status === 200) {
            close();
            return
        }
        else {
            console.log('Failure code', xhr.status);
        }
    }

    xhr.send(html2python());

}



function html2python() {
    return "[[1,0,2], [0,3,1], [1,1,0]]"
}