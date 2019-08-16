(function($){"use strict";$.fn.stickMe=function(options){var $window=$(window),$document=$(document),$elemTopOffset,$body=$('body'),position=0,$elem=this,$elemHeight=$elem.innerHeight(),$win_center=$window.height()/2,$pos,settings=$.extend({transitionDuration:300,shadow:!1,shadowOpacity:0.3,animate:!0,triggerAtCenter:!0,topOffset:$elemHeight,transitionStyle:'fade',stickyAlready:!1},options);$elem.addClass('stick-me').addClass('not-sticking');switch(settings.triggerAtCenter){case(settings.triggerAtCenter&&settings.topOffset<$elemHeight)||(settings.triggerAtCenter&&settings.topOffset>$elemHeight):settings.triggerAtCenter=!1;break}
if(settings.stickyAlready){settings.triggerAtCenter=!1;settings.topOffset=0;stick()}
$elemTopOffset=$elem.offset().top;function $elem_slide(){if(settings.animate===!0&&settings.transitionStyle==='slide'&&settings.stickyAlready!==!0){$elem.slideDown(settings.transitionDuration)}
if(settings.animate===!0&&settings.transitionStyle==='fade'&&settings.stickyAlready!==!0){$elem.fadeIn(settings.transitionDuration)}else{$elem.show()}
$elem.removeClass('not-sticking')}
function stick(){if($elem.hasClass('sticking')){$elem.trigger('sticking')}
if(position===0){position=1;if(settings.stickyAlready===!1){$elem.trigger('sticky-begin')}}
if($elem.hasClass('not-sticking')){$elem.hide();$elem_slide()}
if(settings.shadow===!0){$elem.css('box-shadow','0px 1px 2px rgba(0,0,0,'+settings.shadowOpacity+')')}
$elem.addClass('sticking').css('position','fixed').css('top','0');$body.css('padding-top',$elemHeight)}
function unstick(){if(settings.shadow===!0){$elem.css('box-shadow','none')}
$elem.addClass('not-sticking').removeClass('sticking').show().css('position','relative');$body.css('padding-top','0')}
$window.scroll(function(){$pos=$window.scrollTop();if($pos===0){position=0;$elem.trigger('top-reached')}
if(settings.triggerAtCenter===!0){if($pos>$win_center+$elemHeight){stick()}}
if(settings.triggerAtCenter===!1){if($pos>settings.topOffset){stick()}}
if($pos+$window.height()>$document.height()-1){$elem.trigger('bottom-reached')}
if(settings.triggerAtCenter===!0){if($pos<(1+$elemTopOffset)){unstick()}}
if(settings.triggerAtCenter===!1){if($pos<1){if(settings.stickyAlready!==!0){unstick()}}}});return this}}(jQuery))