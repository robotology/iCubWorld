






// Scrollspy
var lastId;
var topMenu = $("#navigator nav");
var topMenuHeight = topMenu.outerHeight()+15;
// All list items
var menuItems = topMenu.find("a");

var headerHeight = 1.5*$('header').height();

var landing_page = document.getElementById('background');
var header = document.getElementsByTagName('header')[0];

var min_alpha_landing = 0.3;
var max_alpha_landing = 1.0;
var min_alpha_header = 0.01;
var max_alpha_header = 1.0;

changeAlpha(landing_page,0,min_alpha_landing,max_alpha_landing);

changeAlpha(header,0,min_alpha_header,max_alpha_header);


// Anchors corresponding to menu items
var scrollItems = menuItems.map(function(){
  var item = $($(this).attr("href"));
  if (item.length) { return item; }
});

// add the brand button
menuItems.push($('#brand')[0]);

// Bind click handler to menu items
// so we can get a fancy scroll animation
menuItems.click(function(e){
    var href = $(this).attr("href");
    var offsetTop = href === "#" ? 0 : $('main').scrollTop() + $(href).offset().top;
    
    if(href=="#acquisition")
        offsetTop-=headerHeight;
    
  $('main').stop().animate({ 
      scrollTop: offsetTop
  }, 300);
//  e.preventDefault();
});

// Bind to scroll
$('main').scroll(function(){
   // Get container scroll position
//   var fromTop = $('html').scrollTop()+topMenuHeight;
   var fromTop = topMenuHeight+headerHeight;
   
   // Get id of current scroll item
   var cur = scrollItems.map(function(){
     if ($(this).offset().top < fromTop)
       return this;
   });
   // Get the id of the current element
   cur = cur[cur.length-1];
   var id = cur && cur.length ? cur[0].id : "";
   var id = cur ? cur[0].id : "";
   
   if (lastId !== id) {
       lastId = id;
       // Set/remove active class
       menuItems
         .removeClass("active").filter("[href='#"+id+"']").addClass("active");
   }
    
    
    var main_height = $('main').scrollTop();
    var landing_height = $('#background').height();
    
    var alpha_t = main_height/(landing_height-topMenu.height())
    
    alpha_t = alpha_t <= 1.0? alpha_t : 1.0; 
    
changeAlpha(landing_page,alpha_t,min_alpha_landing,max_alpha_landing);
    changeAlpha(header,alpha_t,min_alpha_header,max_alpha_header);
    
    if(alpha_t>=0.1)
        header.classList.add('shadow');
    else
        header.classList.remove('shadow');
                
});





// alpha change 




function changeAlpha(object,alpha_t,min_alpha,max_alpha) {
    
    alpha = min_alpha + alpha_t*(max_alpha-min_alpha);
    
    var current_color = getComputedStyle(object).getPropertyValue("background-color");
//            var match = /rgba?\((\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(,\s*\d+[\.\d+]*)*\)/g.exec(current_color);
    
            var match = current_color.replace(/[^\d,]/g, '').split(',');
    
            alpha = alpha > 1 ? (alpha / 100) : alpha;
            object.style.backgroundColor = "rgba(" + [match[0],match[1],match[2],alpha].join(',') +")";
    
}


var datasets = $('#datasets .thumbnail');

datasets.map(function() {
    
    $(this).find('.open-modal').click( function (e) {

        var pointed_modal = $(this).attr("href");
        
        $(pointed_modal).modal('toggle');

        e.preventDefault();

    });
             
});


var publications = $('#publications .thumbnail');

publications.map(function() {
   
    var bibtex = $(this).find('.bibtex');
    var bibtex_text = $(this).find('.bibtex-text');
    
    

    $(bibtex).click(function(e) {

        $(bibtex_text).toggleClass('active');
        
        e.preventDefault();

    });
    
});




