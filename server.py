import grpc
import messages_pb2_grpc as mess_grpc
from messages_pb2 import ProdCatReply, ProdReply
from shop_info import cat_arr
from shop_info import prod_arr
from concurrent import futures

class ShopServicer(mess_grpc.ShopServicer):
    def GetCateg(self, request, context):
        print(request.c)
        print(cat_arr)
        return ProdCatReply(cat=cat_arr[:request.c])
    
    def GetProd(self, request, context):
        for i in prod_arr:
            if i['category'] == request.category:
                return ProdReply(category=i['category'], prod_price=i['prod_price'])

def server_up():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mess_grpc.add_ShopServicer_to_server(ShopServicer(), server)
    server.add_insecure_port('[::]:40070')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    server_up()