import requests
from bs4 import BeautifulSoup, NavigableString
import chromadb
from uuid import uuid4
import warnings
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning, module='torch.utils._pytree')

def get_clean_inner_texts(soup):
    """Extract clean inner texts from a BeautifulSoup object."""
    title = soup.title.string
    soup = soup.find('div', {'id': 'haru-content-main'})
    if soup is None:
        return []
    texts = ''
    for element in soup.find_all(True):  # Find all tags
        if element.name not in ['script', 'style']:  # Skip script and style tags
            if not element.find_all(True):  # Check if there are no child elements
                if isinstance(element, NavigableString):
                    continue
                text = element.get_text(strip=True)
                if text:  # Only add non-empty text
                    texts += text
    return texts, title

def get_inner_text_from_url(url):
    """Fetch inner text content and title from a URL."""
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    inner_texts, title = get_clean_inner_texts(soup)
    inner_texts = ''.join(inner_texts)
    inner_texts = inner_texts.replace(
        'JOIN US AND MAKE AWESOME THINGS THAT MATTER.Bạn đã sẵn sàng ứng tuyển chưa ?Môi trường năng động, sáng tạoNhiều sự kiệnNhiều chính sách đãi ngộSimilar JobsHà NộiĐà NẵngIT Comtor to BrSEWHO WE ARE Bạn là IT Comtor và có định hướng phát triển trở thành BrSE nhưng lại chưa có nhiều kiến thức cũng như kinh nghiệm trong lĩnh vực này? Ở Sun*, chúng tôi có giải pháp dành cho...Xem thêmApply for this Job******Attach*---HanoiDanangHochiminh*---Sun* HRSun* FacebookSun* LinkedinSun* EmailOther', '')
    inner_texts = inner_texts.replace('at Sun* Inc.', '')
    return inner_texts, title

