$(document).ready(() => {


    $('#input-main').submit((e) => {
        e.preventDefault()
        const getReq = $('#input-main').serialize()
        console.log(getReq)
        $.ajax({
            url: '',
            data: getReq,
            success: (response) => {
                $('.container-posts').html(response)
            }
        })

        history.replaceState(null, null, `?${getReq}`);
    })

})