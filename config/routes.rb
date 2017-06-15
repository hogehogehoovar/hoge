Rails.application.routes.draw do
  devise_for :users
  root 'events#index'
  resources :events, only: :index do
    collection do
      post :search
    end
  end
end
