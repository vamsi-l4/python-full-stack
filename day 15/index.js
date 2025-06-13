const todo=[]
const displayTodo = ()=>{
    const todoContainer=document.getElementById('todo-container');
    todoContainer.innerHTML="";
    todo.forEach((element,index) => {
        const todoItem=document.createElement('div');
        todoItem.innerText=`${index+1}.${element}`;
        todoItem.classList.add("item")
        if (element.status==="done"){
            todoItem.classList.add("done");
            todoItem.classList.remove("pending");
        }else {
            todoItem.classList.add("pending");
            todoItem.classList.remove("done");
        }
        todoItem.innerHTML =`
         <p>${index + 1}. ${element}</p>
         <div class ="item pending">
         <select id="id${index}">
            <option>value="Pending"</option>
            <option>value="done"</option>
        </select>
        </div>`
        todoContainer.appendChild(todoItem);

        document.getElementById(`id${index}`).addEventListener("change" , (e)=>{
            if (!todoItem.classList.contains("done")){
                todoItem.classList.add("done");
                todoItem.classList.remove("pending");
            }else {
                todoItem.classList.add("pending");
                todoItem.classList.remove("done");
            }
        })
    }) ;       
   
}
function updatestatus(selectElement){
    const parent=selectElement.parentElement;
    parent.classList.remove('done','pending');
    const status=selectElement.value;
    parent.classList.add(newStatus);
    if(todo[itemIndex]){
        todo[itemIndex].status= newStatus;
    }
}

const button = document.getElementById("Add")
button.addEventListener("click", ()=>{
    const input= document.getElementById("todoname");
    if (input.value.trim() !==""){
    todo.push(input.value);
    input.value="";
    displayTodo();
    }
});