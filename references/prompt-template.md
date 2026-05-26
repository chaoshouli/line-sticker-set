# Prompt Template

Use this as the base image prompt. Adapt the bracketed fields.

```text
Reference the uploaded image as the character identity source. Transform the character into a cute stylized LINE sticker character while preserving the recognizable traits: [stable character traits].

Create a complete set of 16 different LINE-style stickers for everyday Chinese chat conversations about: [scene description].

Layout:
- one single sticker sheet
- 4x4 grid arrangement
- pure white background
- no visible grid lines, no borders, no frames
- treat the sheet as 16 separate invisible square cells with clear white gutters between neighboring cells
- each sticker group stays fully inside its own invisible square cell
- inside each cell, place the complete sticker inside an imaginary centered safe box occupying only the central 50-60% of that cell
- leave at least 25% white safe margin between every sticker group and every cell edge
- keep the character smaller rather than too large
- no cropping, no overflow, no element touching or crossing the image edge or any cell boundary
- all hands, feet, hair, hats, props, speech bubbles, effects, decorative marks, and Chinese text must be fully visible inside the same cell
- do not let confetti, stars, moons, bubbles, scarf ends, motion lines, text, hair, hands, feet, or any decoration spill into neighboring cells

Style:
- cute stylized mascot / LINE sticker style
- clean outline, soft colors, expressive face
- readable Chinese text integrated as speech bubbles, captions, or dynamic sticker text
- varied text layouts across stickers

Variety:
- 16 stickers must all be different
- vary pose, expression, gesture, prop, camera angle, and text placement
- do not repeat the same pose or layout

Chinese dialogue:
1. 早呀～
2. 收到！
3. 好耶！
4. 狠狠赞了
5. 我先溜啦
6. 等我一下
7. 尊嘟假嘟？
8. 破防了
9. 笑发财了
10. 有点离谱
11. 开冲！
12. 已读乱回
13. 今天也要加油
14. 谢谢老板
15. 不愧是你
16. 晚安啦

Strict negative constraints:
- no cropped body parts
- no cropped text
- no sticker touching boundaries
- no decorative elements crossing into neighboring cells
- no character, text, prop, bubble, or effect outside its own invisible cell safe box
- no text outside its cell
- no duplicate pose
- no extra stickers
- no watermark
- no non-white background
```

## Phrase Swaps

Pick wording that fits the user's scene. Keep phrases short for readability.

Daily:
`早呀～`, `晚安啦`, `收到！`, `马上来`, `等我一下`, `我先溜啦`, `安排上了`, `没问题`

Work/study:
`开会中`, `已同步`, `在改了`, `ddl救命`, `今天也要加油`, `脑子加载中`, `先码住`, `狠狠拿捏`

Emotion:
`破防了`, `笑发财了`, `尊嘟假嘟？`, `有点离谱`, `我裂开了`, `太难了`, `好耶！`, `稳了`

Social:
`谢谢老板`, `不愧是你`, `狠狠赞了`, `贴贴`, `抱抱`, `别卷了`, `一起冲`, `已读乱回`
