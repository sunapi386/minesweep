$(document).ready(function(){
    this.oncontextmenu = function() {
        return false;
    }
});

function redraw(minefield, board_list) {
    minefield.empty();
    for (var row = 0; row < board_list.length; row++) {
        minefield.append("<tr>");
        var cols = "";
        for(var col = 0; col < board_list[row].length; col++) {
            cols += "<td class=\"cell\" \onclick=\"play_cell(this)\" " +
                    "row=\"" + row + "\" " +
                    "col=\"" + col + "\" " +
                    "oncontextmenu=\"flag_cell(this)\">" +
                    board_list[row][col] +
                    "</td>";
        };
        minefield.append('<tr>' + cols + '</tr>');
    };
};

function newgame_handler(data) {
    console.log("newgame_handler:", data);
    var minefield = $(".field");
    var board_list = data["new_minefield"];
    redraw(minefield, board_list);
}

function updategame_handler(data) {
    console.log("updategame_handler:", data);
    var minefield = $(".field");
    var board_list = data["played_minefield"];
    redraw(minefield, board_list);
}

function flaggame_handler(data) {
    console.log("flaggame_handler:", data);
    var minefield = $(".field");
    var board_list = data["played_minefield"];
    redraw(minefield, board_list);
}

function new_game() {
    // TODO: dynamically have user choose difficulty?
    var JSONObj = {'board_size' : 10, 'num_mines' : 10};
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