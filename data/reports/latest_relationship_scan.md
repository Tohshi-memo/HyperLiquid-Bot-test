# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T13:39:19.429202+00:00`
- Price records: `672`
- Market context records: `6608`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.5971` n `169` status `ready` deltaP `2.7078` edge `0.5729` maxDD `-13.2952`
- `market_context_high->unknown_1h` score `2.1124` n `206` status `ready` deltaP `-5.6799` edge `0.304` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.2805` n `169` status `ready` deltaP `7.6943` edge `0.1589` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2775` n `206` status `ready` deltaP `2.2135` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4286` n `206` status `ready` deltaP `6.9051` edge `0.0256` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5349` n `206` status `ready` deltaP `0.4404` edge `-0.0032` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.563` n `206` status `ready` deltaP `-0.5581` edge `0.0035` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6781` n `206` status `ready` deltaP `4.1785` edge `0.0165` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.8917` n `206` status `ready` deltaP `9.6688` edge `0.0092` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1828` n `206` status `ready` deltaP `1.8284` edge `-0.0004` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.209` n `206` status `ready` deltaP `-0.0637` edge `-0.0051` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3565` n `206` status `ready` deltaP `-4.4373` edge `-0.0033` maxDD `-2.0797`
- `market_context_high->unknown_4h` score `-1.5184` n `206` status `ready` deltaP `-17.3795` edge `0.2299` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6318` n `206` status `ready` deltaP `1.9654` edge `-0.0011` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.6926` n `206` status `ready` deltaP `7.4621` edge `0.0647` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0772` n `206` status `ready` deltaP `4.4814` edge `0.044` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1493` n `206` status `ready` deltaP `-1.2003` edge `0.0185` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.1185` n `206` status `ready` deltaP `7.3496` edge `-0.0219` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.3328` n `169` status `ready` deltaP `-0.2375` edge `0.0571` maxDD `-11.2901`
- `market_context_high->fx_24h` score `-5.7055` n `169` status `ready` deltaP `-6.2928` edge `-0.0003` maxDD `-8.9898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
