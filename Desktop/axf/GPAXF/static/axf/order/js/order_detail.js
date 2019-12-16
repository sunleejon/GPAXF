$(function () {
    console.log("支付");
    $("#alipay").click(function () {
        console.log("支付");
        var orderid = $(this).attr("orderid");
        $.getJSON('/axf/payed/', {"orderid": orderid}, function (data) {
            console.log(data);
            console.log(data["pay_url"])
            if (data["status"] === 200){
                window.open(data["pay_url"], target="_self")
            }



        })

    })
})
