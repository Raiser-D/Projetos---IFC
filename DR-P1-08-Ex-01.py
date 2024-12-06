class Pessoa:
    def __init__(self, nome, sobrenome, endereco, segm_ensino, turma, user, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.segm_ensino = segm_ensino
        self.turma = turma
        self.user = user
        self.email = email
        self.__senha = senha
        self.ativo = True  # Indica se a pessoa está ativa no sistema

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
        #permitindo acessar e editar a senha

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, endereco, segm_ensino, turma, user, email, senha, filiacao, email_resp, RA, curso):
        super().__init__(nome, sobrenome, endereco, segm_ensino, turma, user, email, senha)
        self.filiacao = filiacao
        self.email_resp = email_resp
        self.RA = RA
        self.curso = curso
        self.ativo = True
        #criando a classe aluno e herdando atributos da classe pessoa

    def tranferencia(self):
        trocar_curso = input("Mudar de curso? 1 - Sim / 2 - Não: ")
        #pergunta se o aluno quer trocar de curso
        if trocar_curso == '1':
            if self.segm_ensino == '1' or self.segm_ensino == 'Ensino Médio':
                self.curso = input("Para qual curso do Ensino Médio deseja trocar? 1 - Informática / 2 - Eletromecânica / 3 - Mecatrônica: ")
                if self.curso == '1':
                    self.curso = "Informática"
                elif self.curso == '2':
                    self.curso = "Eletromecênica"
                elif self.curso == '3':
                    self.curso = "Mecatrônica"
                else:
                    print("Opção inválida. Selecione 1, 2 ou 3.")
                print(f"Curso alterado com sucesso. Agora você está matriculado em {self.curso}")
                #se ele quiser e digitar 1, em e 1, sim, pergunta para qual curso quer trocar

            elif self.segm_ensino == '2' or self.segm_ensino == 'Ensino Superior':
                if self.curso != '3':
                    curso_transf = input("Para qual curso do Ensino Superior deseja trocar? 1 - BCC / 2 - Pedagogia: ")
                    #se ele quiser e digitar 2, es e 1, sim, pergunta para qual curso quer trocar
                    if curso_transf != self.curso:
                        self.curso = curso_transf #Faz a verificação para saber se o aluno escolheu um curso diferente do seu
                        print(f"Curso alterado com sucesso. Agora você está matriculado em {'BCC' if self.curso == '1' else 'Pedagogia'}")
                    else:
                        print("Você já está no curso selecionado, se realmente deseja se tranferir responda novamente: ")
                        curso_transf = input("1 - BCC / 2 - Pedagogia: ")
                        #caso digite o mesmo curso que está, verificação, pergunta novamente
                        if curso_transf != self.curso:
                            self.curso = curso_transf
                            print(f"Curso alterado com sucesso. Agora você está matriculado em {'BCC' if self.curso == '1' else 'Pedagogia'}")
                        else:
                            print(f"Você manteve sua matrícula no curso {'BCC' if self.curso == '1' else 'Pedagogia'}")
                else:
                    print("Você está matriculado nos dois cursos do Ensino Superior, não há como fazer transferência.")
                    #confirmação
        elif trocar_curso == '2':
            if self.segm_ensino == '1':
                self.segm_ensino = "Ensino Médio"
                if self.curso == '1': self.curso = "Informática"
                elif self.curso == '2': self.curso = "Eletromecânica"
                else: self.curso = "Mecatrônica"
            else:
                self.segm_ensino = "Ensino Superior"
                if self.curso == '1': self.curso = "BCC"
                elif self.curso == '2': self.curso = "Pedagogia"
            print(f"Você manteve sua matrícula no curso {self.curso} do {self.segm_ensino}")
        
    def editar_dados(self, RA):
        aluno_encontrado = None
        for aluno in obj_turma.alunos:
            if obj_aluno.RA == RA:
                aluno_encontrado = obj_aluno
                break  # Interrompe o loop ao encontrar o aluno

        if aluno_encontrado:
            print(f"\n--- Editar dados do aluno {aluno_encontrado.nome} {aluno_encontrado.sobrenome} ---")
            aluno_encontrado.nome = input(f"Nome atual: {aluno_encontrado.nome} \n Insira o novo nome (Enter para manter): ") or aluno_encontrado.nome
            aluno_encontrado.sobrenome = input(f"Sobrenome atual: {aluno_encontrado.sobrenome} \n Insira o novo sobrenome (Enter para manter): ") or aluno_encontrado.sobrenome
            aluno_encontrado.turma = input(f"Turma atual: {aluno_encontrado.turma} \n Insira a nova turma (Enter para manter): ") or aluno_encontrado.turma
            aluno_encontrado.user = input(f"Nome de usuário atual: {aluno_encontrado.user} \n Insira o novo nome de usuário (Enter para manter): ") or aluno_encontrado.user
            aluno_encontrado.endereco = input(f"Endereço atual: {aluno_encontrado.endereco} \n Insira o novo endereço (Enter para manter): ") or aluno_encontrado.endereco
            aluno_encontrado.email = input(f"E-mail atual: {aluno_encontrado.email} \n Insira o novo e-mail (Enter para manter): ") or aluno_encontrado.email
            nova_senha = input("Insira uma nova senha (Enter para manter a atual): ")
            if nova_senha:
                aluno_encontrado.senha = nova_senha
            print("-"*21)
            print("Dados do aluno atualizados com sucesso!")
        else:
            print("-"*21)
            print("Aluno não encontrado.")

