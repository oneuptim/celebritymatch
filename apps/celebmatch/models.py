from __future__ import unicode_literals
from django.db import models
import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

# Create your models here.
class Match(models.Model):
    match = models.TextField(max_length=5000, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



# class Trip(models.Model):
# 	destination = models.CharField(max_length=100, null=True)
# 	description = models.CharField(max_length=1000, null=True)
# 	start_date=models.DateTimeField(null=True)
# 	end_date=models.DateTimeField(null=True)
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	updated_at = models.DateTimeField(auto_now = True)
# 	participant = models.ForeignKey('User', null=True, related_name="tripparticipant")
# 	objects = TripManager()












































































# def analyze(self, handle):
#
#     twitter_consumer_key = 'k5pLmAB70ZsP54yqkGLVzq6Mc'
#     twitter_consumer_secret = 'vRZMEIStHYoAgjBymoRrpiqVdWOfSGEJyaLnyNxNcISmZkGqpP'
#     twitter_access_token = '1624965788-jgkGSqnJitOULMLlyS3WRhgMOwADsU0GN5yPsnw'
#     twitter_access_secret = 'AsIC34EadILRS4G1NRdWAvqKq8VZzpQpZDZyFzLHsgbOV'
#
#     twitter_api_call = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
#
#     # handle = "@BrandWithTim"
#
#     statuses = twitter_api_call.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
#
#     text = ""
#     for status in statuses:
#         if (status.lang == 'eng'):
#             text += status.text.encode('utf-8')
#             print text
#
#     pi_username = 'a70c7726-b66a-411e-869f-7e74987f39b8'
#     pi_password = '6rq8ConOjJGo'
#
#     personality_insights = PersonalityInsights(username=pi_username, pi_password=pi_password)
#
#     pi_results = personality_insights.profile(text)
#
#     return pi_results
#
# def flatten(self, orig):
#   data = {}
#   for c in orig['tree']['children']:
#     if 'children' in c:
#       for c2 in c['children']:
#         if 'children' in c2:
#           for c3 in c2['children']:
#             if 'children' in c3:
#               for c4 in c3['children']:
#                 if (c4['category'] == 'personality'):
#                   data[c4['id']] = c4['percentage']
#                   if 'children' not in c3:
#                     if (c3['category'] == 'personality'):
#                       data[c3['id']] = c3['percentage']
#     return data
#
# def compare(self, dict1, dict2):
#     compared_data = {}
#     for keys in dict1:
#         if dict1[keys] != dict2[keys]:
#             compared_data[keys]=abs(dict1[keys] - dict2[keys])
#     return compared_data


# user_handle = "@BrandWithTim"
# celebrity_handle = "@DidoOfficial"
#
# user_results = analyze(user_handle)
# celebrity_results = analyze(celebrity_handle)
#
# user = flatten(user_results)
# celeb = flatten(celebrity_results)
#
# compared_results = compare(user, celeb)
#
# sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))
#
# for keys, value in sorted_result[:5]:
#   print keys,
#   print (user[keys]),
#   print ('=>'),
#   print (celebrity[keys]),
#   print ('=>'),
#   print (compared_results[keys])
#
# print sorted_result
