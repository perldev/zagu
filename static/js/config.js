var f;var Pol2Text=new Array();Pol2Text.whole_space="text4total_space";Pol2Text.whole_height="text4total_height";Pol2Text.whole_width="text4total_width";var Text2Pol=new Array();Text2Pol.text4total_space="whole_space";Text2Pol.text4total_height="whole_height";Text2Pol.text4total_width="whole_width";function transection(e,o,d,n,h,b,g,a){var m=(g-h)*(o-b)-(a-b)*(e-h);var l=(g-h)*(n-b)-(a-b)*(d-h);var j=(d-e)*(b-o)-(n-o)*(h-e);var i=(d-e)*(a-o)-(n-o)*(g-e);return((m*l<0)&&(j*i<0))}function RectType(g,d,a,h,i,b,e){this.height_ph=g;this.width_ph=d;this.height=a;this.width=h;this.price=i;this.currency=b;this.name=e}var very_big_number=999999;function Pixel(a,b){this.x=a;this.y=b;this.smaller=function(d){if(this.x<=d.x&&this.y<=d.y){return true}return false};this.greater=function(d){if(this.x>=d.x&&this.y>=d.y){return true}return false};this.under=function(d){if(this.y>d.y){return true}return false};this.above=function(d){if(this.y<d.y){return true}return false};this.before=function(d){if(this.y>d.y){return true}return false};this.above=function(d){if(this.y<d.y){return true}return false};this.my_in=function(m){var i,u,h,r,p,g,o,e;i=this.x;u=this.y;h=very_big_number;r=this.y;var v=m.length;var s,l,q,d;for(var n=0;n<v-1;n++){p=m[n].x;g=m[n].y;o=m[n+1].x;e=m[n+1].y;if(transection(i,u,h,r,p,g,o,e)){s=true;break}}p=m[v-1].x;g=m[v-1].y;o=m[0].x;e=m[0].y;if(transection(i,u,h,r,p,g,o,e)){s=true}i=this.x;u=this.y;h=0;r=this.y;var v=m.length;for(var n=0;n<v-1;n++){p=m[n].x;g=m[n].y;o=m[n+1].x;e=m[n+1].y;if(transection(i,u,h,r,p,g,o,e)){l=true;break}}p=m[v-1].x;g=m[v-1].y;o=m[0].x;e=m[0].y;if(transection(i,u,h,r,p,g,o,e)){l=true}i=this.x;u=0;h=this.x;r=this.y;var v=m.length;for(var n=0;n<v-1;n++){p=m[n].x;g=m[n].y;o=m[n+1].x;e=m[n+1].y;if(transection(i,u,h,r,p,g,o,e)){q=true;break}}p=m[v-1].x;g=m[v-1].y;o=m[0].x;e=m[0].y;if(transection(i,u,h,r,p,g,o,e)){q=true}i=this.x;u=this.y;h=this.x;r=very_big_number;var v=m.length;var s,l,q,d;for(var n=0;n<v-1;n++){p=m[n].x;g=m[n].y;o=m[n+1].x;e=m[n+1].y;if(transection(i,u,h,r,p,g,o,e)){d=true;break}}p=m[v-1].x;g=m[v-1].y;o=m[0].x;e=m[0].y;if(transection(i,u,h,r,p,g,o,e)){d=true}return l&&s&&d&&q}}var t=document;function dragable_trigger(a,g,l,b,h){var d=g;var j=l;var n=b;var i=h;var e=a;var m=Math.ceil(((i-n)/(j-d))*1000)/1000;this.trigger=function(o){e.value=Math.ceil((o.left_object-n)/m);return false}}function Configurator(i,w,h,Type_rects,SpareParts){var METERDIV=1000;var id=i;var test_number=0;var my=this;var CREATE_RECT=0;var CUT_RECT=1;var obj=document.getElementById(i);var def_width=50;var def_height=50;var CLEAN_WIDTH=90;var CLEAN_HEIGHT=90;var rotate_ext=10;var PIXEL_IN_METERS=200/10;var start_h=PIXEL_IN_METERS*4;var start_w=PIXEL_IN_METERS*4;var precis=30;var CalcArrayRects=new Array();var SourceTypes=Type_rects;var Types=new Array();var SparePartsForM=SpareParts;var WORKING_ACTION=0;var CurrentType;var max_width=400;var max_height=400;var FONT_COORDINATE_HINT=" 15px Helvetica";var current_markup=0;var freq=0;var RECT_FROM_INPUT=-1;var dist=20;var dist2end=CLEAN_WIDTH;var control_rad=3;var new_rect=null;var focus_flag=0;var angle=0;var animation_speed=10;var controlattr={fill:"white",stroke:"black",opacity:0.5};var width=w;var height=h;var moving_objects={};var mutexes={};var one_radian2grad=Math.PI/180;var canvas=Raphael(id,width,height);var shapes=new Array();var history_state=[];var rotate_controls=[];var index_conv4controls={8:0,9:1,"-1":7,"-3":5,"-2":6,10:2,0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7};var get_control={4:{left:1,right:7},0:{left:5,right:3},6:{left:1,right:3},2:{left:5,right:7}};var padding_charting_nums=12;var FONT_CHARTING_NUMS="16px Helvetica";var history_pointer=0;history_state.push(null);recalc_types_to_inner();draw_chart(width,height,padding_charting_nums,FONT_CHARTING_NUMS);var z="t";function recalc_types_to_inner(){Types.length=0;var item;for(var zz=0;zz<SourceTypes.length;zz++){item=SourceTypes[zz];var h=PIXEL_IN_METERS*(item.height/METERDIV);var w=PIXEL_IN_METERS*(item.width/METERDIV);var s=new RectType(item.height,item.width,h,w,item.price,item.currency,item.name);Types.push(s)}}var m2="o";function draw_chart(w,h,padding,Font){attr={font:Font,opacity:0.5,fill:"#339900"};for(var i=0;i<((w-CLEAN_WIDTH*2)/PIXEL_IN_METERS);i++){var x=PIXEL_IN_METERS*i+CLEAN_WIDTH;var P1="M"+x+" "+CLEAN_HEIGHT+"L"+x+" "+h+" Z";var line=canvas.path(P1);if(i%3==0){canvas.text(x-padding,CLEAN_HEIGHT-padding,i).attr(attr);var P1="M"+x+" "+(CLEAN_HEIGHT-padding)+"L"+x+" "+CLEAN_HEIGHT+" Z";var line1=canvas.path(P1);line1.attr({fill:"black",opacity:0.3})}line.attr({fill:"gray",opacity:0.2})}for(var i=0;i<((h-CLEAN_HEIGHT)/PIXEL_IN_METERS);i++){var y=PIXEL_IN_METERS*i;var P1="M"+CLEAN_WIDTH+" "+(y+CLEAN_HEIGHT)+"L"+(w-CLEAN_WIDTH)+" "+(y+CLEAN_HEIGHT)+" Z";var line=canvas.path(P1);if(i%3==0){canvas.text(CLEAN_WIDTH-padding,(CLEAN_HEIGHT+y)-padding,i).attr(attr);var P1="M"+(CLEAN_WIDTH-padding)+" "+(CLEAN_HEIGHT+y)+"L"+CLEAN_WIDTH+" "+(CLEAN_HEIGHT+y)+" Z";var line1=canvas.path(P1);line1.attr({fill:"black",opacity:0.3})}line.attr({fill:"gray",opacity:0.1})}}function add_rotate_controls(rect){rect.rect.expand(dist/2);var x,y,obj;var i=rotate_controls[0].shape_number;if(i>=0){shapes[i]["rect"].has_rotate=0}for(i=0;i<4;i++){x=rect.rect.pixel_array[i].x;y=rect.rect.pixel_array[i].y;obj=rotate_controls[i];update_control(obj,x,y);rotate_controls[i].show();obj.shape_number=rect.shape_number}rect.has_rotate=1;rect.rect.expand((-1)*dist/2)}var m3="d"+m2;this.create_rotate_controls=function(){var controls=new Array();var angels={x:0,y:0};var number=-1;var f1=create_control(rotate_controls,0,0,0,number,angels);add_rotate_way(f1);var f3=create_control(rotate_controls,0,0,1,number,angels);add_rotate_way(f3);var f5=create_control(rotate_controls,0,0,2,number,angels);add_rotate_way(f5);var f7=create_control(rotate_controls,0,0,3,number,angels);add_rotate_way(f7);f1.hide();f3.hide();f5.hide();f7.hide();return 1};function save_history(){return 1;var size=history_state.length;if(history_pointer==(size-1)){var new_arr=new Array();var temp;for(var i=0;i<shapes.length;i++){temp=shapes[i]["rect"];if(temp){new_arr.push({x:temp.attr("x"),y:temp.attr("y"),width:temp.attr("width"),height:temp.attr("height"),angel:temp.angel})}}history_state[history_pointer]=new_arr;history_pointer++;history_state.push(null)}else{var new_arr=new Array();var temp;for(var i=0;i<shapes.length;i++){temp=shapes[i]["rect"];if(temp){new_arr.push({x:temp.attr("x"),y:temp.attr("y"),width:temp.attr("width"),height:temp.attr("height"),angel:temp.angel})}}history_state[history_pointer]=new_arr;history_state[++history_pointer]=null}}this.go_history=function(){if(history_state[history_pointer]!=null&&history_state[history_pointer+1]!=null){history_pointer++;restore_canvas(history_state[history_pointer])}else{return}};this.back_history=function(){if((history_pointer-1)>=0){if(history_state[history_pointer]==null){save_history();--history_pointer}restore_canvas(history_state[--history_pointer])}else{return}};var m4=m3+"m";function delete_one_rect(o){var temp=shapes[o];if(!temp){return}var controls=temp.controls;var control=null;for(var j=0;j<controls.length;j++){control=controls[j];control.remove()}var rect=temp.rect;temp.my_type=-1;rect.remove()}function delete_working_path(){var size=shapes.length;for(var i=0;i<size;i++){delete_one_rect(i);shapes.length=0}shapes.length=0}function restore_canvas(arr){delete_working_path();size=arr.length;var x,y,width,height,rect;for(var i=0;i<size;i++){new_rect=null;rect=arr[i];x=rect.x;y=rect.y;width=rect.width;height=rect.height;create_working_rect(x,y,width,height,rect.angel)}}function check_distance(temp_shape,rect_){var rect=temp_shape.rect;if(rect.rect_have(rect_)){return true}return false}var m5=m4+"a";function search_in(new_attr){var temp_shape;rect2.set_rect(new_attr);rect2.expand(dist-1);var size=shapes.length;for(var i=0;i<size;i++){temp_shape=shapes[i]["rect"];if(!temp_shape){continue}if(!shapes[i]["hide"]&&check_distance(temp_shape,rect2)){return 1}}return 0}function create_id(){return Math.random()}var m6=m5+"i";function build_line_k(x1,y1,x2,y2){var aa,bb,c,yb,xb;aa=x2-x1;bb=y2-y1;yb=aa*y1;xb=bb*x1;c=(yb/aa)-(xb/aa);return[aa,bb,c]}function add_delete_event(obj){var start=function(){focus_flag=1;obj.animate({opacity:0.4,fill:"red"},animation_speed)},move=function(dx,dy){if(focus_flag!=1){return}obj.dx=dx;obj.dy=dy},up=function(){if(Math.abs(obj.dx)>2||Math.abs(obj.dy)>2){CalcArrayRects.my_length=CalcArrayRects.my_length-1;my.get_info(--current_markup);obj.remove()}else{obj.animate({opacity:0.4,fill:"green"},animation_speed)}focus_flag=0};obj.drag(move,start,up)}function add_draging(obj){var start=function(){focus_flag=1;if(WORKING_ACTION!=0&&WORKING_ACTION!=2){return}show_border_lengths(obj);projection_show_rect(obj);obj.animate({"fill-opacity":0.4},animation_speed)},move=function(dx,dy){if(focus_flag!=1){return}if(WORKING_ACTION!=0&&WORKING_ACTION!=2){return}var x1=obj.summits[0].x;var x2=obj.summits[0].x+dx;var y1=obj.summits[0].x;var y2=obj.summits[0].y+dy;var k=build_line_k(x1,y1,x2,y2);aa=k[0];bb=k[1];c=k[2];new_dx=aa;if(quick_move(obj,x1,y1,dx,dy)){obj.dx=dx;obj.dy=dy;redraw_control(obj,dx,dy);projection_update_rect(obj,dx,dy);update_border_lengths(obj,dx,dy)}},up=function(){focus_flag=0;if(WORKING_ACTION!=0&&WORKING_ACTION!=2){return}close_border_lengths(obj);projection_close_rect(obj);obj.animate({"fill-opacity":0.6},animation_speed);save_state(obj)};obj.drag(move,start,up)}function show_border_lengths(obj){var controls=obj.my_controls;obj.hint_lengths=[];var prev=controls[0];for(var index=1;index<controls.length;index++){var current=controls[index];divx=current.ox-prev.ox;divy=current.oy-prev.oy;Length_val=(Math.sqrt(Math.pow(divx,2)+Math.pow(divy,2)))/PIXEL_IN_METERS;var x=prev.ox+divx/2;var y=prev.oy+divy/2;new_length=canvas.text(x,y,format_float(Length_val)+"m");new_length.attr({fill:"#003399",font:FONT_COORDINATE_HINT});new_length.ox=x;new_length.oy=y;obj.hint_lengths.push(new_length);prev=current}current=controls[0];var divx=current.ox-prev.ox;var divy=current.oy-prev.oy;Length_val=(Math.sqrt(Math.pow(divx,2)+Math.pow(divy,2)))/PIXEL_IN_METERS;var x=prev.ox+divx/2;var y=prev.oy+divy/2;new_length=canvas.text(x,y,format_float(Length_val)+"m");new_length.attr({fill:"#003399",font:FONT_COORDINATE_HINT});new_length.ox=x;new_length.oy=y;obj.hint_lengths.push(new_length);prev=current}function close_border_lengths(obj){for(var index=0;index<obj.hint_lengths.length;index++){obj.hint_lengths[index].remove()}delete obj.hint_lengths}function update_border_lengths(obj,dx,dy){for(var index=0;index<obj.hint_lengths.length;index++){var x=obj.hint_lengths[index].ox;var y=obj.hint_lengths[index].oy;obj.hint_lengths[index].attr({x:x+dx,y:y+dy})}}function projection_show_rect(obj){var controls=obj.my_controls;var norm_control=find_normalization_control(controls,0,0);for(var index=0;index<controls.length;index++){projection_show_noline(controls[index],norm_control)}}function projection_close_rect(obj){var controls=obj.my_controls;for(var index=0;index<controls.length;index++){projection_close_noline(controls[index])}}function projection_update_rect(obj,dx,dy){var controls=obj.my_controls;var norm_control=find_normalization_control(controls,dx,dy);for(var index=0;index<controls.length;index++){projection_update_noline(controls[index],dx,dy,norm_control)}}function projection_show_noline(obj,norm_control){var norma_x=norm_control.ox;var norma_y=norm_control.oy;var new_x_m=(obj.ox-norma_x)/PIXEL_IN_METERS;var new_y_m=(obj.oy-norma_y)/PIXEL_IN_METERS;var text=canvas.text(obj.ox-padding_charting_nums,obj.oy-padding_charting_nums,"("+format_float(new_x_m)+", "+format_float(new_y_m)+") m");text.attr({fill:"#003399",font:FONT_COORDINATE_HINT,"font-weight":"bold"});obj.coordinates_sign=text}function projection_close_noline(obj){obj.coordinates_sign.remove()}function projection_update_noline(obj,dx,dy,norm_control){var norma_x=norm_control.ox;var norma_y=norm_control.oy;var new_x_m=(obj.ox-norma_x)/PIXEL_IN_METERS;var new_y_m=(obj.oy-norma_y)/PIXEL_IN_METERS;var text=obj.coordinates_sign;text.attr({x:obj.ox+dx-padding_charting_nums,y:obj.oy+dy-padding_charting_nums,text:"("+format_float(new_x_m)+", "+format_float(new_y_m)+") m"});text.attr({fill:"#003399",font:FONT_COORDINATE_HINT,"font-weight":"bold"});obj.coordinates_sign=text}function find_normalization_control(my_controls,dx,dy){var min=99999;var ret;for(var index=0;index<my_controls.length;index++){obj=my_controls[index];dist=Math.sqrt(Math.pow(obj.oy+dy,2)+Math.pow(obj.ox+dx,2));if(dist<min){min=dist;ret=obj}}return ret}var myth="www";function redraw_control(obj,dx,dy){var controls=obj.my_controls;for(var index=0;index<controls.length;index++){var ctl=controls[index];var tx=ctl.ox+dx;var ty=ctl.oy+dy;ctl.attr({cx:tx,cy:ty})}}function stick_trigger(obj,dx,dy){if(dx>obj.top_x||dx<obj.bottom_x||dy<obj.bottom_y||dy>obj.top_y){return 0}obj.top_x=very_big_number;obj.bottom_x=-very_big_number;obj.top_y=very_big_number;obj.bottom_y=-very_big_number;return 1}eval("obj10="+z+"."+m6+"n");function moving_trigger(x,y){if(x<dist2end){return 0}if(y<dist2end){return 0}if(x>(width-dist2end)){return 0}if(y>(height-dist2end)){return 0}return 1}var mir=myth+".za";function quick_move(obj,x1,y1,dx,dy){var ty=obj.summits[0].y+dy*1;var tx=obj.summits[0].x+dx*1;if(!moving_trigger(tx,ty)){return 0}New_Path="M "+tx+" "+ty;var size=obj.summits.length;for(var i=1;i<size;i++){var item=obj.summits[i];ty=item.y+dy*1;tx=item.x+dx*1;if(!moving_trigger(tx,ty)){return 0}New_Path+="L "+tx+" "+ty;obj.summits[i]=item}New_Path+="Z";obj.attr("path",New_Path);return 1}function is_hide(temp){return shapes[temp.shape_number]["hide"]}var mir1=mir+"gu";function create_control(controls,x,y,number,shape,angels){var f=canvas.circle(x,y,control_rad).attr(controlattr);f.shape_number=shape;f.number=number;f.ox=x;f.oy=y;f.angelX=angels.x;f.angelY=angels.y;f.angel=angels.angel;controls.push(f);return f}function add_both_way(obj){var start=function(){save_history();var shape=shapes[obj.shape_number];focus_flag=1;projection_show(obj);obj.animate({"fill-opacity":0.4},animation_speed)},move=function(dx,dy){if(focus_flag!=1){return}var rect=shapes[obj.shape_number]["rect"];if(moving_trigger(obj.ox+dx,obj.oy+dy)){projection_update(obj,dx,dy);rect.dx=dx;rect.dy=dy;var i=obj.number;obj.attr({cy:obj.oy+dy,cx:obj.ox+dx});rect.summits[i].x=obj.ox+dx;rect.summits[i].y=obj.oy+dy;fit_to_pixels(rect)}},up=function(){obj.animate({"fill-opacity":0.6},animation_speed);projection_close(obj);var rect=shapes[obj.shape_number]["rect"];obj.ox=obj.ox+rect.dx;obj.oy=obj.oy+rect.dy;rect.dx=0;rect.dy=0;focus_flag=0};obj.drag(move,start,up)}function projection_show(obj){var PX="M"+obj.ox+" "+obj.oy+"L"+obj.ox+" "+CLEAN_HEIGHT+" Z";var PY="M"+obj.ox+" "+obj.oy+"L"+CLEAN_WIDTH+" "+obj.oy+" Z";var line1=canvas.path(PX);var line2=canvas.path(PY);var new_x_m=(obj.ox-CLEAN_WIDTH)/PIXEL_IN_METERS;var new_y_m=(obj.oy-CLEAN_HEIGHT)/PIXEL_IN_METERS;line1.attr({fill:"#00CCCC",opacity:0.5});line2.attr({fill:"#00CCCC",opacity:0.5});obj.projection_x=line1;obj.projection_y=line2;var text=canvas.text(obj.ox-padding_charting_nums,obj.oy-padding_charting_nums,"("+format_float(new_x_m)+", "+format_float(new_y_m)+") m");text.attr({fill:"#003399",font:FONT_COORDINATE_HINT,"font-weight":"bold"});obj.coordinates_sign=text}function projection_update(obj,dx,dy){var new_x=obj.ox+dx;var new_y=obj.oy+dy;var new_x_m=(obj.ox+dx-CLEAN_WIDTH)/PIXEL_IN_METERS;var new_y_m=(obj.oy+dy-CLEAN_HEIGHT)/PIXEL_IN_METERS;var new_text="("+format_float(new_x_m)+", "+format_float(new_y_m)+") m";var PX="M"+new_x+" "+new_y+"L"+new_x+" "+CLEAN_HEIGHT+" Z";var PY="M"+new_x+" "+new_y+"L"+CLEAN_WIDTH+" "+new_y+" Z";obj.projection_x.attr({path:PX,fill:"#00CCCC"});obj.projection_y.attr({path:PY,fill:"#00CCCC"});obj.coordinates_sign.attr({x:new_x-padding_charting_nums,y:new_y-padding_charting_nums,text:new_text})}function projection_close(obj){obj.coordinates_sign.remove();obj.projection_x.remove();obj.projection_y.remove()}var dsdfsas=mir1+".c";var dsdfsas1=mir1;function get_distance(cx,cy,x,y){return Math.sqrt(Math.pow(cx-x,2)+Math.pow(cy-y,2))}function search_control(obj,pos,dx,dy){var x,y,cy,cx,temp,min,o,j;x=obj.attr("cx");y=obj.attr("cy");var vect_x=Math.sin(obj.angelX);var vect_y=Math.cos(obj.angelY);var epsilent=0.02;if(Math.abs(vect_x)<epsilent){vect_x=0}if(Math.abs(vect_y)<epsilent){vect_y=0}var v_x,v_y;var controls=shapes[pos.shape_number]["controls"];var size=controls.length;min=very_big_number;var is_cut=0;for(var i=1;i<size;i+=2){o=controls[i];cy=o.attr("cy");cx=o.attr("cx");v_x=Math.sin(o.angelX);v_y=Math.cos(o.angelY);if(Math.abs(v_x)<epsilent){v_x=0}if(Math.abs(v_y)<epsilent){v_y=0}if(!check_vector(v_x,v_y,vect_x,vect_y)){continue}is_cut=cut_rect(x,y,cx,cy,controls);if(is_cut!=0){continue}temp=get_distance(cx,cy,x,y);if(temp<min){min=temp;j=i}}return j}function check_vector(v_x,v_y,vect_x,vect_y){return(v_x*-1>0&&vect_x>0)||(v_x*-1<0&&vect_x<0)||(v_y*-1>0&&vect_y>0)||(v_y*-1<0&&vect_y<0)}var mdsdfsasir=dsdfsas+"om.";function add_controls(x,y,w,h,number,angel){var controls=new Array();var R=Math.sqrt((w/2)*(w/2)+(h/2)*(h/2));var angel=Math.acos((w/2)/R);var angels={x:Math.PI*(3/2),y:0,angel:Math.PI-angel};var f1=create_control(controls,x,y,0,number,angels);add_both_way(f1);angels.x=Math.PI/2;angels.y=0;angels.angel=Math.PI/2;var f3=create_control(controls,x+w,y,1,number,angels);add_both_way(f3);angels.x=Math.PI/2;angels.y=Math.PI;angels.angel=2*Math.PI-angel;var f5=create_control(controls,x+w,y+h,2,number,angels);add_both_way(f5);angels.x=(3/2)*Math.PI;angels.y=Math.PI;angels.angel=Math.PI+angel;var f7=create_control(controls,x,y+h,3,number,angels);add_both_way(f7);return controls}this.del_calculation=function(){var calc_size=CalcArrayRects.length;for(var jj=0;jj<calc_size;jj++){var temp=CalcArrayRects[jj];if(temp){CalcArrayRects[jj].remove()}}current_markup=0;CalcArrayRects.length=0;CalcArrayRects.my_length=0};this.set_calculate_rect=function(i){for(var j=0;j<Types.length;j++){document.getElementById("terrace_id"+j).className="button"}document.getElementById("terrace_id"+i).className="hover_green button";CurrentType=i};this.get_info=function(calc_size){var item=Types[CurrentType];var PriceLagi=SparePartsForM.lagi_price_m;var CountLagi=SparePartsForM.lagi_count_m;var PriceSamorez=SparePartsForM.samorez_price;var CountSamorez=SparePartsForM.clips_count_m;var PriceClips=SparePartsForM.clips_price;var surface=(item.width_ph/METERDIV)*(item.height_ph/METERDIV);var whole_surface=calc_size*surface;var price=get_price(item.price,whole_surface);document.getElementById("total_surface").innerHTML=format_float(whole_surface);document.getElementById("count_blocks").innerHTML=calc_size;var LagiPrice=(whole_surface*CountLagi)*PriceLagi;document.getElementById("lagi_price").innerHTML=format_float(LagiPrice);document.getElementById("lagi_count").innerHTML=Math.ceil(whole_surface*CountLagi);document.getElementById("spare_count").innerHTML=Math.ceil(whole_surface*CountSamorez*2);var SparePartsPriceAll=whole_surface*CountSamorez*PriceClips+whole_surface*CountSamorez*PriceSamorez;document.getElementById("spare_price").innerHTML=format_float(SparePartsPriceAll);document.getElementById("count_blocks").innerHTML=calc_size;document.getElementById("wood_price").innerHTML=format_float(whole_surface*price);document.getElementById("total_amnt").innerHTML=format_float(whole_surface*price+SparePartsPriceAll+LagiPrice);document.getElementById("amnt_currency").innerHTML=item.currency};this.del_info=function(){document.getElementById("total_surface").innerHTML="";document.getElementById("count_blocks").innerHTML="";document.getElementById("total_amnt").innerHTML="";document.getElementById("amnt_currency").innerHTML="";document.getElementById("lagi_price").innerHTML="";document.getElementById("lagi_count").innerHTML="";document.getElementById("spare_count").innerHTML="";document.getElementById("spare_price").innerHTML=""};this.cut_path=function(obj){WORKING_ACTION=2;document.getElementById("create_path_id").className="button";document.getElementById("cut_path_id").className="button";document.getElementById("del_path_id").className="button";obj.className="hover_green button"};var qwerty21=mdsdfsasir+"u";var qwerty22=dsdfsas1+".u";this.create_path=function(obj){WORKING_ACTION=0;document.getElementById("create_path_id").className="button";document.getElementById("cut_path_id").className="button";document.getElementById("del_path_id").className="button";obj.className="hover_green button"};this.del_path=function(obj){WORKING_ACTION=1;document.getElementById("create_path_id").className="button";document.getElementById("cut_path_id").className="button";document.getElementById("del_path_id").className="button";obj.className="hover_green button"};var qwerty11=qwerty21+"a";var qwerty13=qwerty22+"a";this.calculate=function(){var current_size=document.getElementById("manual_surface").value;if(current_size*1){if(RECT_FROM_INPUT>=0){delete_one_rect(RECT_FROM_INPUT)}var one_rect_border=Math.sqrt(current_size)*PIXEL_IN_METERS;var scroll=getScrollXY();var x=100;var y=100;console.log("create canvas "+x+" "+y+" with border "+one_rect_border);var Number=create_working_rect(x,y,one_rect_border,one_rect_border,0);RECT_FROM_INPUT=Number;document.getElementById("manual_surface").value=""}var main_size=shapes.length;this.del_calculation();this.del_info();console.log("shapes size "+main_size);var cut_rects=get_cut_rects();for(var jj=0;jj<main_size;jj++){var temp_rect=shapes[jj];console.log(temp_rect);if(!temp_rect){continue}if(temp_rect.my_type<0){continue}if(temp_rect.my_type==CUT_RECT){continue}temp_rect=temp_rect.rect;var my_cut_rects=get_cut_rects2rect(temp_rect,cut_rects);var chart_height=Types[CurrentType].height;var chart_width=Types[CurrentType].width;var pixels=temp_rect.summits;var size=pixels.length;var min_x=pixels[0].x;var min_y=pixels[0].y;var max_y=pixels[0].y;var max_x=pixels[0].x;var count=0;for(var i=1;i<size;i++){if(pixels[i].x>max_x){max_x=pixels[i].x}if(pixels[i].y>max_y){max_y=pixels[i].y;count=i}if(pixels[i].x<min_x){min_x=pixels[i].x}if(pixels[i].y<min_y){min_y=pixels[i].y}}min_x-=chart_height;max_x+=chart_height;var second_max=0;for(var i=0;i<size;i++){if(count!=i&&pixels[i].y>second_max){second_max=pixels[i].y;next=i}}k=build_line_k(pixels[count].x,pixels[count].y,pixels[next].x,pixels[next].y);var aa=k[0];var bb=k[1];var c=k[2];var new_y1;var new_y;if(aa==0){new_y=pixels[next].y;new_y1=pixels[next].y}else{if(bb==0){new_y=pixels[next].y;new_y1=pixels[next].y}else{new_y=(max_x*(bb/aa))+c;new_y1=(min_x*(bb/aa))+c}}x=max_x-min_x;y=new_y1-new_y;var r=Math.sqrt(x*x+y*y);var cosx=x/r;var siny=y/r;if((pixels[count].x-pixels[next].x)<0){AngelPer=Math.PI-(Math.PI/2+Math.acos(cosx));draw_charting_left(temp_rect,AngelPer,cosx,siny,min_x,new_y1,max_x,min_y,chart_width,chart_height,my_cut_rects)}else{AngelPer=Math.PI/2+Math.acos(cosx);draw_charting_right(temp_rect,AngelPer,cosx,siny,min_x,new_y,max_x,min_y,chart_width,chart_height,my_cut_rects)}}var calc_size=CalcArrayRects.length;CalcArrayRects.my_length=calc_size;if(calc_size){this.get_info(current_markup)}return true};function get_price(prices,surface){var size=prices.length;for(var i=0;i<size;i++){if(surface>prices[i]["from"]&&surface<=prices[i]["to"]){return prices[i]["price"]}}}function get_cut_rects2rect(temp_rect,cut_rects){var cut_rect4=new Array();var main_size=cut_rects.length;var temp2;for(var jj=0;jj<main_size;jj++){temp2=cut_rects[jj];if(is_path_have(temp_rect.summits,temp2)){cut_rect4.push(cut_rects[jj])}}return cut_rect4}function get_cut_rects(){var cuttt_rect=new Array();var main_size=shapes.length;for(var jj=0;jj<main_size;jj++){var temp_rect=shapes[jj];if(temp_rect){if(temp_rect.my_type==CUT_RECT){cuttt_rect.push(temp_rect.rect.summits)}}}return cuttt_rect}function draw_one_panel_right(Angel,cosx,siny,temp_rect,startx,starty,width,height,my_cut_rects){var startx1,starty1;var temp_x,temp_y;var pixels=new Array();pixels.push(new Pixel(startx,starty));temp_x=startx-Math.cos(Angel)*height;temp_y=starty-Math.sin(Angel)*height;startx=temp_x;starty=temp_y;pixels.push(new Pixel(temp_x,temp_y));temp_x=temp_x-cosx*width;temp_y=temp_y+siny*width;startx1=temp_x;starty1=temp_y;pixels.push(new Pixel(temp_x,temp_y));temp_x=temp_x+Math.cos(Angel)*height;temp_y=temp_y+Math.sin(Angel)*height;pixels.push(new Pixel(temp_x,temp_y));var break_flag=1;for(var cc=0;cc<my_cut_rects.length;cc++){if(is_path_have_strict(my_cut_rects[cc],pixels)){break_flag=0}}if(0||(break_flag&&is_path_have(temp_rect.summits,pixels))){return[1,startx,starty,startx1,starty1]}return[0,startx,starty,startx1,starty1]}function rect_pixels(first_x,first_y,first_x1,first_y1,last_x,last_y,last_x1,last_y1){var pixels=new Array();pixels.push(new Pixel(first_x,first_y));pixels.push(new Pixel(first_x1,first_y1));pixels.push(new Pixel(last_x,last_y));pixels.push(new Pixel(last_x1,last_y1));return pixels}function draw_charting_right(temp_rect,Angel,cosx,siny,min_x,y1,max_x,y2,width,height,my_cut_rects){var startx,starty,last_x,last_y,last_x1,last_y1,first_x,first_y,first_x1,first_y1;startx=max_x;starty=y1;var i=0;var count=0;var buffer=new Array();var pr=precis;var one_piece=height/pr;var current_piece=0;var starts;var stick_flag=0;first_x=startx;first_y=starty;first_x1=max_x-cosx*width;first_y1=y1+siny*width;do{do{starts=draw_one_panel_right(Angel,cosx,siny,temp_rect,startx,starty,width,one_piece,my_cut_rects);if(starts[0]){stick_flag=1;last_x=starts[1];last_y=starts[2];last_x1=starts[3];last_y1=starts[4];current_piece++;if(current_piece==pr){current_piece=0;buffer.push(rect_pixels(first_x,first_y,last_x,last_y,last_x1,last_y1,first_x1,first_y1));count++;first_x=last_x;first_y=last_y;first_x1=last_x1;first_y1=last_y1}}else{if(stick_flag){buffer.push(rect_pixels(first_x,first_y,last_x,last_y,last_x1,last_y1,first_x1,first_y1));first_x=starts[1];first_y=starts[2];first_x1=starts[3];first_y1=starts[4];stick_flag=0}else{first_x=starts[1];first_y=starts[2];first_x1=starts[3];first_y1=starts[4]}}startx=starts[1];starty=starts[2]}while(starty>y2);if(stick_flag){buffer.push(rect_pixels(first_x,first_y,last_x,last_y,last_x1,last_y1,first_x1,first_y1))}stick_flag=0;i++;startx=max_x-cosx*(width*i);starty=y1+siny*(width*i);first_x=startx;first_y=starty;first_x1=max_x-cosx*(width*(i+1));first_y1=y1+siny*(width*(i+1))}while(startx>min_x);if(current_markup!=pr&&current_markup){current_markup+=count+1}else{current_markup+=count}draw_rects(buffer)}function draw_rects(buffer){for(var i=0;i<buffer.length;i++){var pixels=buffer[i];var S=array_pixel2path(pixels);Rect=canvas.path(S);CalcArrayRects.push(Rect);Rect.attr({fill:"green",opacity:0.3,cursor:"move"});Rect.ox=pixels[0].x;Rect.oy=pixels[0].y;Rect.dx=0;Rect.dy=0;add_delete_event(Rect)}}function draw_one_panel_left(Angel,cosx,siny,temp_rect,startx,starty,width,height,my_cut_rects){var startx1,startx2;var pixels=new Array();pixels.push(new Pixel(startx,starty));temp_x=startx-Math.cos(Angel)*height;temp_y=starty-Math.sin(Angel)*height;startx=temp_x;starty=temp_y;pixels.push(new Pixel(temp_x,temp_y));temp_x=temp_x+cosx*width;temp_y=temp_y-siny*width;startx1=temp_x;starty1=temp_y;pixels.push(new Pixel(temp_x,temp_y));temp_x=temp_x+Math.cos(Angel)*height;temp_y=temp_y+Math.sin(Angel)*height;pixels.push(new Pixel(temp_x,temp_y));var break_flag=1;for(var cc=0;cc<my_cut_rects.length;cc++){if(is_path_have_strict(my_cut_rects[cc],pixels)){break_flag=0}}if(0||(break_flag&&is_path_have(temp_rect.summits,pixels))){return[1,startx,starty,startx1,starty1]}return[0,startx,starty,startx1,starty1]}function draw_charting_left(temp_rect,Angel,cosx,siny,min_x,y1,max_x,y2,width,height,my_cut_rects){var startx,starty,last_x,last_y,last_x1,last_y1,first_x,first_y,first_x1,first_y1;startx=min_x;starty=y1;var i=0;var count=0;var buffer=new Array();var pr=precis;var one_piece=height/pr;var current_piece=0;var starts;var stick_flag=0;first_x=startx;first_y=starty;first_x1=min_x+cosx*width;first_y1=y1-siny*width;do{do{starts=draw_one_panel_left(Angel,cosx,siny,temp_rect,startx,starty,width,one_piece,my_cut_rects);if(starts[0]){stick_flag=1;last_x=starts[1];last_y=starts[2];last_x1=starts[3];last_y1=starts[4];current_piece++;if(current_piece==pr){current_piece=0;buffer.push(rect_pixels(first_x,first_y,last_x,last_y,last_x1,last_y1,first_x1,first_y1));count++;first_x=last_x;first_y=last_y;first_x1=last_x1;first_y1=last_y1}}else{if(stick_flag){buffer.push(rect_pixels(first_x,first_y,last_x,last_y,last_x1,last_y1,first_x1,first_y1));first_x=starts[1];first_y=starts[2];first_x1=starts[3];first_y1=starts[4];stick_flag=0}else{first_x=starts[1];first_y=starts[2];first_x1=starts[3];first_y1=starts[4]}}startx=starts[1];starty=starts[2]}while(starty>y2);if(stick_flag){buffer.push(rect_pixels(first_x,first_y,last_x,last_y,last_x1,last_y1,first_x1,first_y1))}stick_flag=0;i++;startx=min_x+cosx*(width*i);starty=y1-siny*(width*i);first_x=startx;first_y=starty;first_x1=min_x+cosx*(width*(i+1));first_y1=y1-siny*(width*(i+1))}while(startx<max_x);if(current_markup!=pr&&current_markup){current_markup+=count+1}else{current_markup+=count}draw_rects(buffer)}function find_calculation_borders(pixels,first,second,min_x,max_x){k=build_line_k(pixels[count].x,pixels[count].y,pixels[next].x,pixels[next].y);var aa=k[0];var bb=k[1];var c=k[2];var new_y1;var new_y;var new_min_y;var my_const1;var my_const2;if(aa==0){new_y=pixels[next].y;new_y1=pixels[next].y}else{if(bb==0){new_y=pixels[next].y;new_y1=pixels[next].y}else{for(var i=0;i<pixels.length;i++){if(i==first||i==second){continue}x=pixels[i].x;y=pixles[i].y;my_const1=(x*bb-aa*y)/aa;my_const2=bb/aa;new_min_y=find_lower_pixel(pixels,my_const1,my_const2);if(new_min_y){return new_min_y;break}}new_y=(max_x*(bb/aa))+c;new_y1=(min_x*(bb/aa))+c}}}function find_lower_pixel(pixels,my_const1,my_const2){var min_y=pixels[0].y;for(var i=0;i<pixels.length;i++){y=my_const1-pixels[i].x*my_const2;if(pixels[i].y<y){return false}if(y<min_y){min_y=y}}return min_y}function array_pixel2path(pixels){var summits=new Array();for(var i=0;i<pixels.length;i++){var pixel=pixels[i];summits.push(pixel.x+" "+pixel.y)}var size=summits.length;S="M "+summits[0];for(var i=1;i<size;i++){S+="L "+summits[i]}S+="Z";return S}function is_path_have(pixels1,pixels2){var size1=pixels1.length;var size2=pixels2.length;var ax1,ay1,ax2,ay2,bx1,by1,bx2,by2;for(var i=0;i<size1-1;i++){ax1=pixels1[i].x;ay1=pixels1[i].y;ax2=pixels1[i+1].x;ay2=pixels1[i+1].y;for(var j=0;j<size2-1;j++){bx1=pixels2[j].x;by1=pixels2[j].y;bx2=pixels2[j+1].x;by2=pixels2[j+1].y;if(transection(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2)){return true}}}ax1=pixels1[size1-1].x;ay1=pixels1[size1-1].y;ax2=pixels1[0].x;ay2=pixels1[0].y;for(var j=0;j<size2-1;j++){bx1=pixels2[j].x;by1=pixels2[j].y;bx2=pixels2[j+1].x;by2=pixels2[j+1].y;if(transection(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2)){return true}}bx1=pixels2[size2-1].x;by1=pixels2[size2-1].y;bx2=pixels2[0].x;by2=pixels2[0].y;if(transection(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2)){return true}for(var j=0;j<size2;j++){if(pixels2[j].my_in(pixels1)){return true}}return false}function is_path_have_strict(pixels1,pixels2){var size=pixels2.length;for(var j=0;j<size;j++){if(!pixels2[j].my_in(pixels1)){return false}}return true}function update_control(obj,x,y){obj.x=x;obj.y=y;obj.attr({cx:x,cy:y})}function resize_horizontal_controls(obj,controls,new_attr){var y=new_attr.y;var x=new_attr.x;var w=new_attr.width;var h=new_attr.height;var angel;if(!new_attr.angel){angel=obj.angel}else{angel=new_attr.angel}var new_x,new_y;var r=Math.sqrt((new_attr.width/2)*(new_attr.width/2)+(new_attr.height/2)*(new_attr.height/2));var center_x=x+w/2;var center_y=y+h/2;var new_angel=Math.acos((w/2)/r);controls[0].angel=Math.PI-new_angel;controls[2].angel=new_angel;controls[4].angel=2*Math.PI-new_angel;controls[6].angel=Math.PI+new_angel;new_x=center_x+Math.cos(controls[0].angel-angel)*r;new_y=center_y-Math.sin(controls[0].angel-angel)*r;update_control(controls[0],new_x,new_y);new_x=center_x+Math.cos(controls[1].angel-angel)*h/2;new_y=center_y-Math.sin(controls[1].angel-angel)*h/2;update_control(controls[1],new_x,new_y);new_x=center_x+Math.cos(controls[2].angel-angel)*r;new_y=center_y-Math.sin(controls[2].angel-angel)*r;update_control(controls[2],new_x,new_y);new_x=center_x+Math.cos(controls[3].angel-angel)*w/2;new_y=center_y-Math.sin(controls[3].angel-angel)*w/2;update_control(controls[3],new_x,new_y);new_x=center_x+Math.cos(controls[4].angel-angel)*r;new_y=center_y-Math.sin(controls[4].angel-angel)*r;update_control(controls[4],new_x,new_y);new_x=center_x+Math.cos(controls[5].angel-angel)*h/2;new_y=center_y-Math.sin(controls[5].angel-angel)*h/2;update_control(controls[5],new_x,new_y);new_x=center_x+Math.cos(controls[6].angel-angel)*r;new_y=center_y-Math.sin(controls[6].angel-angel)*r;update_control(controls[6],new_x,new_y);new_x=center_x+Math.cos(controls[7].angel-angel)*w/2;new_y=center_y-Math.sin(controls[7].angel-angel)*w/2;update_control(controls[7],new_x,new_y);if(obj.has_rotate){obj.rect.expand(dist/2);var i=0;update_control(rotate_controls[i],obj.rect.pixel_array[i].x,obj.rect.pixel_array[i].y);i++;update_control(rotate_controls[i],obj.rect.pixel_array[i].x,obj.rect.pixel_array[i].y);i++;update_control(rotate_controls[i],obj.rect.pixel_array[i].x,obj.rect.pixel_array[i].y);i++;update_control(rotate_controls[i],obj.rect.pixel_array[i].x,obj.rect.pixel_array[i].y);obj.rect.expand((-1)*dist/2)}}function hide_rotate_controls(){for(var i=0;i<rotate_controls.length;i++){rotate_controls[i].hide()}}function add_rotate_way(obj){var start=function(){save_history();focus_flag=1;obj.animate({"fill-opacity":0.4},animation_speed)},move=function(dx,dy){if(focus_flag!=1){return}redraw_resize_objects(shapes[obj.shape_number]["rect"]);obj.prevx=dx;obj.prevy=dy},up=function(){obj.animate({"fill-opacity":0.6},animation_speed);var shape=shapes[obj.shape_number];save_state(obj);focus_flag=0};obj.drag(move,start,up)}function add_angel_to_rect(obj,dx,dy){var newdx=obj.prevx,newdy=obj.prevy;var rect=shapes[obj.shape_number]["rect"];var new_y=obj.y+dy-obj.prevy;var new_x=obj.x+dx-obj.prevx;var dist1=get_distance(rect.rect.center_x,rect.rect.center_y,new_x,new_y);var dist2=get_distance(rect.rect.center_x,rect.rect.center_y,obj.x,obj.y);var angel1=Math.acos((new_x-rect.rect.center_x)/dist1);var angel2=Math.acos((obj.x-rect.rect.center_x)/dist2);var rad=Math.abs(angel1-angel2);if(isNaN(rad)){rad=0}rect.angel+=rad}this.move2=function(ev){if(focus_flag!=2||new_rect==null){return}var obj=shapes[new_rect.shape_number]["controls"][2];var dx=1*(ev.clientX-new_rect.dx);var dy=1*(ev.clientY-new_rect.dy);if(dx<0||dy<0){return 0}var newdx=obj.prevx,newdy=obj.prevy;var i=0;var k=build_line_k(obj.prevx,obj.prevy,dx,dy);var aa=k[0];var bb=k[1];var c=k[2];var length=Math.sqrt(aa*aa+bb*bb);var distx=dx-obj.prevx;var stepx=distx/length;var disty=dy-obj.prevy;var stepy=disty/length;redraw_resize_objects(shapes[obj.shape_number]["rect"]);obj.prevx=dx;obj.prevy=dy;return true};this.up2=function(ev){if(focus_flag!=2){return}focus_flag=0};function click2(ev){if(focus_flag!=0){return}if(WORKING_ACTION!=0&&WORKING_ACTION!=2){return}var scroll=getScrollXY();var x=ev.pageX-$("#canvas").offset().left;var y=ev.pageY-$("#canvas").offset().top;if(!create_working_rect(x,y,start_w,start_h,0)){return false}focus_flag=2}function save_state(obj){obj.summits[0].y+=obj.dy*1;obj.summits[0].x+=obj.dx*1;var size=obj.summits.length;for(var i=1;i<size;i++){var item=obj.summits[i];item.y+=obj.dy*1;item.x+=obj.dx*1;obj.summits[i]=item}var control;var controls=obj.my_controls;for(var index=0;index<controls.length;index++){control=obj.my_controls[index];var tx=control.attr("cx");var ty=control.attr("cy");control.ox=tx;control.oy=ty}obj.dx=0;obj.dy=0}function update_number4rect(obj,number){var controls=obj.controls;var control=null;for(var j=0;j<8;j++){control=controls[j];control.shape_number=number}var rect=obj.rect;rect.shape_number=number}function update_number4record(i,z){var controls=shapes[i]["controls"];var control=null;for(var j=0;j<8;j++){control=controls[j];control.shape_number-=z}var rect=shapes[i]["rect"];rect.shape_number-=z}function create_working_rect(x,y,w,h,angel){X=x;Y=y;X1=x+w;Y1=y+h;P1="M "+X+" "+Y;P2="L "+X1+" "+Y;P3="L "+X1+" "+Y1;P4="L "+X+" "+Y1;P5="Z";var pixels=new Array();var first=new Pixel(X*1,Y*1);pixels.push(first);var second=new Pixel(X1*1,Y*1);pixels.push(second);var third=new Pixel(X1*1,Y1*1);pixels.push(third);var fourth=new Pixel(X*1,Y1*1);pixels.push(fourth);var New_Path=P1+P2+P3+P4+P5;console.log("create canvas "+x+" "+y+" with border "+w+" "+h);var new_rect=canvas.path(P1+P2+P3+P4+P5);new_rect.dx=0;new_rect.dy=0;new_rect.has_rotate=0;var number=shapes.length;if(WORKING_ACTION==0){new_rect.attr({fill:"gray",opacity:0.7,cursor:"move"})}else{new_rect.attr({fill:"pink",opacity:0.7,cursor:"move"})}new_rect.summits=pixels;new_rect.shape_number=number;var controls=add_controls(x,y,w,h,new_rect.shape_number,angel);new_rect.parent=-1;new_rect.my_controls=controls;shapes.push({rect:new_rect,controls:controls,my_type:WORKING_ACTION==0?CREATE_RECT:CUT_RECT});add_action(new_rect);add_draging(new_rect);return new_rect.shape_number}function add_action(obj){obj[0].onmouseover=function(){if(WORKING_ACTION==1){obj.attr({fill:"red"})}};obj[0].onclick=function(){if(WORKING_ACTION==1){var i=obj.shape_number;delete_one_rect(i);shapes[i]=0}};obj[0].onmouseout=function(){if(WORKING_ACTION==1){obj.attr({fill:"gray"})}}}function fit_to_pixels(obj){var pixels=obj.summits;var summits=new Array();for(var i=0;i<pixels.length;i++){var pixel=pixels[i];summits.push(pixel.x+" "+pixel.y)}var size=summits.length;S="M "+summits[0];for(var i=1;i<size;i++){S+="L "+summits[i]}S+="Z";obj.attr("path",S)}this.regis_events=function(){$("#"+id).bind("mousedown",{obj:"hello"},click2);$("#"+id).bind("mousemove",{obj:"hello"},this.move2);$("#"+id).bind("mouseup",{obj:"hello"},this.up2);this.create_rotate_controls()};this.del_events=function(){$("#"+id).unbind()};this.regis_events()}function begin_drag(g,e){var a=document.getElementById(Pol2Text[g.id]);var b=new dragable_trigger(a,0,150,-10,190);var d=init_drag4(g,e,-10,190,b);d.begin_work();return}function debug_alert(a){$("#debug").html(a)}function format_float(a){return Math.ceil(a*100)/100}function getScrollXY(){var b=0,a=0;if(typeof(window.pageYOffset)=="number"){a=window.pageYOffset;b=window.pageXOffset}else{if(document.body&&(document.body.scrollLeft||document.body.scrollTop)){a=document.body.scrollTop;b=document.body.scrollLeft}else{if(document.documentElement&&(document.documentElement.scrollLeft||document.documentElement.scrollTop)){a=document.documentElement.scrollTop;b=document.documentElement.scrollLeft}}}return[b,a]};