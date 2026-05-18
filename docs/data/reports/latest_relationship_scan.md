# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T09:22:18.749199+00:00`
- Price records: `672`
- Market context records: `1104`
- Flow alert records: `5082`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `17.2982` n `150` status `ready` deltaP `37.5556` edge `1.2375` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `6.7353` n `150` status `ready` deltaP `13.9166` edge `0.5919` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.1475` n `150` status `ready` deltaP `15.6527` edge `0.4576` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.3022` n `150` status `ready` deltaP `-2.9305` edge `0.6281` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.8945` n `150` status `ready` deltaP `15.1319` edge `0.3378` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.8556` n `168` status `ready` deltaP `10.7942` edge `0.149` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.9699` n `168` status `ready` deltaP `8.8995` edge `0.0898` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4378` n `168` status `ready` deltaP `7.1963` edge `0.0202` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2273` n `168` status `ready` deltaP `2.2811` edge `0.0415` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1376` n `168` status `ready` deltaP `8.3155` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0729` n `168` status `ready` deltaP `7.1322` edge `0.0351` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.041` n `168` status `ready` deltaP `8.4567` edge `0.141` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.2184` n `168` status `ready` deltaP `6.8007` edge `-0.0025` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2682` n `168` status `ready` deltaP `2.9441` edge `0.0423` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6787` n `168` status `ready` deltaP `1.6986` edge `0.0013` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6952` n `168` status `ready` deltaP `-1.1762` edge `-0.0005` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0717` n `168` status `ready` deltaP `5.2338` edge `0.1242` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.2845` n `168` status `ready` deltaP `7.3098` edge `-0.0437` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1266` n `168` status `ready` deltaP `-10.6635` edge `-0.013` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.2703` n `150` status `ready` deltaP `2.2152` edge `-0.0264` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
