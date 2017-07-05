class EventUsersController < ApplicationController
  # Deviseのデフォルトの設定で、ログイン後はログイン画面遷移前のビューに飛ぶ
  before_action :authenticate_user!

  def create
    event = Event.find(params[:event_id])

    # ToDo Pythonに処理を飛ばすと、勝手にevent_user, group, group_userをつくってくれる。
    RubyPython.start(:python_exe => "python2.7")
    dir = Rails.root.join('sandbox').to_s
    sys = RubyPython.import 'sys'
    sys.path.append File.join(dir)
    called_ruby = RubyPython.import("called_ruby")
    called_ruby.print_python
    called_ruby.print_python_with_argument!( arg1: event.id, arg2: current_user.id )
    RubyPython.stop

    event_user = EventUser.find_or_create_by( { event_id: event.id, user_id: current_user.id } )
    group = Group.find_or_initialize_by( { event_id: event.id, restaurant_id: event.facility.restaurants.first.id } )
    GroupUser.find_or_create_by( { group_id: group.id, user_id: current_user.id } )
    redirect_to event_group_path(event, group)
  end
end
