$(' #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 3,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 6,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 7,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('#slider1').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 0,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 2,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }



})

$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    console.log(id)
    let eml = this.parentNode.children[2]

    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            console.log(data)
            console.log("success")
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.totalamount

        }
    })

})
$('.minus-cart').click(function() {
    let id = $(this).attr("pid").toString();
    let eml = this.parentNode.children[2]

    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.totalamount

        }
    })

})

$('#remove-cart').click(function() {
    let id = $(this).attr("pid").toString();
    let eml = this
    console.log("remove");
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function(data) {
            console.log("Delete");
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()



        }
    })

})