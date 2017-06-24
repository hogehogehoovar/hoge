class GroupsController < ApplicationController
  def show
    @group = Group.find(params[:id])
    @event = Event.find(params[:event_id])
    @restaurant = @group.restaurant
    @facility = @event.facility

    @hash = Gmaps4rails.build_markers(@facility) do |facility, marker|
      marker.lat facility.latitude
      marker.lng facility.longitude
      marker.infowindow facility.name
    end
  end

  def create
    event = Event.find(params[:event_id])
    group = Group.new
    group.event = event
    group.users = event.users
    group.restaurant = Restaurant.first # ToDo ここの処理を書く

    # Python連携のサンプルコード
    RubyPython.start(:python_exe => "python2.7")
    dir = Rails.root.join('sandbox').to_s
    sys = RubyPython.import 'sys'
    sys.path.append File.join(dir)
    called_ruby = RubyPython.import("called_ruby")
    called_ruby.print_python
    called_ruby.print_python_with_argument!( arg1: event.id )
    RubyPython.stop

    if group.save
      redirect_to event_group_path(event, group)
    else
      redirect_to event_path(event)
    end
  end
end