class Professor(Pessoa):
    def __init__(self, nome, sobrenome, endereco, segm_ensino, turma, user, email, senha, cpf, formacao, disciplina):
        super().__init__(nome, sobrenome, endereco, segm_ensino, turma, user, email, senha)
        self.__cpf = cpf
        self.formacao = formacao
        self.disciplina = disciplina
        self.ativo = True

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf
        #permitindo acessar e editar cpf

    def editar_dados(self, cpf):
        professor_encontrado = None
        for professor in obj_turma.lista_profs:
            if obj_professor.__cpf == cpf:
                professor_encontrado = obj_professor
                break  # Interrompe o loop ao encontrar o professor

        if professor_encontrado:
            print(f"\n--- Editar dados do professor {professor_encontrado.nome} {professor_encontrado.sobrenome} ---")
            professor_encontrado.nome = input(f"Nome atual: {professor_encontrado.nome} \n Insira o novo nome (Enter para manter): ") or professor_encontrado.nome
            professor_encontrado.sobrenome = input(f"Sobrenome atual: {professor_encontrado.sobrenome} \n Insira o novo sobrenome (Enter para manter): ") or professor_encontrado.sobrenome
            professor_encontrado.turma = input(f"Turma atual: {professor_encontrado.turma} \n Insira a nova turma (Enter para manter): ") or professor_encontrado.turma
            professor_encontrado.user = input(f"Nome de usuário atual: {professor_encontrado.user} \n Insira o novo nome de usuário (Enter para manter): ") or professor_encontrado.user
            professor_encontrado.endereco = input(f"Endereço atual: {professor_encontrado.endereco} \n Insira o novo endereço (Enter para manter): ") or professor_encontrado.endereco
            professor_encontrado.email = input(f"E-mail atual: {professor_encontrado.email} \n Insira o novo e-mail (Enter para manter): ") or professor_encontrado.email
            nova_senha = input("Insira uma nova senha (Enter para manter a atual): ")
            if nova_senha:
                professor_encontrado.senha = nova_senha
            professor_encontrado.formacao = input(f"Formação atual: {professor_encontrado.formacao} \n Insira a nova formação do professor (Enter para manter): ") or professor_encontrado.formacao
            professor_encontrado.disciplina = input(f"Disciplina atual: {professor_encontrado.endereco} \n Insira a nova disciplina que lecionará (Enter para manter): ") or professor_encontrado.disciplina
            print("-"*22)
            print("Dados do professor atualizados com sucesso!")
        else:
            print("-"*22)
            print("Professor não encontrado.")

