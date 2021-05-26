$(document).ready(() => {


    $('#input-main').submit((e) => {
        e.preventDefault()
        $.ajax({
            url: '',
            data: $('#input-main').serialize(),
            success: (response) => {
                console.log(response)
                $('.container-posts').empty()
                $('.pagination').empty()
                response.all_posts.forEach((e) => {
                    $('.container-posts').append(`
                    <div class="card text-left fade"> 
                    <div class="card-header text-left">
                
                            <strong>${e.post_text}</strong>
               
                        </div>
                        <div class="card-body">
                            <p class="card-text">${e.post_text}</p>
                         </div>
                        <div class="card-footer text-muted">
                            ${e.date_pub}
                      </div>
                
                       </div>`)
                })
            }
        })
    })

})