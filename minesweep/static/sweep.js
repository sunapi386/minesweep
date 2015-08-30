$(document).ready(function(){
    this.oncontextmenu = function() {
        return false;
    }
});

function newgame_handler(data) {
    console.log("newgame_handler:", data);
    var minefield = $(".field");
    minefield.empty();
    console.log(data["new_minefield"]);
    for (var row = 0; row < data["new_minefield"].length; row++) {
        minefield.append("<tr>");
        var cols = "";
        for(var col = 0; col < data["new_minefield"][row].length; col++) {
            cols += "<td class=\"cell\" \onclick=\"play_cell(this)\" " +
                    "row=\"" + row + "\" " +
                    "col=\"" + col + "\" " +
                    "oncontextmenu=\"flag_cell(this)\">" +
                    data["new_minefield"][row][col] +
                    "</td>";
        };
        minefield.append('<tr>' + cols + '</tr>');
    };
}

function updategame_handler(data) {
    console.log("updategame_handler:", data);
}

function flaggame_handler(data) {
    console.log("flaggame_handler:", data);
}

function new_game() {
    var JSONObj = {};
    var targeturl = '/api/newgame.json'
    ajax_post(JSONObj, targeturl, newgame_handler);
}

function play_cell(attrs) {
    var row = attrs.getAttribute("row");
    var col = attrs.getAttribute("col");
    var JSONObj = {'row':row, 'col':col};
    var targeturl = '/api/play.json'
    ajax_post(JSONObj, targeturl, updategame_handler);
}

function flag_cell(attrs) {
    var row = attrs.getAttribute("row");
    var col = attrs.getAttribute("col");
    var JSONObj = {'row':row, 'col':col};
    var targeturl = '/api/flag.json'
    ajax_post(JSONObj, targeturl, flaggame_handler);
}

function ajax_post(JSONObj, targeturl, callbackfn) {
    console.log("ajax_post:", JSON.stringify(JSONObj));
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