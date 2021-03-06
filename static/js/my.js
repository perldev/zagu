function back(){
      window.history.back();
}
function change_img(Path){
      var image = $("#big_image");
      image.fadeOut('slow', function () {
                image.attr('src', Path );
                image.fadeIn('slow');
                image.attr("data-zoom-image",Path);
                var ez =   $('#big_image').data('elevateZoom');     
                ez.swaptheimage(Path, Path); 
      });
      
          
    
    
}

function deleteCookie(name) {
  setCookie(name, "", { expires: -1 })
}


function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, options) {
  options = options || {};

  var expires = options.expires;

  if (typeof expires == "number" && expires) {
    var d = new Date();
    d.setTime(d.getTime() + expires*1000);
    expires = options.expires = d;
  }
  if (expires && expires.toUTCString) {

    options.expires = expires.toUTCString();
  }

  value = encodeURIComponent(value);

  var updatedCookie = name + "=" + value;
  for(var propName in options) {
    updatedCookie += "; " + propName;
    var propValue = options[propName];   
    if (propValue !== true) {
      updatedCookie += "=" + propValue;
     }
  }
 
  document.cookie = updatedCookie;

}




var my_gallery = {
  change : function(id){
      var newsrc = $("#big_image_"+id).attr("src");
      var title = $("#title_"+id).html();
      var desc = $("#desc_"+id).html();
      $("#gallery_thumb_"+ my_gallery.current_project).removeClass("bordered");
      my_gallery.current_project = id;
      $("#gallery_thumb_"+ my_gallery.current_project).addClass("bordered");
      $("#project_title").html(title);
      $("#project_desc").html(desc);
      var image = $("#project_img");
      
      image.fadeOut('fast', function () {
		$(this).attr('src', newsrc );
                $(this).attr("data-zoom-image",newsrc);
		image.fadeIn('fast');
      });
      
      
      
      
    
  },
  images_identifies:[],
  max_left: -300,
  current:0,
  current_project:0 ,
  step:-100,
  turn_left_img:function(){
           
           var index = my_gallery.images_identifies.indexOf(my_gallery.current_project);
           if(index==0){
                 return ;
           }
           my_gallery.change( my_gallery.images_identifies[index - 1] );
//            my_gallery.turn_left();
          
  },
  turn_right_img:function(){
           var index = my_gallery.images_identifies.indexOf(my_gallery.current_project);
           if(index == (my_gallery.images_identifies.length-1) ) {
                 return ;
           }
           my_gallery.change( my_gallery.images_identifies[index + 1] );
//            my_gallery.turn_right();
  },
  turn_left :function(){
    if(my_gallery.current<0){
	my_gallery.current = my_gallery.current - my_gallery.step;
        $("#gallery_lenta").animate({"margin-left":  my_gallery.current + "px" },300);

      
    }
    
  },
  turn_right:function(){
    var max_right = (my_gallery.images_identifies.length+2)*my_gallery.step;  
    console.log(max_right);
    console.log(my_gallery.current);
    console.log("================");

    if(my_gallery.current > max_right){
	my_gallery.current = my_gallery.current + my_gallery.step;
        $("#gallery_lenta").animate({"margin-left":  my_gallery.current + "px" },300);
      
    }
    
    
  }
  
}

var slider = {
  current:0,
  current_index:0,
  current_id:"",
  direction:1,
  gallery_count:0,
  image_list:null,
  
  turn_left :function(){
    if(slider.current>=1){
        slider.current-=1;
        slider.set_current_image(slider.current);
    }
    
  },
  
  turn_right:function(){
    if(slider.current<=(slider.gallery_count-1)){
        slider.current+=1;
        slider.set_current_image(slider.current);
    }
    
    
  },
  set_current_image:function(Index){
      var info  = slider.list[Index];
      slider.current_index = Index;
      $("#project_title").html(info["title"]);
      $("#project_desc").html(info["desc"]);
      var image = $("#slider_image");
      var newsrc = info["path"];    
      image.fadeOut('fast', function () {
                image.css({"background-image":"url("+newsrc+")"});
                image.fadeIn('slow');
      });
      slider.current = Index;
  },
  next:function(){ // in straight direction
        var NewIndex = slider.current_index + 1;
        if(NewIndex< slider.gallery_count ){
              slider.set_current_image(NewIndex);

                  
              setTimeout(function(){ 
                            slider.next() 
                      }, slider.TimeOut);
              
        }else{
              slider.back();
              return ;
        }
        
  },
  back:function(){ //in back direction
        var NewIndex = slider.current_index - 1;
        if(NewIndex >= 0 ){
              slider.set_current_image(NewIndex);
              setTimeout(function(){ 
                            slider.back() 
                      }, slider.TimeOut);
              
        }else{
              
              slider.next();
              return ;
        }          
    
  },
  init:function(array, TimeOut){
          slider.list = array;
          setTimeout(function(){ 
                            slider.next() 
                      }, TimeOut);
          slider.set_current_image(0);
          slider.TimeOut = TimeOut;
          slider.gallery_count = array.length;          
  }
  
}
//0979185401
var Audio = {
 
  start_audio:function(){
      var AList = document.getElementById("audio_obj");
      Audio.controller = AList;
      console.log("initilize " );
  
    
  },
  loaded : function(){
      console.log("initilize " + Audio.is_loaded );
      if(Audio.is_loaded) 
	  return;
      
      var CurrentTrack = getCookie("CurrentTrack");
      var IsPlay = getCookie("CurrentStop");
      var CurrentPos = getCookie("CurrentPos");
      Audio.current_time = -1;
      console.log(" is play " + IsPlay );
      if(IsPlay == 0){
	  Audio.current_time = CurrentPos;
	  Audio.controller.currentTime = CurrentPos;
	  console.log("fetch params but not  play " );
	  
      }else if(IsPlay == 1){

	Audio.current_time = CurrentPos;
	Audio.controller.currentTime = CurrentPos;
        console.log("restart play " + CurrentPos );

	Audio.controller.play();
	
      }else if(IsPlay == undefined){
	Audio.controller.play();
	console.log("start play " );
      }
      Audio.is_loaded = 1;
    
  },
  start_interval_timer:function(){
    var Timer =   setInterval(function(){
		      Audio.current_time = Audio.controller.currentTime;	  
		      console.log("save current time "  + Audio.current_time );
		    }, 500);
    Audio.interval_timer = Timer;
    var Timer1 =   setInterval(function(){
		        setCookie("CurrentPos", Audio.current_time, {expires:3600*72, path:"/"});
    		         console.log("write current time "  + Audio.current_time );

		    }, 2000);
    Audio.interval_timer_write = Timer1;
    
    
  },
  clear_interval_timer:function(){
    if(Audio.interval_timer_write)
      clearInterval(Audio.interval_timer_write);
    
    if(Audio.interval_timer)
      clearInterval(Audio.interval_timer);
    
    Audio.interval_timer_write = null;
    Audio.interval_timer = null;
    
  },
  audio_play: function(){
        console.log(" start "  + Audio.current_time );
        setCookie("CurrentStop", 1, {expires:3600*72, path:"/"});
        Audio.is_play = 1;
        Audio.start_interval_timer();
    
  },
  audio_stop: function(){
        console.log(" stop "  + Audio.current_time );

	setCookie("CurrentStop", 0,{expires:3600*72, path:"/"});
	Audio.clear_interval_timer();
	Audio.is_play = 0;
  },
  interval_timer: null,
  interval_timer_write: null,
  current_time: 0,
  is_play: 0,
  is_loaded:0
  
};








