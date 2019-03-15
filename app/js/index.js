var DRILL_BASE_URL = 'http://localhost/starWarsPortal/api/';

function getChars() {
    $.ajax({
        url : DRILL_BASE_URL+'chars',
        crossDomain: true,
        type : 'GET'
    })
    .done(function(data){
        console.log(data);
        for (i = 0; i < data.length; i++) { 
            $('#char-list').append(`<a class="click list-group-item list-group-item-action" href="#">${data[i]["name"]}</a>`);
        }
        
    })
    .fail(function(jqXHR, textStatus, msg){
        console.log(msg);
    }); 
}


function showCharDetails(name){
    $.ajax({
        url : DRILL_BASE_URL+`chars\\${name}`,
        crossDomain: true,
        type : 'GET'
    })
    .done(function(data){
        console.log(data);

        updateModal(data[0]);
       
    })
    .fail(function(jqXHR, textStatus, msg){
        console.log(msg);
    }); 
}

function updateModal(char){
    $('#charName').text(char["name"]);
    $('#charBirth').text(`${char["gender"]}, ${char["birth_year"]}`);

    // Characters 
    $('#character-list').empty()
    $('#character-list').append(`<li class="list-group-item"><span class="font-weight-bold">Eye color:</span> ${char["eye_color"]}</li>`);
    $('#character-list').append(`<li class="list-group-item"><span class="font-weight-bold">Hair color:</span> ${char["hair_color"]}</li>`);
    $('#character-list').append(`<li class="list-group-item"><span class="font-weight-bold">Height:</span> ${char["height"]}</li>`);
    $('#character-list').append(`<li class="list-group-item"><span class="font-weight-bold">Mass:</span> ${char["mass"]}</li>`);
    $('#character-list').append(`<li class="list-group-item"><span class="font-weight-bold">Skin color:</span> ${char["skin_color"]}</li>`);


    $('#charModal').modal('show');
}


$(document).ready(function(){

    //get characters name
    getChars();

    $('body').on('click', 'a.click', function() {
        showCharDetails($(this).text());
    });

});