# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T10:22:25.819712+00:00`
- Price records: `672`
- Market context records: `6909`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_24h` score `0.0531` n `193` status `ready` deltaP `-5.3681` edge `0.4422` maxDD `-14.3015`
- `market_context_high->fx_1h` score `-0.1615` n `224` status `ready` deltaP `3.7345` edge `0.0029` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3707` n `224` status `ready` deltaP `3.109` edge `0.0248` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4543` n `224` status `ready` deltaP `4.5953` edge `0.0219` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6213` n `224` status `ready` deltaP `-0.8982` edge `-0.0052` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7227` n `224` status `ready` deltaP `15.527` edge `0.0102` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7651` n `224` status `ready` deltaP `-0.7298` edge `-0.0021` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8199` n `224` status `ready` deltaP `-3.5447` edge `-0.0047` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3128` n `224` status `ready` deltaP `-1.5789` edge `-0.0088` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5546` n `224` status `ready` deltaP `-2.8122` edge `-0.0207` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.717` n `224` status `ready` deltaP `2.5342` edge `-0.019` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.895` n `224` status `ready` deltaP `5.3136` edge `-0.0204` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1646` n `224` status `ready` deltaP `2.7766` edge `0.0023` maxDD `-5.5324`
- `market_context_high->commodity_24h` score `-2.5177` n `193` status `ready` deltaP `-1.0785` edge `-0.0158` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `-2.7153` n `224` status `ready` deltaP `2.2104` edge `-0.0045` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.815` n `224` status `ready` deltaP `-0.0871` edge `-0.0276` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9925` n `224` status `ready` deltaP `-7.818` edge `0.0393` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.1264` n `193` status `ready` deltaP `-5.1661` edge `-0.0058` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.1028` n `224` status `ready` deltaP `2.7113` edge `-0.1342` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3083` n `193` status `ready` deltaP `-13.2811` edge `-0.1174` maxDD `-28.4043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
