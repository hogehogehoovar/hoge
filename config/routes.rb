Rails.application.routes.draw do
  devise_for :users
  root 'tests#index'
end
