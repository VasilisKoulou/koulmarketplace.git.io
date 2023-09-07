from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProductSerializer
from projects.models import Product, Review, Tag

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/products'},
        {'GET':'/api/products/id'},
        {'POST':'/api/products/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},

    ]
    

    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def productVote(request, pk):
    product = Product.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner= user,
        product = product, 
    )
    review.value = data['value']
    review.save()
    product.getVoteCount

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    productId = request.data['product']

    product = Product.objects.get(id=productId)
    tag = Tag.objects.get(id=tagId)

    product.tags.remove(tag)

    return Response('Category was deleted')
