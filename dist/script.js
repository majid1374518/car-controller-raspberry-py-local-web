$(function(){
  var flag=0;
  
  $('.share').on('click',function(){
   if(flag == 0)
    {
      $(this).siblings('.one').animate({
      top:'160px',
      left:'50%',
    },200);
    
     $(this).siblings('.two').delay(200).animate({
      top:'500px',
      left:'30%'
    },200);
    
     $(this).siblings('.three').delay(300).animate({
      top:'500px',
      left:'70%'
    },200);

     $(this).siblings('.four').delay(300).animate({
      top:'840px',
      left:'50%'
    },200);
              
    $('.one i,.two i, .three i, .four i').delay(500).fadeIn(200);  
      flag = 1;
    }
    
    
  else{
    $('.one, .two, .three, .four').animate({
        top:'500px',
        left:'50%'
      },200);
      
  $('.one i,.two i, .three i, .four i').delay(500).fadeOut(200);
      flag = 0;
    }
  });
});