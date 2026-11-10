
from dao.db_cofig import get_connection


class MatriculaDAO:

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT
                m.id,
                a.nome,
                c.nome_curso,
                t.semestre,
                p.nome,
                p.disciplina
            FROM matricula m
            JOIN aluno a ON m.aluno_id = a.id
            JOIN curso c ON m.curso_id = c.id
            JOIN turma t ON m.turma_id = t.id
            JOIN professor p ON t.professor_id = p.id
            ORDER BY m.id
        """

        cursor.execute(sql)
        lista = cursor.fetchall()

        cursor.close()
        conn.close()

        return lista

    def listar_alunos(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome FROM aluno ORDER BY nome")
        lista = cursor.fetchall()

        cursor.close()
        conn.close()

        return lista

    def listar_cursos(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, nome_curso FROM curso ORDER BY nome_curso"
        )
        lista = cursor.fetchall()

        cursor.close()
        conn.close()

        return lista

    def listar_turmas(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, semestre
            FROM turma
            ORDER BY semestre
        """)

        lista = cursor.fetchall()

        cursor.close()
        conn.close()

        return lista

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, aluno_id, curso_id, turma_id
            FROM matricula
            WHERE id = %s
        """, (id,))

        matricula = cursor.fetchone()

        cursor.close()
        conn.close()

        return matricula

    def salvar(self, id, aluno_id, curso_id, turma_id):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if id:
                cursor.execute("""
                    UPDATE matricula
                    SET aluno_id = %s,
                        curso_id = %s,
                        turma_id = %s
                    WHERE id = %s
                """, (aluno_id, curso_id, turma_id, id))
            else:
                cursor.execute("""
                    INSERT INTO matricula
                    (aluno_id, curso_id, turma_id)
                    VALUES (%s, %s, %s)
                """, (aluno_id, curso_id, turma_id))

            conn.commit()

            return {"status": "ok"}

        except Exception as erro:
            conn.rollback()
            return {
                "status": "erro",
                "mensagem": str(erro)
            }

        finally:
            cursor.close()
            conn.close()

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM matricula WHERE id = %s",
                (id,)
            )

            conn.commit()

            return {"status": "ok"}

        except Exception as erro:
            conn.rollback()
            return {
                "status": "erro",
                "mensagem": str(erro)
            }

        finally:
            cursor.close()
            conn.close()
