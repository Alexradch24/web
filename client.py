import grpc
import messages_pb2_grpc as mess_grpc
from messages_pb2 import ProdCatRequest, ProdRequest

channel = grpc.insecure_channel('localhost:40070')
stub = mess_grpc.ShopStub(channel)

print(stub.GetCateg(ProdCatRequest(c=2)))
print(stub.GetProd(ProdRequest(category="Выпечка")))
