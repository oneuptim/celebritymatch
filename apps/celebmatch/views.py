from django.shortcuts import render, redirect, HttpResponse
from models import Match
import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

def index(request):
    return render(request, 'celebmatch/index.html')



def process(request):
    # def analyze(handle):
    #
    #     twitter_consumer_key = 'k5pLmAB70ZsP54yqkGLVzq6Mc'
    #     twitter_consumer_secret = 'vRZMEIStHYoAgjBymoRrpiqVdWOfSGEJyaLnyNxNcISmZkGqpP'
    #     twitter_access_token = '1624965788-jgkGSqnJitOULMLlyS3WRhgMOwADsU0GN5yPsnw'
    #     twitter_access_secret = 'AsIC34EadILRS4G1NRdWAvqKq8VZzpQpZDZyFzLHsgbOV'
    #
    #     twitter_api_call = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)


        # handle = "@BrandWithTim"

        # statuses = twitter_api_call.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
        #
        # text = ""
        # for status in statuses:
            # if (status.lang == 'eng'):
            # text += status.text.encode('utf-8')


            # print text, "*"*300

        # pi_username = 'a70c7726-b66a-411e-869f-7e74987f39b8'
        # pi_password = '6rq8ConOjJGo'
        #
        # personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
        #
        # pi_results = personality_insights.profile(text)
        #
        # return pi_results

    # def flatten(orig):
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
    # def compare(dict1, dict2):
    #     compared_data = {}
    #     for keys in dict1:
    #         if dict1[keys] != dict2[keys]:
    #             compared_data[keys]=abs(dict1[keys] - dict2[keys])
    #     return compared_data
    #
    #
    # if request.method == 'POST':
    #     user_handle = request.POST['user']
    #     celebrity_handle = request.POST['celeb']

        # user_results = analyze(user_handle)
        # celebrity_results = analyze(celebrity_handle)
        #
        # user = flatten(user_results)
        # celeb = flatten(celebrity_results)
        #
        # compared_results = compare(user, celeb)
        #
        # sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

        # for keys, value in sorted_result[:5]:
        #   print keys,
        #   print (user[keys])
        #   print ('=>')
        #   print (celeb[keys])
        #   print ('=>')
        #   print (compared_results[keys])
        #   print "&"*20

        # print sorted_result, "#"*200

        # matchObject = Match.objects.create(match=sorted_result)
        # print type(matchObject), "*****************"
        # match_list = matchObject.match

        return redirect('/results')
        # return sorted_result
    # analyze, flatten, compare,



def results(request):
    def analyze(handle):

        twitter_consumer_key = 'k5pLmAB70ZsP54yqkGLVzq6Mc'
        twitter_consumer_secret = 'vRZMEIStHYoAgjBymoRrpiqVdWOfSGEJyaLnyNxNcISmZkGqpP'
        twitter_access_token = '1624965788-jgkGSqnJitOULMLlyS3WRhgMOwADsU0GN5yPsnw'
        twitter_access_secret = 'AsIC34EadILRS4G1NRdWAvqKq8VZzpQpZDZyFzLHsgbOV'

        twitter_api_call = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)


        # handle = "@BrandWithTim"

        statuses = twitter_api_call.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

        text = ""
        for status in statuses:
            # if (status.lang == 'eng'):
            text += status.text.encode('utf-8')


            # print text, "*"*300

        pi_username = 'a70c7726-b66a-411e-869f-7e74987f39b8'
        pi_password = '6rq8ConOjJGo'

        personality_insights = PersonalityInsights(username=pi_username, password=pi_password)

        pi_results = personality_insights.profile(text)

        return pi_results

    def flatten(orig):
      data = {}
      for c in orig['tree']['children']:
        if 'children' in c:
          for c2 in c['children']:
            if 'children' in c2:
              for c3 in c2['children']:
                if 'children' in c3:
                  for c4 in c3['children']:
                    if (c4['category'] == 'personality'):
                      data[c4['id']] = c4['percentage']
                      if 'children' not in c3:
                        if (c3['category'] == 'personality'):
                          data[c3['id']] = c3['percentage']
        return data

    def compare(dict1, dict2):
        compared_data = {}
        for keys in dict1:
            if dict1[keys] != dict2[keys]:
                compared_data[keys]=abs(dict1[keys] - dict2[keys])
        return compared_data


    if request.method == 'POST':
        user_handle = request.POST['user']
        celebrity_handle = request.POST['celeb']

        user_results = analyze(user_handle)
        celebrity_results = analyze(celebrity_handle)

        user = flatten(user_results)
        celeb = flatten(celebrity_results)

        compared_results = compare(user, celeb)

        sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

        for keys, value in sorted_result[:10]:
          print keys, (user[keys]) * 100,
          print ('=>'), (celeb[keys]) * 100,
          print ('=>'), (compared_results[keys]) * 100

    data = {
        'match': sorted_result,
        'keyzos': keys,
        'yuza': (user[keys]) * 100
        }

    return render(request, 'celebmatch/results.html', data)
