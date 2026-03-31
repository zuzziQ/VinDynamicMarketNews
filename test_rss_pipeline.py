import sys
import io
import time
import feedparser
from bs4 import BeautifulSoup

import config  # Import cấu hình từ file config.py

# Fix unicode characters printing error on Windows terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Constants
BATCH_SIZE = 5

def clean_html(html_content):
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text(separator=" ", strip=True)

def filter_by_keywords(text):
    """
    Hàm kiểm tra xem bài viết có chứa bất kỳ Keywords nào hay không.
    Sử dụng Regex kết hợp Ignore Case (Bỏ qua viết hoa viết thường).
    """
    if not text:
        return False
    text = text.lower()
    for keyword in config.KEYWORDS:
        # Nếu từ khóa xuất hiện nguyên vẹn trong đoạn text
        if keyword.lower() in text:
            return True
    return False

def fetch_rss_feeds():
    print("[*] Bắt đầu cào dữ liệu từ danh sách RSS_FEEDS (Đã cấu hình)...")
    all_articles = []
    
    for url in config.RSS_FEEDS:
        print(f"  -> Fetching: {url}")
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                title = entry.get("title", "")
                summary_raw = entry.get("summary", "")
                summary_clean = clean_html(summary_raw)
                
                # Pre-filtering: Kiểm tra xem tiêu đề Hoặc phần tóm tắt có chứa Keywords không
                if filter_by_keywords(title) or filter_by_keywords(summary_clean):
                    all_articles.append({
                        "title": title,
                        "link": entry.link,
                        "published": entry.get("published", ""),
                        "summary": summary_clean,
                        "feed_source": url
                    })
        except Exception as e:
            print(f"  [!] Lỗi khi cào feed {url}: {e}")
            
    # Lọc trùng lặp bài báo (Dựa trên đường dẫn URL)
    unique_links = set()
    deduped_articles = []
    for article in all_articles:
        if article["link"] not in unique_links:
            unique_links.add(article["link"])
            deduped_articles.append(article)
            
    return deduped_articles

def mock_anthropic_call(batch_index, batch_data):
    """
    Gửi prompt chứa Analyst Persona và lô dữ liệu bản tin cho Claude API.
    """
    # Xây dựng Prompt (Trong thực tế đây là System Prompt trong payload API)
    system_prompt = config.ANALYST_PERSONA
    print(f"\n[>] [Gửi Batch {batch_index}] tới Claude 3.5 Sonnet... (Với System Prompt: VinDynamic Analyst)")
    
    # Giả lập độ trễ xử lý API
    time.sleep(2)
    print(f"[<] [Nhận Batch {batch_index}] Claude trả về Report JSON thành công.")
    
    return {
        "status": "success",
        "batch_index": batch_index,
        "articles_processed": len(batch_data),
        "insight_report": f"Thị trường Robotics Châu Á vừa có {len(batch_data)} bản tin nổi bật phân tích theo hệ quy chiếu VinDynamic."
    }

def process_in_batches(articles, mock=True):
    total_articles = len(articles)
    print(f"\n[*] Tổng số bài vượt qua Pre-filtering (Lọc TỪ KHÓA) cực gắt: {total_articles} bài báo.")
    
    if total_articles == 0:
        print("[!] Không có bài tin nào liên quan đến Robotics/Automation ngày hôm nay.")
        return []
        
    aggregated_results = []
    
    # Chia nhỏ lô báo
    for i in range(0, total_articles, BATCH_SIZE):
        batch = articles[i:i + BATCH_SIZE]
        batch_index = (i // BATCH_SIZE) + 1
        
        print(f"\n--- Xử lý lô (Batch) {batch_index} ({len(batch)} bài báo) ---")
        for idx, article in enumerate(batch):
            try:
                source_domain = article['feed_source'].split('//')[1][:15]
            except:
                source_domain = "unknown"
            print(f"  - {idx+1}. [{source_domain}] {article['title']:.70}...")
            
        if mock:
            result = mock_anthropic_call(batch_index, batch)
            aggregated_results.append(result)
        
        if i + BATCH_SIZE < total_articles:
            print("[zzZ] Sleep 3 giây Rate-limit Antrophic...")
            time.sleep(3)
            
    return aggregated_results

def main():
    print("=== BẮT ĐẦU CHẠY PIPELINE (VỚI CẤU HÌNH VINDYNAMIC) ===")
    
    articles = fetch_rss_feeds()
    
    # Lấy 10 bài đầu tiên làm mẫu để test cho nhanh
    articles = articles[:10]
    
    results = process_in_batches(articles, mock=True)
    
    print("\n=== HOÀN TẤT KIẾN TRÚC MỚI ===")
    print(f"[*] Đã thu về {len(results)} bản ghi JSON từ hệ thống xử lý (MOCK API).")

if __name__ == "__main__":
    main()
