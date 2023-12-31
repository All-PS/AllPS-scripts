from config.DatabaseConfig import DatabaseConfig
import openai
import re

class ProgrammersCategorizer:

    def __init__(self):
        self.dbConnection = DatabaseConfig().getConnection()

    def set_gpt_api(self, key):
        openai.api_key = key

    def request_gpt(self, correct_code):
        message = (correct_code +
                   " 위 코드를 1,dp 2,implementation 3,greedy 4,bruteforcing 5,string 6,backtracking 7,graph 8,two_pointer 9,tree 10,priority_queue 11,data_structure 12,shortest_path 13,prefix_sum 14,binary_search 15,precomputation 16,math 17,recursion 18,divide_and_conquer 19,sorting 20,topological_sorting 21,hashing 22,geometry 23,disjoint_set 24,mst 25,segment_tree 26,bitmasking 27,flow  "
                   "중에 해당하는 번호로 알려줘")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )

        return response.choices[0].message['content']

    def categorize(self):
        with self.dbConnection.cursor() as cursor:
            delete_query = """
                DELETE FROM problem_category
                WHERE problem_id IN (
                    SELECT * FROM (
                        SELECT p.id
                        FROM problem p
                            INNER JOIN problem_category pc ON p.id = pc.problem_id
                        WHERE p.platform_id = 3
                    ) AS subquery
                )
            """
        cursor.execute(delete_query)
        self.dbConnection.commit()
        print("All deleted.")

        select_query = """
                SELECT p.id, s.code
                FROM problem p
                INNER JOIN solution s ON p.id = s.problem_id
                WHERE p.platform_id = 3
            """

        cursor.execute(select_query)
        rows = cursor.fetchall()

        cnt = 0
        self.set_gpt_api("")

        for row in rows:
            category = self.request_gpt(row[1])

            # 정규 표현식을 사용하여 숫자와 카테고리 정보 추출
            match = re.search(r'(\d+),(\w+)', category)

            self.insert(cursor, row[0], match.group(1))

            cnt += 1
            if cnt % 1000 == 0:
                self.dbConnection.commit()
                print(f"{cnt} committed.")
            self.dbConnection.commit()

        print("All committed.")

    def insert(self, cursor, problem_id, category_id):
        insert_query = """
            INSERT INTO problem_category(problem_id, category_id)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE problem_id = problem_id;
        """
        cursor.execute(insert_query, (problem_id, category_id))
