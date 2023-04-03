select *
from people
where gender = 'girl'
  and age between 18 and 26
  and not exists(select *
                 from relationship
                 where (person_one = people.id or person_two = people.id) and type = 'romantic')
  and is_cute = true
  and is_crazy = false
  and has_small_waist = true
  and is_honest = true
  and is_white = true
  and is_funny = true
  and is_smart = true
  and is_intelligent = true
  and is_introverted = true
  and is_tomboyish = true
  and is_confident = true
  and is_kind = true
  and is_loyal = true
  and has_job = true
  and is_ambitious = true
  and has_empathy = true
  and has_sense_of_humor = true
  and has_common_sense = true
  and has_communication_skills = true
  and has_good_manners = true
  and has_similar_interests = true
  and is_emotionally_stable = true
  and is_emotionally_intelligent = true
  and is_trustworthy = true
  and has_stable_income = true
  and has_shared_values = true
  and is_fairly_attractive = true
  and is_fairly_white = true