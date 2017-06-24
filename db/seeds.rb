10.times do |num|
  User.create!(email: "test#{num}@gmail.com", password: '000000', name: Faker::Pokemon.name)
end
