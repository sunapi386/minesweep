
function newgame(data) {
    console.log("newgame:", data);
}

function update_game(data) {
    console.log("update_game:", data);
}

function new_game() {
    var JSONObj = {'mapsize':10};
    var targeturl = '/api/newgame.json'
    ajax_post(JSONObj, targeturl, newgame);
}

function play_cell() {
    var JSONObj = {'mapsize':10};
    var targeturl = '/api/play.json'
    ajax_post(JSONObj, targeturl, update_game);
}

function ajax_post(JSONObj, targeturl, callbackfn) {
    console.log(JSON.stringify(JSONObj));
    $.ajax({
        contentType: 'application/json; charset=utf-8',
        type: 'POST',
        url: targeturl,
        data: JSON.stringify(JSONObj),
    }).done(function(data){
        console.log("ajax_post done", data);
        callbackfn(data);
    });
}