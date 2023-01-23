$(document).ready(function() {
  $("#survey-form").submit(function(event) {
    event.preventDefault();
    
    const experienceInput = parseInt($("#experience").val());
    const interestInput = parseInt($("input:radio[name=interest]:checked").val());
    const trueFalseInput = parseInt($("input:radio[name=torf]:checked").val());
    const procInput = parseInt($("input:radio[name=processing]:checked").val());
    const moviesInput = parseInt($("input:radio[name=movies]:checked").val());

    if (experienceInput + interestInput + trueFalseInput + procInput + moviesInput < 7) {
      $("#rust").hide();
      $("#go").hide();
      $("#ruby").show();
    } else if (experienceInput + interestInput + trueFalseInput + procInput + moviesInput <= 7) {
      $("#rust").hide();
      $("#go").show();
      $("#ruby").hide();
    } else if (experienceInput + interestInput + trueFalseInput + procInput + moviesInput > 9) {
      $("#rust").show();
      $("#go").hide();
      $("#ruby").hide();
    }
  })
});
  