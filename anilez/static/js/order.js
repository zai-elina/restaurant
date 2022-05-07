var updateBtns= document.getElementsByClassName('update-order')

for(var i=0;i<updateBtns.length;i++)
{
    updateBtns[i].addEventListener('click', function(e){
        e.preventDefault()
        var foodId = this.dataset.food
        var action = this.dataset.action
        console.log('foodId:',foodId,'action:',action)

        console.log('USER:',user);

    })
}