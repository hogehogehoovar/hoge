def get_alphabet(n)
  ('a'[0].ord + n).chr
end

50.times do |num|
  User.create!(email: "test#{num}@gmail.com", password: '000000', name: Faker::Pokemon.name, job: get_alphabet(Faker::Number.between(1, 10)), university: get_alphabet(Faker::Number.between(1, 10)), gender: Faker::Number.between(0, 1), birthday: Faker::Date.birthday(18, 35) )
end
