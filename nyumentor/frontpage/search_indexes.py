from haystack import indexes
from frontpage.models import CourseModel

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.EdgeNgramField(model_attr='course_number', document=True, use_template=True)

	def get_model(self):
		return CourseModel

	def index_queryset(self, using=None):
		return self.get_model().objects.all()

# site.register(CourseModel, CourseIndex)