class Disciplina:
    def __init__(self, id, descricao, segm_ensino):
        self.id = id
        self.descricao = descricao
        self.segm_ensino = segm_ensino
        self.prof_titular = []  # Professor titular da disciplina, None para verificar depois se já há professor na disciplina
        self.ativo = True

    def editar_disciplina(self):
        for disciplina in obj_turma.disciplinas:
            if disciplina.id == id:
                print(f"\n--- Editar disciplina {disciplina.id} - {disciplina.descricao} ---")
                disciplina.descricao = input(f"Descrição atual da disciplina: {disciplina.descricao} \n Insira a nova descrição (Enter para manter): ") or disciplina.descricao
                disciplina.segm_ensino = input(f"Segmento atual: {disciplina.segm_ensino} \n Insira o novo segmento de ensino (Enter para manter): ") or disciplina.segm_ensino
                print("-"*22)
                print("Disciplina atualizada com sucesso!")

    def adicionar_professor(self, obj_professor):
        self.prof_titular.append(obj_professor)

class Turma:
    def __init__(self, nome_turma, segm_ensino, curso, ano):
        self.nome_turma = nome_turma
        self.segm_ensino = segm_ensino  # Ensino Médio ou Superior
        self.curso = curso
        self.ano = ano
        self.alunos = []
        self.lista_profs = []
        self.disciplinas = []
        self.ativo = True

    def adicionar_aluno(self, obj_aluno):
        self.alunos.append(obj_aluno) # Adiciona uma instância da classe Aluno dentro da lista alunos

    def desativar_aluno(self, RA):
        for self.aluno in self.alunos:
            if obj_aluno.RA == RA:
                obj_aluno.ativo = False
                print(f"Aluno {obj_aluno.nome} {obj_aluno.sobrenome} foi desativado.")
                return
        print("Aluno não encontrado.")

    def excluir_aluno(self, RA):
        for aluno in self.alunos:
            if obj_aluno.RA == RA:
                self.alunos.remove(obj_aluno)
                print(f"Aluno {obj_aluno.nome} {obj_aluno.sobrenome} foi excluído da turma.")
                return
        print("Aluno não encontrado.")

############################################## FIM FUNÇÕES ALUNO

    def desativar_professor(self, cpf):
        for professor in self.lista_profs:
            if professor.cpf == cpf:
                professor.ativo = False
                print(f"Professor {professor.nome} {professor.sobrenome} foi desativado.")
                return
        print("Professor não encontrado.")

    def excluir_professor(self, cpf):
        for professor in self.lista_profs:
            if professor.cpf == cpf:
                if professor in obj_disciplina.prof_titular: # Garante que o código tentará excluir um professor da disciplina só se houver
                    obj_disciplina.prof_titular.remove(professor)
                self.lista_profs.remove(professor)
                
                print(f"Professor {obj_professor.nome} {obj_professor.sobrenome} foi excluído da turma.")
                return
        print("Professor não encontrado.")

############################################## FIM FUNÇÕES PROFESSOR

    def adicionar_disciplina(self, obj_disciplina, obj_professor):
        self.disciplinas.append(obj_disciplina)
        #print(f"Disciplina {obj_disciplina.descricao} adicionada à turma {self.nome_turma}.")
        # Adicionar professor no momento que insere a disciplina
        self.lista_profs.append(obj_professor)

    def desativar_disciplina(self, id):
        for disciplina in self.disciplinas:
            if disciplina.id == id:
                obj_disciplina.ativo = False
                print(f"A disciplina {disciplina.descricao} foi desativada.")
                return
        print("Disciplina não encontrada.")
    
    def excluir_disciplina(self, id):
        for disciplina in self.disciplinas:
            if disciplina.id == id:
                self.disciplinas.remove(obj_disciplina)
                print(f"A disciplina {disciplina.descricao} foi excluída.")
                return
        print("Disciplina não encontrada.")

