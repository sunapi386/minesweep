
function newgame_handler(data) {
    console.log("newgame_handler:", data);
}

function updategame_handler(data) {
    console.log("updategame_handler:", data);
}

function new_game() {
    var JSONObj = {'mapsize':10};
    var targeturl = '/api/newgame.json'
    ajax_post(JSONObj, targeturl, newgame_handler);
}

function play_cell() {
    var JSONObj = {'mapsize':10};
    var targeturl = '/api/play.json'
    ajax_post(JSONObj, targeturl, updategame_handler);
}

function ajax_post(JSONObj, targeturl, callbackfn) {
    // console.log(JSON.stringify(JSONObj));
    $.ajax({
        contentType: 'application/json; charset=utf-8',
        type: 'POST',
        url: targeturl,
        data: JSON.stringify(JSONObj),
    }).done(function(data){
        // console.log("ajax_post done", data);
        callbackfn(data);
    });
}