# List of URLs to fetch
new_link=['https://sun-asterisk.vn/recruitment/technical-leader-fullstack-leader-english-fluency/',
 'https://sun-asterisk.vn/en/project/du-an-softbank-meetruck/',
 'https://sun-asterisk.vn/project/smart-league-saai/',
 'https://sun-asterisk.vn/recruitment-category/software-engineer/',
 'https://sun-asterisk.vn/en/project/du-an-uiza-nen-tang-ung-dung-dich-vu-dam-may-cho-video/',
 'https://sun-asterisk.vn/location/da-nang/',
 'https://sun-asterisk.vn/recruitment/brse/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-6/',
 'https://sun-asterisk.vn/recruitment/ai-engineer/',
 'https://sun-asterisk.vn/en/recruitment/management-accounting/',
 'https://sun-asterisk.vn/recruitment/general-affairs-hn/',
 'https://sun-asterisk.vn/du-an/',
 'https://sun-asterisk.vn/en/jobs/',
 'https://sun-asterisk.vn/recruitment/fresher-ai-engineer/',
 'https://sun-asterisk.vn/en/recruitment-category/brse-communicator-en/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-9/',
 'https://sun-asterisk.vn/en/jobs-en/',
 'https://sun-asterisk.vn/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-8/',
 'https://sun-asterisk.vn/en/project/du-an-tilani-nen-tang-ket-noi-matching-platform-hang-dau-tai-viet-nam-rudicaf/',
 'https://sun-asterisk.vn/en/project/du-an-cong-cu-ho-tro-ban-hang-tu-dong-va-toi-uu-hoa-loi-nhuan-cong-ty-tnhh-mazrica/',
 'https://sun-asterisk.vn/van-hoa-su-kien/',
 'https://sun-asterisk.vn/location/ha-noi/',
 'https://sun-asterisk.vn/recruitment/devops-engineer/',
 'https://sun-asterisk.vn/en/environment/',
 'https://sun-asterisk.vn/en/project/du-an-harutaka-2/',
 'https://sun-asterisk.vn/en/project/du-an-cfn-dien-dan-tim-kiem-viec-lam-song-ngu/',
 'https://sun-asterisk.vn/recruitment/qa-fresher-dinh-huong-lam-trainer/',
 'https://sun-asterisk.vn/en/creative-engineering-english/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-14/',
 'https://sun-asterisk.vn/recruitment/ai-intern/',
 'https://sun-asterisk.vn/en/project/du-an-kurashicom-2/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-16/',
 'https://sun-asterisk.vn/en/',
 'https://sun-asterisk.vn/recruitment-category/human-resources/',
 'https://sun-asterisk.vn/recruitment/reactjs-engineer-english-fluency/',
 'https://sun-asterisk.vn/project/du-an-kurashicom/',
 'https://sun-asterisk.vn/recruitment/nodejs-engineer-english-fluency/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-3/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-4/',
 'https://sun-asterisk.vn/recruitment/business-development/',
 'https://sun-asterisk.vn/en/project/du-an-money-forward/',
 'https://sun-asterisk.vn/recruitment-category/communications-marketing/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-12/',
 'https://sun-asterisk.vn/en/project/du-an-ssk/',
 'https://sun-asterisk.vn/location/ho-chi-minh/',
 'https://sun-asterisk.vn/recruitment/management-accounting-copy/',
 'https://sun-asterisk.vn/recruitment/it-comtor-to-brse/',
 'https://sun-asterisk.vn/chinh-sach-phuc-loi/',
 'https://sun-asterisk.vn/recruitment-category/management/',
 'https://sun-asterisk.vn/en/van-hoa-su-kien-english/',
 'https://sun-asterisk.vn/recruitment/japanese-teacher-dai-hoc-cong-nghe-thong-tin-dhqg-tp-hcm/',
 'https://sun-asterisk.vn/creative-engineering/',
 'https://sun-asterisk.vn/en/project/du-an-smart-league-saai/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-12',
 'https://sun-asterisk.vn/en/location/ha-noi-en/',
 'https://sun-asterisk.vn/en/recruitment/brse-2/',
 'https://sun-asterisk.vn/co-hoi-nghe-nghiep/',
 'https://sun-asterisk.vn/recruitment-category/intern-fresher/',
 'https://sun-asterisk.vn/en/location/da-nang-en/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-15/',
 'https://sun-asterisk.vn/recruitment/react-native-engineer-english-fluency/',
 'https://sun-asterisk.vn/recruitment-category/administration-support/',
 'https://sun-asterisk.vn/en/about-us/',
 'https://sun-asterisk.vn/en/project/du-an-globis-dich-vu-cung-cap-video-hoc-tap/',
 'https://sun-asterisk.vn/ve-chung-toi/',
 'https://sun-asterisk.vn/en/project/du-an-facy-website-kinh-doanh-thoi-trang-truc-tuyen/',
 'https://sun-asterisk.vn/recruitment/networkengineer/',
 'https://sun-asterisk.vn/en/project/du-an-dich-vu-tim-kiem-mat-bang-kinh-doanh-ctcp-tenanta/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-10/',
 'https://sun-asterisk.vn/recruitment/organization-design-executive/',
 'https://sun-asterisk.vn/recruitment-category/brse-communicator/',
 'https://sun-asterisk.vn/project/du-an-harutaka/',
 'https://sun-asterisk.vn/talent-platform/',
 'https://sun-asterisk.vn/en/talent-platform-english/',
 'https://sun-asterisk.vn/recruitment/project-manager-english-fluency/',
 'https://sun-asterisk.vn/recruitment/risk-management-executive-2/',
 'https://sun-asterisk.vn/recruitment/chuyenviendoingoaitiengnhatn2-hcm/',
 'https://sun-asterisk.vn/recruitment/chuyen-vien-iso/',
 'https://sun-asterisk.vn/recruitment-category/system-security/',
 'https://sun-asterisk.vn/en/project/du-an-kids-taxi/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-7/',
 'https://sun-asterisk.vn/en/project/du-an-sports-bull-kenh-tin-tuc-the-trao-truc-tuyen/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-11/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-13/',
 'https://sun-asterisk.vn/en/projects/',
 'https://sun-asterisk.vn/recruitment-category/education/',
 'https://sun-asterisk.vn/en/recruitment-category/administration-support-en/',
 'https://sun-asterisk.vn/project/giai-dau-thong-minh-saai-5/']
new_link = [i for i in new_link if '/en/' not in i]

# Extract content and titles
sources = []
contents = []
for i in new_link:
    content, source = get_inner_text_from_url(i)
    print(i)
    sources.append(source)
    contents.append(content)

# Generate unique IDs and metadata
ids = [str(uuid4()) for _ in range(len(contents))]
metadatas = [{'source': title} for title in sources]

# Initialize ChromaDB client
chroma_db = chromadb.PersistentClient(path="db")

# Define embedding function
embedding_fn = SentenceTransformerEmbeddingFunction(model_name='sentence-transformers/paraphrase-multilingual-mpnet-base-v2')

# Get or create ChromaDB collection
chroma_collection = chroma_db.get_or_create_collection("sun", embedding_function=embedding_fn)

# Add documents to the ChromaDB collection
chroma_collection.add(documents=contents, ids=ids, metadatas=metadatas)
