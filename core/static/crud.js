(function(){
    var crud_mod = angular.module('crud', ['fast_ajax', 'ngResource']);
    crud_mod.directive('clientCrud', function(){
        return {
            restrict: 'E',
            replace: true,
            scope: {
            },
            templateUrl: '/static/client-crud.html',
            controller: function($scope, FAjax){
                var m = $scope.m = {
                    new_client: {}
                };
                angular.extend(m,{
                    criar_novo_usuario: criar_novo_usuario,
                    reset_novo_usuario: reset_novo_usuario,
                    editar_usuario: editar_usuario,
                    deletar_usuario: deletar_usuario,
                    comecar_edicao: comecar_edicao,
                    cancelar_edicao: cancelar_edicao
                });
                m.loading_clients = true;
                FAjax.get('/core/clients').success(function(response){
                    m.clients = response;
                }).finally(function(){
                    m.loading_clients = false;
                });
                function criar_novo_usuario(){
                    m.criando_client = true;
                    FAjax.post('/core/clients/', m.new_client).then(function(response){
                        m.clients.push(response.data);
                        reset_novo_usuario();
                        m.criando_client = false;
                    }, function(){
                        alert('Erro ao salvar usuário');
                    });
                }
                function reset_novo_usuario(){
                    m.new_client = {};
                    m.mostrar_form = false;
                }
                function editar_usuario(client){
                    client.salvando_edicao = true;
                    FAjax.update('/core/clients/' + client.pk, {name: client._name, email: client._email, phone: client._phone}).success(function(response){
                        angular.extend(client, response);
                    }).finally(function(){
                        client.salvando_edicao = false;
                        client.is_editing = false;
                    });
                }
                function deletar_usuario(client){
                    FAjax.delete('/core/clients/' + client.pk).success(function(response){
                        var client_index = m.clients.map(function(clt){
                            return clt.pk;
                        }).indexOf(client.pk);
                        if (client_index !== -1){
                            m.clients.splice(client_index, 1);
                        }
                    }).error(function(){
                        alert('Erro ao deletar usuário');
                    });
                }
                function comecar_edicao(client){
                    client._name = client.name;
                    client._email = client.email;
                    client._phone =  client.phone;
                    client.is_editing = true;
                }
                function cancelar_edicao(client){
                    client._name = client.name;
                    client._email = client.email;
                    client._phone =  client.phone;
                    client.is_editing = false;
                }
            }
        }
    });
})();