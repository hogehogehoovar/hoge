class GroupsController < ApplicationController
  def index
  end

  def show
    @group = Group.find(params[:id])
    # includesが効いてないので、どうしてもN+1を避けたければsql直打ちでマージする
    @users = @group.users.includes(:group_users)
    # すでにattend=1になっているかの判定に使う
    @group_user = GroupUser.find_by(group_id: @group.id, user_id: current_user.id)
    @event = Event.find(params[:event_id])
    # 二次会の開始時刻をイベント終了時刻30分後にする
    @start_time = (@event.end_time+1800).strftime("%H時%M分")

    @restaurant = @group.restaurant
    @facility = @event.facility
    locations = [@restaurant, @facility]
    @hash = Gmaps4rails.build_markers(locations) do |location, marker|
      marker.lat location.latitude
      marker.lng location.longitude
      marker.infowindow location.name
    end
    respond_to do |format|
      format.html
      format.json
    end
  end
end
