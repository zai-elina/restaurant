var updateBtns= document.getElementsByClassName('update-order')

for(var i=0;i<updateBtns.length;i++)
{
    updateBtns[i].addEventListener('click', function(e){
        e.preventDefault()
        var foodId = this.dataset.food
        var action = this.dataset.action
        console.log('foodId:',foodId,'action:',action)

        console.log('USER:',user);
        if(user === 'AnonymousUser')
        {
            console.log('Не вошли в систему');
        }
        else
        {
            updateUserOrder(foodId,action);
        }

    })
}

function updateUserOrder(foodId,action,e){
    console.log('Пользователь вошёл в систему')

    var url='/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'foodId':foodId,'action':action})

    })

     .then((response) => {
         return response.json()
     })

    .then((data) =>{
        console.log('data:',data)
        location.reload()
        })
}

