$(document).ready(() => {


    $('#input-main').submit((e) => {
        e.preventDefault()
        $.ajax({
            url: '',
            data: $(this).serialize(),
            success: (response) => {
                $('.container-posts').empty()
                $('.pagination').empty()
                response.all_posts.forEach((e) => {
                    $('.container-posts').append(`
                    <div class="card text-left fade"> 
                    <div class="card-header text-left">
                
                            <strong>Тут должны быть теги</strong>
               
                        </div>
                        <div class="card-body">
                            <p class="card-text">${e.post_text}</p>
                         </div>
                        <div class="card-footer text-muted">
                            ${e.date_pub} - кривое время
                      </div>
                
                       </div>`)
                })
            }
        })
    })

})