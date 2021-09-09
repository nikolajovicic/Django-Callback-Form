window.onload = function(){
    //alert('hello from js!')

    document.getElementById("id_callback_date").onchange = function() {checkWeekDay()};

    function checkWeekDay() { 
        var d = new Date();
        d = document.getElementById("id_callback_date").valueAsDate;
        var n = d.getDay();

        if (n == 0){
            alert('Sunday is not allowed.');
            document.getElementById("id_callback_date").value = null;
        }
        else if (n == 6){
            hideOptions();
        }
        else{
            showOptions();
        }
    }

    function hideOptions(){
        for (i = 9; i <=24; i++){
            var x = document.getElementById("id_callback_time").options[i].hidden = true;
        }
    }
    
    function showOptions(){
        for (i = 9; i <=24; i++){
            var x = document.getElementById("id_callback_time").options[i].hidden = false;
        }
    }
}
