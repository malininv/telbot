$(document).ready(() => {


    $('#input-main').submit((e) => {

        e.preventDefault()
        $.ajax({
            url: '',
            data: $('#input-main').serialize(),
            success: (response) => {
                $('.container-posts').html(response)
            }
        })
    })

})