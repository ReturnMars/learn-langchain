from my_llm import llm

print("=" * 60)
print("流式输出（实时显示，带标记）：")
print("=" * 60)

# 如果需要调试，可以设置为 True 查看 chunk 结构
DEBUG = True

chunks = []
think_content = ""  # 思考过程
answer_content = ""  # 正式回答

# 用于标记是否已经打印了标签
think_label_printed = False
answer_label_printed = False

for chunk in llm.stream("用三句话简单介绍一下：机器学习的基本概念"):
    reasoning = ""
    
    # 调试模式：打印 chunk 结构（仅前3个）
    if DEBUG and len(chunks) < 3:
        print(f"\n[调试] Chunk {len(chunks)}: type={type(chunk)}")
        print(f"  - chunk attributes: {dir(chunk)}")
        if hasattr(chunk, 'message'):
            print(f"  - message type: {type(chunk.message)}")
            print(f"  - message attributes: {dir(chunk.message)}")
            if hasattr(chunk.message, 'additional_kwargs'):
                print(f"  - additional_kwargs: {chunk.message.additional_kwargs}")
                print(f"  - additional_kwargs keys: {list(chunk.message.additional_kwargs.keys())}")
        # 检查chunk本身是否有additional_kwargs
        if hasattr(chunk, 'additional_kwargs'):
            print(f"  - chunk.additional_kwargs: {chunk.additional_kwargs}")
        if hasattr(chunk, 'content'):
            print(f"  - chunk.content: {repr(chunk.content)}")
    
    # 提取思考内容（reasoning）- 尝试多种方式
    # 方式1：从 chunk.message.additional_kwargs 获取
    if hasattr(chunk, 'message') and hasattr(chunk.message, 'additional_kwargs'):
        reasoning = chunk.message.additional_kwargs.get("reasoning_content", "")
        if not reasoning:
            # 尝试其他可能的键
            reasoning = chunk.message.additional_kwargs.get("reasoning", "")
    
    # 方式2：从 chunk.additional_kwargs 获取（如果存在）
    if not reasoning and hasattr(chunk, 'additional_kwargs'):
        reasoning = chunk.additional_kwargs.get("reasoning_content", "")
        if not reasoning:
            reasoning = chunk.additional_kwargs.get("reasoning", "")
    
    # 方式3：检查chunk的其他属性
    if not reasoning and hasattr(chunk, 'reasoning_content'):
        reasoning = chunk.reasoning_content
    
    if reasoning:
        # 只在第一次遇到思考内容时打印标签
        if not think_label_printed:
            print("[思考] ", end='', flush=True)
            think_label_printed = True
        print(reasoning, end='', flush=True)
        think_content += reasoning
    
    # 提取正式回答内容
    content = chunk.content if hasattr(chunk, 'content') else ""
    if content:
        # 只在第一次遇到回答内容时打印标签
        if not answer_label_printed:
            if think_label_printed:
                print("\n[回答] ", end='', flush=True)
            else:
                print("[回答] ", end='', flush=True)
            answer_label_printed = True
        print(content, end='', flush=True)
        answer_content += content
    
    chunks.append(chunk)

print("\n")  # 换行
print("=" * 60)
print(f"完整内容（共 {len(chunks)} 个 chunks）")
print("=" * 60)

if think_content:
    print("\n【思考过程】")
    print("-" * 60)
    print(think_content)
    print("-" * 60)

if answer_content:
    print("\n【正式回答】")
    print("-" * 60)
    print(answer_content)
    print("-" * 60)

print("=" * 60)