############################################## FIM FUNÇÕES DISCIPLINA

    def criar_turma(self, nome_turma, segm_ensino, curso, ano):
        # Variáveis que servirão como contador dos alunos em um segmento
        alunos_EM = 0
        alunos_ES = 0

        for aluno in self.alunos:
            if aluno.segm_ensino == '1':  # Ensino Médio
                alunos_EM += 1
            elif aluno.segm_ensino == '2':  # Ensino Superior
                alunos_ES += 1

        # Lista para turmas criadas
        turmas = []

        # Verificar condições para criar turmas
        if segm_ensino == '1' or segm_ensino == 'Ensino Médio':
            if alunos_EM >= 1:
                turma_EM = Turma(nome_turma, segm_ensino, curso, ano)
                turmas.append(turma_EM)
                for turma in turmas:
                    print("-"*21)
                    print(f"Turma {turma.nome_turma} do {turma.segm_ensino} criada com sucesso!")
            else:
                print("Não é possível criar turma de Ensino Médio (mínimo: 20 alunos).")
    
        elif segm_ensino == '2' or segm_ensino == 'Ensino Superior':
            if alunos_ES >= 2:
                turma_ES = Turma(nome_turma, segm_ensino, curso, ano)
                turmas.append(turma_ES)
                for turma in turmas:
                    print(f"Turma {turma.nome_turma} do {turma.segm_ensino} criada com sucesso!")
            else:
                print("Não é possível criar turma de Ensino Superior (mínimo: 5 alunos).")
        return turmas

    def editar_turma(self):
        for turma in turmas:
            if turma.nome_turma == nome_turma:
                print(f"\n--- Editar turma {turma.nome_turma} - {turma.curso} - {turma.segm_ensino} ---")
                turma.nome_turma = input(f"Nome atual da turma: {turma.nome_turma} \n Insira o novo nome à turma (Enter para manter): ") or turma.nome_turma
                turma.segm_ensino = input(f"Segmento atual: {turma.segm_ensino} \n Insira o novo segmento de ensino (Enter para manter): ") or turma.segm_ensino
                turma.curso = input(f"Curso atual da turma: {turma.curso} \n Insira o novo curso da turma (Enter para manter): ") or turma.curso
                turma.ano = input(f"Ano atual da turma: {turma.ano} \n Insira o novo ano que a turma iniciará (Enter para manter): ") or turma.ano
            else:
                print("Turma não encontrada.")

    def desativar_turma(self):
        for turma in turmas:
            if turma.nome_turma == nome_turma:
                obj_turma.ativo = False
                print(f"A turma {turma.nome_turma} foi desativada.")
                return
            else:
                print("Turma não encontrada.")
    
    def excluir_turma(self):
        for turma in turmas:
            if turma.nome_turma == nome_turma:
                turmas.remove(turma)
                print(f"A turma {turma.nome_turma} foi excluída.")
                return
        print("Turma não encontrada.")

    def imprimir_turma(self):
        for turma in turmas:
            if turma.nome_turma == nome_turma:
                print(f"\n--- Detalhes da Turma {turma.nome_turma} ---")
                print(f"Segmento de Ensino: {'Ensino Médio' if turma.segm_ensino == '1' or turma.segm_ensino == 'Ensino Médio' else 'Ensino Superior'}")
                print(f"Curso: {turma.curso}")
                print(f"Ano de Início: {turma.ano}")

                print("\n--- Professores ---")
                for professor in self.lista_profs:  # Itera diretamente sobre os objetos em self.lista_profs
                    status = "Ativo" if professor.ativo else "Desativado"
                    print(f"Nome: {professor.nome} {professor.sobrenome} - Disciplina: {professor.disciplina} ({status})")

                print("\n--- Alunos ---")
                for aluno in self.alunos:  # Itera diretamente sobre os objetos em self.alunos
                    status = "Ativo" if aluno.ativo else "Desativado"
                    print(f"Nome: {aluno.nome} {aluno.sobrenome} - RA: {aluno.RA} - Curso: {aluno.curso} ({status})")

                print("\n--- Disciplinas ---")
                for disciplina in self.disciplinas:  # Itera diretamente sobre os objetos em self.disciplinas
                    print(f"ID: {disciplina.id} - Descrição: {disciplina.descricao}")

