function getValue(e){
form.screen.value += e.value
}

function ClearC(){
    form.screen.value= null;
}

function ev(){
    form.screen.value= eval(form.screen.value);
}