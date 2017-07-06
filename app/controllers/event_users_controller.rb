class EventUsersController < ApplicationController
  # Deviseのデフォルトの設定で、ログイン後はログイン画面遷移前のビューに飛ぶ
  before_action :authenticate_user!

  def create
    event = Event.find(params[:event_id])

    event_user = EventUser.find_by( { event_id: event.id, user_id: current_user.id } )
    if event_user.nil?
      EventUser.create( { event_id: event.id, user_id: current_user.id } )

      dir = Rails.root.join('sandbox').to_s
      result = system("python #{dir}/create_groups.py #{event.id}  #{current_user.id}")
      puts "cannot connect to python" if not result
    end

    group = Group.search_by_user_and_event(current_user.id, event.id)
    redirect_to event_group_path(event, group)
  end
end
