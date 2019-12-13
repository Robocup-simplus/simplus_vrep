#include <iostream>
#include <memory>
#include <string>

#include <grpcpp/grpcpp.h>

#include "simplus.grpc.pb.h"
#include "player.cc"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using SimPlus::WorldInfo;
using SimPlus::ServerInfo;
using SimPlus::TeamInfo;
using SimPlus::Observations;
using SimPlus::Observation;
using SimPlus::Proximity;
using SimPlus::Position;
using SimPlus::Commands;
using SimPlus::Command;
using SimPlus::Ending;
using SimPlus::Result;
using SimPlus::Action;
using SimPlus::CheckPoint;
using SimPlus::Pixel;
using SimPlus::Image;
using simplus=SimPlus::SimPlus;


class Client final : public simplus::Service {

  Status Start(ServerContext* context, const WorldInfo* worldInfo,
                  TeamInfo* teamInfo) override {
    start(worldInfo,teamInfo);

    return Status::OK;
  }

  Status Action(ServerContext* context, const Observations* observations,
                  Commands* commands) override {
     int id=0;
     for (Observation observation:observations->robots()){
        Command* cmd=commands->add_commands();
        cmd->set_id(id);
        play(id, observations->server(), observation, cmd);
        id++;
     }
    return Status::OK;
  }
  
  Status End(ServerContext* context, const Ending* ending,
  			Result* result) override {
  			end(ending,result);
    return Status::OK;
  }  
};

void RunServer() {
  std::string server_address("localhost:50051");
  Client service;

  ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<Server> server(builder.BuildAndStart());
  std::cout << "Client listening on " << server_address << std::endl;
  server->Wait();
}

int main() {
RunServer();


  return 0;
}