// $("#delete_course").click(function(){
// 	console.log("clicked me");
// });

function delete_course(course_block){
	$.ajax({
		type: 'POST',
		url: '/frontpage/delete_course/',
		data:{'course_id': course_block.find('b').html()},
		asynch:false,
		success: function(){
			location.reload();
		}
	});
	console.log(course_block.find('b').html());
}