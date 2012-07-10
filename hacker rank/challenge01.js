function getCandies(n){
    console.clear();
    payload = {move: n%6, remote: 'true'};

    url = 'http://www.hackerrank.com/splash/challenge.json';
    tt = jQuery.ajax({
      type: "PUT",
      url: url,
      data: payload,
      success: function(response, textStatus, jqXHR){
                value = jqXHR.responseText;
                value = value.substring(value.search("current") + 9);
                value = value.substring(0, value.search(","));
                current = parseInt(value);
                if(current>0){
                    t = getCandies(current);
                } else{
                    console.log(jqXHR.responseText);
                }
            }
    });
}


function challenge(cc){
  url = 'http://www.hackerrank.com/splash/challenge.json';
  payload = {n: cc, remote: 'true'};

  tt = jQuery.ajax({
    type: "POST",
    url: url,
    data: payload,
    success: function(response, textStatus, jqXHR){
              // log a message to the console
              value = jqXHR.responseText;
              value = value.substring(value.search("current") + 9);
              value = value.substring(0, value.search(","));
              current = parseInt(value);
              t = getCandies(current);
          }
  });
}




for(i=2100; i< 2400; i++)
    if(i%6 !== 0)
        challenge(i);
