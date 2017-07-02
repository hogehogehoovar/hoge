Rails.application.routes.draw do
  devise_for :users
  root 'events#index'
  resources :events, only: :show do
    collection do
      post :search
    end
    resources :event_users, only: :create
    resources :groups, only: [:index, :show, :create] do
      resources :group_users, only: [] do
        collection do
          get :attend
        end
      end
    end
  end
end
