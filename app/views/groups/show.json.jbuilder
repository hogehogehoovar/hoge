json.array! @users do |user|
  json.id             user.id
  json.name           user.name
  json.age            user.age
  json.image          user.image
  json.job            user.job
  json.attend_group   user.attend_group?(@group.id)
end
