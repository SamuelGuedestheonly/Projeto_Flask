from dao.db_cofig import get_connection

class TurmaDAO:
    sqlSelect="select turma.id,turma.semestre,curso.nome_curso,professor.nome,professor.disciplina from turma join curso on curso.id=turma.curso_id join professor on professor.id=turma.professor_id"
    
    def listar(self):
        conn = get_connection()
            
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
            
        lista = cursor.fetchall()
        
        return lista

    def salvar(self, id, semestre, curso_id, professor_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO turma (semestre, curso_id, professor_id) VALUES (%s, %s, %s)',
                (semestre, curso_id, professor_id)
            )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()

