from dao.db_cofig import get_connection

class CursoDAO:
    sqlSelect="SELECT id, nome_curso, duracao FROM curso"
    
    def listar(self):
        conn = get_connection()
            
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
            
        lista = cursor.fetchall()
        
        return lista

    def salvar(self, id, nome_curso, duracao):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO curso (nome_curso, "duracao") VALUES (%s, %s)',
                (nome_curso, duracao)
            )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
