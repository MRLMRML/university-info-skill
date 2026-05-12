#!/bin/bash
# ============================================================
# university-info-skill 一键安装脚本
# 用途：将三个 Skill 注册到 OpenCode
# ============================================================

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$HOME/.opencode/skills"

echo ""
echo "🎓 高校信息检索 Skill 安装脚本"
echo "================================"
echo ""

if [ ! -d "$SCRIPT_DIR/高校信息检索" ] || [ ! -d "$SCRIPT_DIR/择校分析" ] || [ ! -d "$SCRIPT_DIR/校招助手" ]; then
    echo -e "${RED}❌ 错误：找不到 Skill 目录${NC}"
    echo "请确保在 university-info-skill 仓库根目录下运行此脚本"
    exit 1
fi

mkdir -p "$SKILLS_DIR"

echo "📦 正在注册 Skill..."

if [ -e "$SKILLS_DIR/高校信息检索" ]; then
    echo -e "${YELLOW}⚠️  高校信息检索 已存在，跳过${NC}"
else
    ln -s "$SCRIPT_DIR/高校信息检索" "$SKILLS_DIR/高校信息检索"
    echo -e "${GREEN}✅ 高校信息检索 已注册${NC}"
fi

if [ -e "$SKILLS_DIR/择校分析" ]; then
    echo -e "${YELLOW}⚠️  择校分析 已存在，跳过${NC}"
else
    ln -s "$SCRIPT_DIR/择校分析" "$SKILLS_DIR/择校分析"
    echo -e "${GREEN}✅ 择校分析 已注册${NC}"
fi

if [ -e "$SKILLS_DIR/校招助手" ]; then
    echo -e "${YELLOW}⚠️  校招助手 已存在，跳过${NC}"
else
    ln -s "$SCRIPT_DIR/校招助手" "$SKILLS_DIR/校招助手"
    echo -e "${GREEN}✅ 校招助手 已注册${NC}"
fi

echo ""
echo "================================"
echo -e "${GREEN}🎉 安装完成！${NC}"
echo ""
echo "已注册的 Skill："
echo "  • 高校信息检索 — 通用查询（学科/排名/就业/师资/分数线）"
echo "  • 择校分析    — 学生场景（考研难度/性价比择校/调剂建议）"
echo "  • 校招助手    — HR 专用（目标校筛选/校招策略/ROI估算）"
echo ""
echo "💡 重启 OpenCode 后即可使用"
echo ""
