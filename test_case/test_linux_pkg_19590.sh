#!/bin/bash

# 設定測試用的檔案名稱
TEST_WAV="test_audio.wav"
TEST_MP3="test_audio.mp3"
TEST_7Z="test_archive.7z"

# 函數：檢查命令是否存在
check_command() {
    if command -v $1 >/dev/null 2>&1; then
        echo "$1 已安裝."
        return 0
    else
        echo "$1 未安裝或不在PATH中."
        return 1
    fi
}

# 函數：測試 ffmpeg
test_ffmpeg() {
    if check_command ffmpeg; then
        echo "測試 ffmpeg..."
        ffmpeg -i $TEST_WAV -ac 1 -ar 16000 -b:a 32k $TEST_MP3 >/dev/null 2>&1
        if [ $? -eq 0 ] && [ -f $TEST_MP3 ]; then
            echo "ffmpeg 成功將 WAV 轉換為 MP3."
        else
            echo "ffmpeg 轉換失敗."
        fi
        rm -f $TEST_MP3
    fi
}

# 函數：測試 sox
test_sox() {
    if check_command sox; then
        echo "測試 sox..."
        sox $TEST_WAV $TEST_MP3 >/dev/null 2>&1
        if [ $? -eq 0 ] && [ -f $TEST_MP3 ]; then
            echo "sox 成功將 WAV 轉換為 MP3."
        else
            echo "sox 轉換失敗."
        fi
        rm -f $TEST_MP3
    fi
}

# 函數：測試 7zr
test_7zr() {
    if check_command 7zr; then
        echo "測試 7zr..."
        echo "test content" > test_file.txt
        7zr a $TEST_7Z test_file.txt >/dev/null 2>&1
        if [ $? -eq 0 ] && [ -f $TEST_7Z ]; then
            echo "7zr 成功創建壓縮檔."
            7zr e $TEST_7Z -y >/dev/null 2>&1
            if [ $? -eq 0 ] && [ -f test_file.txt ]; then
                echo "7zr 成功解壓縮檔案."
            else
                echo "7zr 解壓縮失敗."
            fi
        else
            echo "7zr 創建壓縮檔失敗."
        fi
        rm -f test_file.txt $TEST_7Z
    fi
}

# 主程序
echo "開始測試..."
test_ffmpeg
echo ""
test_sox
echo ""
test_7zr
echo ""
echo "測試完成."