# Criação dos objetos com valores temporários
obj_turma = Turma("Nome", "Ensino Médio", "Informática", "2010") 
obj_aluno = Aluno("nome", "sobrenome", "endereco", "segm_ensino", "turma", "user", "email", "senha", "filiacao", "email_resp", "RA", "curso")
obj_disciplina = Disciplina("id", "descricao", "segm_ensino")

solicitar = ''
while True:
    print("------- AÇÕES -------")
    try:
        solicitar = input('''
1 - Cadastrar aluno
2 - Editar aluno
3 - Realizar transferência
4 - Desativar aluno
5 - Excluir aluno
6 - Cadastrar professor
7 - Editar professor
8 - Desativar professor
9 - Excluir professor
10 - Adicionar disciplina
11 - Editar disciplina
12 - Desativar disciplina
13 - Excluir disciplina
14 - Criar turma
15 - Editar turma
16 - Desativar turma
17 - Excluir turma
18 - Imprimir turma
19 - Finalizar programa
Digite o número referente à sua escolha: ''')
        if solicitar == '1':
            print("-"*21)
            print("---- Cadastrar aluno ----")
            nome = input("Insira o nome do aluno: ")
            sobrenome = input("Insira o sobrenome do aluno: ")
            endereco = input("Insira o endereço do aluno: ")
            segm_ensino = input("Insira o número do segmento que o aluno seguirá: \n1 - Ensino Médio \n2 - Ensino Superior: ")
            turma = input("Insira a turma que o aluno entrará: ")
            user = input("Insira o nome de usuário do aluno: ")
            email = input("Insira o e-mail do aluno: ")
            senha = input("Insira a senha do aluno: ")
            filiacao = input("Insira o nome do responsável legal pelo aluno: ")
            email_resp = input("Insira o e-mail do responsável: ")
            RA = input("Insira o número do Registro Acadêmico do aluno: ")
            if segm_ensino == '1':
                curso = input("Insira o número do curso que o aluno seguirá: \n1 - Informática \n2 - Eletromecânica \n3 - Mecatrônica: ")
                if curso == '1':
                    curso = 'Informática'
                elif curso == '2':
                    curso = 'Eletromecânica'
                else:
                    curso = 'Mecatrônica'
            else:
                curso = input("Insira o número do curso que o aluno seguirá: \n1 - Bacharel em Ciências da Computação \n 2 - Bacharel em Pedagogia: ")
                if curso == '1':
                    curso = 'Bacharel em Ciências da Computação'
                else:
                    curso = 'Bacharel em Pedagogia'

            obj_aluno = Aluno(nome, sobrenome, endereco, segm_ensino, turma, user, email, senha, filiacao, email_resp, RA, curso) 
            obj_turma.adicionar_aluno(obj_aluno)
            print("-"*21)
            print("Aluno cadastrado com sucesso!")
        
        elif solicitar == '2': # Editar Aluno
            print("-"*21)
            print("---- Editar Aluno ----")
            RA = input("Insira o RA do aluno que deseja editar: ")
            for aluno in obj_turma.alunos: # Irá passar por toda a lista e se encontrar o obj com tal RA irá chamar a função de editar
                if obj_aluno.RA == RA:
                    obj_aluno.editar_dados(RA)
                    break
                else:
                    print("-"*21)
                    print("Aluno não encontrado.")

        elif solicitar == '3': # Transferência aluno
            print("-"*21)
            print("---- Realizar transferência de aluno ----")
            RA = input("Insira o RA do aluno que deseja transferir: ")
            for aluno in obj_turma.alunos: # Irá passar por toda a lista e se encontrar o obj com tal RA irá chamar a função de editar
                if obj_aluno.RA == RA:
                    obj_aluno.tranferencia()
                    break
                else:
                    print("-"*21)
                    print("Aluno não encontrado.")
        
        elif solicitar == '4': # Desativar aluno
            print("-"*21)
            print("---- Desativar aluno ----")
            RA = input("Insira o RA do aluno que deseja desativar: ")
            for aluno in obj_turma.alunos: 
                if obj_aluno.RA == RA:
                    obj_turma.desativar_aluno(RA) # Dentro da função, RA será usado como identificador do aluno
                    break
                else:
                    print("-"*21)
                    print("Aluno não encontrado.")

        elif solicitar == '5': # Excluir aluno
            print("-"*21)
            print("---- Excluir aluno ----")
            RA = input("Insira o RA do aluno que deseja excluir: ")
            for aluno in obj_turma.alunos:
                if obj_aluno.RA == RA:
                    obj_turma.excluir_aluno(RA)
                    break
                else:
                    print("-"*21)
                    print("Aluno não encontrado.")
        
        elif solicitar == '6': # Cadastrar professor
            print("-"*21)
            print("---- Cadastrar professor ----")
            nome = input("Insira o nome do professor: ")
            sobrenome = input("Insira o sobrenome do professor: ")
            endereco = input("Insira o endereço do professor: ")
            segm_ensino = input("Insira o segmento de ensino que o professor lecionará: ")
            turma = input("Insira a turma que o professor será responsável: ")
            user = input("Insira o nome de usuário do professor: ")
            email = input("Insira o e-mail do professor: ")
            senha = input("Insira a senha do professor: ")
            cpf = input("Insira o CPF do professor: ")
            formacao = input("Insira o nível de formação do professor: ")
            disciplina = input("Insira qual disciplina o professor lecionará: ")

            obj_professor = Professor(nome, sobrenome, endereco, segm_ensino, turma, user, email, senha, cpf, formacao, disciplina)
            obj_disciplina.adicionar_professor(obj_professor)
            print("-"*21)
            print("Professor cadastrado com sucesso!")
        
        elif solicitar == '7': # Editar professor
            print("-"*21)
            print("---- Editar Professor ----")
            cpf = input("Insira o CPF do professor que deseja editar: ")
            for professor in obj_turma.lista_profs: # Mesmo funcionamento do aluno
                if obj_professor.cpf == cpf:
                    obj_professor.editar_dados(cpf)
                    break
            else:
                print("-"*21)
                print("Professor não encontrado.")
        
        elif solicitar == '8': # Desativar professor
            print("-"*21)
            print("---- Desativar professor ----")
            cpf = input("Insira o CPF do professor que deseja desativar: ")
            for professor in obj_turma.lista_profs:
                if obj_professor.cpf == cpf:
                    obj_turma.desativar_professor(cpf)
                    break
            else:
                print("-"*21)
                print("Professor não encontrado.")

        elif solicitar == '9': # Excluir professor
            print("-"*21)
            print("---- Excluir professor ----")
            cpf = input("Insira o CPF do professor que deseja excluir: ")
            for professor in obj_turma.lista_profs:
                if professor.cpf == cpf:
                    obj_turma.excluir_professor(cpf)
                    break
            else:
                print("-"*21)
                print("Professor não encontrado.")

        elif solicitar == '10': # Adicionar disciplina
            print("-"*21)
            print("---- Adicionar disciplina ----")
            id = input("Insira o ID referente à disciplina: ")
            descricao = input("Insira uma descrição da disciplina a ser criada: ")
            segm_ensino = input("Insira o segmento de ensino a qual esta pertence (Pode ser mais de um): ")
            prof_titular = input("Insira o nome do professor titular desta disciplina: ")

            try:
                # Verifica se o professor foi criado
                obj_professor  # Acessar diretamente; gerará NameError se não existir
                
                # Cria e adiciona a disciplina
                obj_disciplina = Disciplina(id, descricao, segm_ensino)
                obj_turma.adicionar_disciplina(obj_disciplina, obj_professor)
                print("-" * 21)
                print("Disciplina cadastrada com sucesso!")
            except NameError:
                print("-" * 21)
                print("Erro: Nenhum professor foi criado. Não é possível adicionar uma disciplina sem um professor.")

        elif solicitar == '11': # Editar disciplina
            print("-"*21)
            print("---- Editar disciplina ----")
            id = input("Insira o ID da disciplina que deseja editar: ")
            for disciplina in obj_turma.disciplinas:
                if obj_disciplina.id == id:
                    obj_disciplina.editar_disciplina()
                    break
            else:
                print("-"*21)
                print("Disciplina não encontrada.")

        elif solicitar == '12': # Desativar disciplina
            print("-"*21)
            print("---- Desativar disciplina ----")
            id = input("Insira o ID da disciplina que deseja desativar: ")
            obj_turma.desativar_disciplina(id)

        elif solicitar == '13': # Excluir disciplina
            print("-"*21)
            print("---- Excluir disciplina ----")
            id = input("Insira o ID da disciplina que deseja excluir: ")
            obj_turma.excluir_disciplina(id)
        
        elif solicitar == '14': # Criar turma
            print("-"*21)
            print("---- Criar turma ----")
            nome_turma = input("Insira o nome da turma: ")
            segm_ensino = input("Insira de qual segmento de ensino ela é (1 - Ensino Médio / 2 - Ensino Superior): ")
            if segm_ensino == '1':
                segm_ensino = 'Ensino Médio'
                curso = input("Insira de qual curso a turma é: \n1 - Informática \n2 - Eletromecânica \n3 - Mecatrônica: ")
                if curso == '1':
                    curso = 'Informática'
                elif curso == '2':
                    curso = 'Eletromecânica'
                else:
                    curso = 'Mecatrônica'
            elif segm_ensino == '2':
                segm_ensino = 'Ensino Superior'
                curso = input("Insira de qual curso a turma é: \n1 - Bacharel em Ciências da Computação \n2 - Bacharel em Pedagogia: ")
                if curso == '1':
                    curso = 'Bacharel em Ciências da Computação'
                else:
                    curso = 'Bacharel em Pedagogia'
            ano = input("Insira o ano de início da turma: ")

            # Chama o método criar_turma para gerar turmas com base nos alunos cadastrados
            turmas = obj_turma.criar_turma(nome_turma, segm_ensino, curso, ano)

        elif solicitar == '15': # Editar turma
            print("-"*21)
            print("---- Editar turma ----")
            nome_turma = input("Insira o nome da turma que deseja editar: ")
            for turma in turmas:
                if turma.nome_turma == nome_turma:
                    obj_turma.editar_turma()
                else:
                    print("-"*21)
                    print("Turma não encontrada.")

        elif solicitar == '16': # Desativar turma
            print("-"*21)
            print("---- Desativar turma ----")
            nome_turma = input("Insira o nome da turma que deseja desativar: ")
            obj_turma.desativar_turma()

        elif solicitar == '17': # Excluir turma
            print("-"*21)
            print("---- Excluir turma ----")
            nome_turma = input("Insira o nome da turma que deseja excluir: ")
            obj_turma.excluir_turma()

        elif solicitar == '18': # Imprimir turma
            print("-" * 21)
            segm_ensino = input("Insira o segmento de ensino da turma que deseja imprimir \n(Ensino Médio | Ensino Superior): ").upper()
            nome_turma = input("Insira o nome da turma: ")
            try:
                for turma in turmas:
                    if turma.nome_turma == nome_turma and turma.segm_ensino.upper() == segm_ensino:
                        obj_turma.imprimir_turma()
                        break
                    else:
                        print("-" * 21)
                        print("Turma não encontrada.")
            except NameError:
                print("-"*21)
                print("Erro: A lista 'turmas' não foi definida. Certifique-se de criar turmas antes de tentar imprimir.")      
        
        elif solicitar == '19': # Finalizar programa
            print("---- FINALIZANDO PROGRAMA ----")
            break

        else:
            raise ValueError("Opção inválida. Tente novamente.")
    except ValueError as e:
        print("-"*21)
        print(e)
