import os

TEMPLATE_FILE = 'template.html' # 템플릿 파일
CONTENT_FILES = ['home.html', 'cv.html', 'research.html', 'coursework.html', 'essay.html'] # 내용을 채울 HTML 파일 목록
OUTPUT_DIR = 'output'  # 결과물이 저장될 폴더
PLACEHOLDER = '{{content}}' # 템플릿에서 교체될 특수 문자열

def generate_pages():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    try:
        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"FileNotFoundError: '{TEMPLATE_FILE}'")
        return

    for content_file in CONTENT_FILES:
        try:
            with open(content_file, 'r', encoding='utf-8') as f:
                page_content = f.read()

            final_html = template_content.replace(PLACEHOLDER, page_content)
            if content_file == 'home.html':
                final_html = final_html.replace('{isHome}', 'bg-gray-200 ')
            if content_file == 'cv.html':
                final_html = final_html.replace('{isCV}', 'bg-gray-200 ')
            if content_file == 'research.html':
                final_html = final_html.replace('{isResearch}', 'bg-gray-200 ')
            if content_file == 'coursework.html':
                final_html = final_html.replace('{isCoursework}', 'bg-gray-200 ')
            if content_file == 'essay.html':
                final_html = final_html.replace('{isEssay}', 'bg-gray-200 ')
                
            output_filename = os.path.basename(content_file)
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_html)

            print(f"'{output_path}' 파일이 생성되었습니다.")

        except FileNotFoundError:
            print(f"FileNotFoundError: '{content_file}'")
        except Exception as e:
            print(f"'{e}': {content_file}")

if __name__ == '__main__':
    generate_pages()