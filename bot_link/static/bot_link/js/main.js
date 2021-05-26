$(document).ready(() => {


    $('#input-main').submit((e) => {

        e.preventDefault()
        $.ajax({
            url: '',
            data: $('#input-main').serialize(),
            success: (response) => {
                const containerPosts = $('.container-posts')
                containerPosts.empty()
                $('.pagination').empty()
                if (response.all_posts.length > 0) {
                    response.all_posts.forEach((e) => {
                        containerPosts.append(`
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
                } else {
                    containerPosts.append(`
                    <div class="alert alert-warning" role="alert">
                        There is no posts...
                    </div>`)
                }

            }
        })
    })

})