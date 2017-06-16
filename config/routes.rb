Rails.application.routes.draw do
  devise_for :users
  root 'events#index'
  resources :events, only: :show do
    collection do
      post :search
    end
  end
end
