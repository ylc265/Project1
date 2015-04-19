// var courses = ['CSCI-UA 201', 'CSCI-UA 202', 'CSCI-UA 203', 'MATH-UA 102', 'MATH-UA 103'];

var course_auto = new Bloodhound({
	datumTokenizer: Bloodhound.tokenizers.obj.whitespace('course_number'),
  	queryTokenizer: Bloodhound.tokenizers.whitespace,
  	remote: '/frontpage/autocoursesearch?Search=Search&q=%QUERY&autocomplete=yes'
});

course_auto.initialize();

$('#bloodhound .typeahead').typeahead({
	hint: true,
	highlight: true,
	minLength: 1
},
{
	name: 'courses',
	displayKey: 'course_number',
	source: course_auto.ttAdapter()
});