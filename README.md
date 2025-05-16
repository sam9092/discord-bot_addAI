# 生成式AI結合discord bot
Discord API+ Google Cloud + Groq + Stable Diffusion

## 作者
翱翔 ao xiang

## 機器人載點(github)
https://github.com/sam9092/discord-bot_addAI

## 製作動機
在日常生活中，我們經常會在 LINE 或 Discord 等平台上看到許多有趣又實用的社群機器人，而這樣的互動形式深深吸引了我。
所以身為一位資工人的我，雖然過去沒有撰寫過社群機器人的經驗，但讓我產生了嘗試開發社群機器人的想法。

剛好在一次機緣下，朋友釋出了一個 Discord bot的委託需求，希望能開發一個可以偵測並處理 被盜訊息(@everyone)的 Discord bot。這個提案剛好契合我想實作的方向，因此我決定接下這個委託。

此外，這學期我選修了生成式 AI 相關的課程，為了鞏固所學，也為了讓這個 bot 更加有趣，我將生成式 AI 的功能整合進這個 Discord bot中，提升互動性，讓使用者在使用的過程中，也能享受與 AI 同樂的時光。

## 使用技術
### Discord API
Discord API 是這個專案的核心技術之一，它負責與 Discord平台進行溝通，讓 bot能夠即時監控訊息、回應指令以及管理伺服器內的任何互動。透過 discord套件，能實作了各種有趣且實用的功能，例如：訊息過濾（如監測 @everyone 的濫用）、任務排程、指令觸發（如 /help、/image）等功能，讓 Discord bot能夠更有互動性地融入伺服器活動中。

### Google Cloud Platform（GCP）
因為課程需求，我常帶筆電出門或關機，因此朋友(憨吉)常常跟我抱怨為什麼 Discord bot又沒開、不能玩指令，於是我想到以前所學的雲端技能來確保 24小時運作 Discord bot，而不用一直侷限在我自己的本地端(筆電)上，讓我可以正常關機或處理其他事情，不用被 Discord bot占用電腦資源。
在眾多雲端平台中，我選擇 Google Cloud Platform的主要原因是它提供了 300美金的額度，來免費使用各種雲端資源，對於我來說非常友善。
在部署過程中，我使用 Compute Engine建立了一台 Ubuntu虛擬機，並手動設定環境（venv+tumx的虛擬環境、Bot 所用的相關函式庫及程式），讓 Discord bot可以穩定在雲端運行。
在使用的過程中，我發現到 Google Cloud有提供帳號綁定的 SSH連線(不需要去處理金鑰的部分)及 文件上傳/下載的GUI介面，這兩個功能對我來說非常的方便，可以快速更新 Discord bot，此外 Compute Engine的虛擬機開機速度也蠻快的，不用為了開虛擬機等半天。
這次的雲端部署，讓我複習了當初學的雲端架設技術及 Linux的基礎操作(移動資料等等)。

### Groq
因為 Groq提供了免費的 API來使用各種模型，而我透過了 openai函式庫來串接 Groq，再選擇 Meta 的大型語言模型 meta-llama/llama-4-scout-17b-16e-instruct。
我看別人評論此模型相比其他模型具備了良好的中文對話能力，可用於回答問題、翻譯等功能，讓 Discord bot能與使用者自然互動、產生幽默且具有風格的文字。

### Stable Diffusion
Stable Diffusion是一種圖像生成技術，使用者只需輸入一句話，模型就能透過 Prompt生成獨特的圖片。在眾多模型中，我選擇了 nitrosocke/Ghibli-Diffusion，是因為其風格是模仿宮崎駿動畫的風格，能讓 Discord bot提供大家娛樂，增添伺服器互動氛圍。

## 使用方式
0. 到 https://github.com/sam9092/discord-bot_addAI 下載程式
1. 建立自己的.env
    ```
    DISCORD_TOKEN=(Discord_Token)
    api_key=(Groq API....)
    ```
2. 到 https://console.cloud.google.com/ 註冊(若沒有要雲端服務，直接跳到步驟 12)
3. 建立雲端伺服器(點選 Compute Engine/VM執行個體/建立執行個體)
4. 設定伺服器的機型
    * 我是選用最便宜的方案->共用核心的 e2-small (0.5至2個 vCPU，2 GB記憶體)
5. 裝虛擬環境 venv(由於Google Cloud Platform不能直接 pip install)
    ```
    python3 -m venv dcbot
   ```
7. 裝程式需要的函式庫
    ```
   pip install discord.py python-dotenv diffusers torch openai
    ```

8. 還需要裝 tmux(避免中斷SSH連線，機器人也跟著離線)
    ```
   sudo apt install tmux
    ```
10. 啟動 tmux及 venv虛擬環境
    ```
    tmux
    source dcbot/bin/activate
    ```
11. 把下載的程式上傳至雲端
12. 執行 shell檔移動程式到他該去的地方
    ```
    chmod +x move.sh
    sh move.sh
    ```
13. cd進 (bot.py所在的資料夾)
    ```
    cd dcBot
    ```
15. 執行bot.py即可
    ```
    python bot.py
    ```
17. 若中斷ssh回來，想回到虛擬環境
    ```
    tmux attach
    ```

## 參考資料
[Python Discord Bot 基礎教學](https://hackmd.io/@smallshawn95/python_discord_bot_base)

[Python Discord Bot Course (Github)](https://github.com/smallshawn95/Python-Discord-Bot-Course)

[Google Cloud 架設教學](https://www.chirue.com/gcp-vm-setting/)
