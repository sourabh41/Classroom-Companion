from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^authlogin/$', views.authlogin, name='authlogin'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^add_course/(?P<instructor_id>.*)$', views.add_course, name = 'add_course'),
    url(r'^makecourse$', views.make_course, name = 'makecourse'),
    url(r'^addstudents/(?P<course_id>.*)$', views.addstudents, name = 'addstudents'),
    url(r'^csv/(?P<course_id>.*)$', views.add_students, name = 'csvfile'),
    url(r'^showstudents/(?P<course_id>.*)/$', views.showstudents, name = 'showstudents'),
    url(r'^make_poll/(?P<course_id>.*)/$', views.make_poll, name = 'make_poll'),
    url(r'^poll/(?P<course_id>.*)$', views.poll, name = 'poll'),
    url(r'^makequiz/(?P<course_id>.*)$', views.make_quiz, name = 'makequiz'),
    url(r'^quiz/(?P<course_id>.*)$', views.quiz, name = 'quiz'),
    url(r'^addquestions/(?P<quiz_id>.*)$', views.addquestions, name = 'addquestions'),
    url(r'^course_view/(?P<course_id>.*)/$', views.course_view, name = 'course_view'),
    url(r'^pollresults/(?P<poll_id>.*)$', views.pollresults, name = 'pollresults'),
    url(r'^quizresults/(?P<quiz_id>.*)$', views.quizresults, name = 'quizresults'),
    url(r'^deletequizzes/(?P<course_id>.*)$', views.deletequizzes, name = 'deletequizzes'),
    url(r'^deletequiz/(?P<quiz_id>.*)$', views.deletequiz, name = 'deletequiz'),
    url(r'^deletepolls/(?P<course_id>.*)$', views.deletepolls, name = 'deletepolls'),
    url(r'^deletepoll/(?P<poll_id>.*)$', views.deletepoll, name = 'deletepoll'),
    url(r'^viewfeedback/(?P<course_id>.*)$', views.viewfeedback, name = 'viewfeedback'),
    url(r'^courseview/(?P<rollno>[a-zA-Z0-9]+)/$', views.courseview.as_view(), name = 'courseview'),
    url(r'^quizview/(?P<key>[a-zA-Z0-9]+)/$', views.quizview.as_view(), name = 'quizview'),
    url(r'^questionview/(?P<key>[a-zA-Z0-9]+)/$', views.questionview.as_view(), name = 'questionview'),
    url(r'^pollview/(?P<key>[a-zA-Z0-9]+)/$', views.pollview.as_view(), name = 'pollview'),
    url(r'^feedbackview/(?P<key>[a-zA-Z0-9]+)/(?P<feedback>.+)/$', views.FeedbackSubmit, name = 'feedbackview'),
    url(r'^pollsubmit/(?P<key>[a-zA-Z0-9]+)/(?P<feedback>.+)/$', views.PollSubmit, name = 'pollsubmit'),
    url(r'^quizsubmit/(?P<key>[a-zA-Z0-9]+)/(?P<feedback>.+)/$', views.QuizSubmit, name = 'quizsubmit'),
    url(r'^querysubmit/(?P<key>.+)/(?P<feedback>.+)/$', views.make_query, name = 'querysubmit'),
    url(r'^queryview/(?P<key>.+)/$', views.queryview.as_view(), name = 'queryview'),
    url(r'^updatequery/(?P<key>.+)/(?P<feedback>.+)/$', views.update_query, name = 'updatequery'),
    url(r'^answerquery/(?P<query_id>.*)/$', views.answerquery, name = 'answerquery'),
    url(r'^savequery/(?P<query_id>.*)$', views.savequery, name = 'savequery'),
]

urlpatterns = format_suffix_patterns(urlpatterns)