"use strict";
/* Fashion / Chapter 02. Progressive enhancement only.
   All claims and quotations refer to the 17 Oct author-selected manuscript.
   No analytics requests, cookies, email collection, or simulated checkout. */
(() => {
  const quotes = [
    "mỗi mùa đông về có thể tự thưởng cho bản thân một đôi sneakers trendy nhất season.",
    "bán nhiều hơn → higher revenue → ra thêm sản phẩm → bán nhiều hơn nữa.",
    "Kiểu techwear thì phải thế này mới được gọi là techwear",
    "bỏ bớt những thứ không hợp, giữ lại những thứ hợp",
    "chính những dấu mark hay vết stain trên những món items cũ của bạn làm cho chúng đặc biệt",
    "cái cảm giác lục tủ đồ của bố bạn rồi bỗng nhiên tìm được a hidden gem there"
  ];
  const stageNames = ["DESIRE", "CONSUMPTION", "IMITATION", "EXPERIMENT", "PATINA", "INHERITANCE"];
  const annotations = [
    "Khởi đầu là một ước muốn, không phải một bản ghi về món giày đã mua. Hình minh họa không chứng minh một giao dịch thực tế.",
    "Cách Jason từng diễn giải vòng lặp doanh thu. Đây là một quan sát cá nhân về consumption, không phải bằng chứng kinh tế nhân quả.",
    "Những quy tắc thời trang trong bài được thuật lại từ cảm nhận của người kể; không công bố lại bài viết hoặc danh tính đồng nghiệp.",
    "Jason nhìn việc học theo người khác như một bước thử nghiệm rồi chọn ra thứ phù hợp. Đây là diễn giải của biên tập, không phải một sự kiện mới.",
    "Vết sờn và dấu bẩn là motif trong văn bản. Hình ảnh minh họa không khẳng định đây là một món đồ Jason thực sự sở hữu.",
    "Hình ảnh tủ đồ của bố là biểu tượng từ câu văn của Jason, chưa phải hiện vật gia đình hoặc ảnh tư liệu đã xác minh."
  ];

  const choices = Array.from(document.querySelectorAll('[data-memory]'));
  const image = document.getElementById("memory-img");
  const title = document.getElementById("memory-title");
  const description = document.getElementById("memory-desc");
  const quote = document.getElementById("memory-quote");
  const footnote = document.getElementById("memory-footnote");
  const counter = document.getElementById("wardrobe-counter");
  const previous = document.getElementById("wardrobe-prev");
  const next = document.getElementById("wardrobe-next");
  const card = document.querySelector(".memory");
  let selected = 0;

  function selectMemory(index, moveFocus = false) {
    if (!choices.length || !choices[index]) return;
    selected = index;
    choices.forEach((button, i) => button.setAttribute("aria-pressed", String(i === selected)));
    const item = choices[selected];
    if (card) card.classList.add("is-changing");
    if (image) {
      image.src = item.dataset.image;
      image.alt = "Trích một phần tranh minh họa Fashion, không phải ảnh tư liệu: " + item.dataset.title;
      image.onload = () => card && card.classList.remove("is-changing");
      image.onerror = () => card && card.classList.remove("is-changing");
    }
    if (title) title.textContent = item.dataset.title;
    if (description) description.textContent = item.dataset.description;
    if (quote) quote.textContent = "“" + quotes[selected] + "”";
    if (footnote) footnote.textContent = annotations[selected];
    if (counter) counter.textContent = String(selected + 1).padStart(2, "0") + " / 06 · " + stageNames[selected];
    if (previous) previous.disabled = selected === 0;
    if (next) next.textContent = selected === choices.length - 1 ? "BACK TO THE DROP ↗" : "NEXT OBJECT →";
    if (moveFocus) item.focus();
  }

  choices.forEach((item, i) => {
    item.addEventListener("click", () => selectMemory(i));
    item.addEventListener("keydown", event => {
      if (!["ArrowRight", "ArrowLeft", "ArrowDown", "ArrowUp", "Home", "End"].includes(event.key)) return;
      event.preventDefault();
      const target = event.key === "Home" ? 0 :
        event.key === "End" ? choices.length - 1 :
        event.key === "ArrowRight" || event.key === "ArrowDown" ?
          (i + 1) % choices.length : (i - 1 + choices.length) % choices.length;
      selectMemory(target, true);
    });
  });
  if (previous) previous.addEventListener("click", () => selectMemory(Math.max(0, selected - 1)));
  if (next) next.addEventListener("click", () => selectMemory((selected + 1) % choices.length));
  if (choices.length) selectMemory(0);

  // Reading progress shows position only: no scroll history is recorded.
  const meter = document.getElementById("reading-meter");
  if (meter) {
    let pending = false;
    const updateMeter = () => {
      const total = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      const percent = Math.max(0, Math.min(100, (window.scrollY / total) * 100));
      document.documentElement.style.setProperty("--chapter-scroll", percent.toFixed(1) + "%");
      pending = false;
    };
    window.addEventListener("scroll", () => {
      if (!pending) { pending = true; window.requestAnimationFrame(updateMeter); }
    }, { passive: true });
    window.addEventListener("resize", updateMeter);
    updateMeter();
  }

  const pageUrl = "https://jasonthedataguy.github.io/json-under-revision/chapters/02/";
  const copy = document.getElementById("copy-chapter-link");
  const share = document.getElementById("share-chapter");
  const feedback = document.getElementById("share-feedback");
  const status = message => { if (feedback) feedback.textContent = message; };
  if (copy) {
    copy.addEventListener("click", async () => {
      try {
        if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error("Clipboard unavailable");
        await navigator.clipboard.writeText(pageUrl);
        status("Đã copy đường dẫn chương Fashion.");
      } catch (_) {
        // Display a selectable URL instead of claiming the clipboard worked.
        status("Copy đường dẫn này: " + pageUrl);
      }
    });
  }
  if (share && typeof navigator.share === "function") {
    share.hidden = false;
    share.addEventListener("click", async () => {
      try {
        await navigator.share({ title: "Fashion | .json / 02", text: "Be your own label, not a hanger.", url: pageUrl });
        status("Trang chia sẻ đã được mở.");
      } catch (error) {
        // Cancellation is not a successful share.
        if (error && error.name !== "AbortError") status("Không thể mở chia sẻ. Bạn có thể copy link.");
      }
    });
  }
})();