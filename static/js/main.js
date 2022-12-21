window.addEventListener("DOMContentLoaded", ()=>{
    let button = document.querySelector("#button-excel");

    button.addEventListener("click", e => {
    let table = document.querySelector("#loptable");
    TableToExcel.convert(table);
});
})

