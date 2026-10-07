# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T11:22:29.017244+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_4h` score `36.6623` n `93` status `ready` deltaP `-5.0583` edge `3.1428` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.4392` n `62` status `ready` deltaP `36.1428` edge `0.6493` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1598` n `62` status `ready` deltaP `23.5445` edge `0.5741` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.6447` n `62` status `ready` deltaP `26.3889` edge `0.1278` maxDD `0.0`
- `news_risk_high->index_4h` score `2.9355` n `62` status `ready` deltaP `32.7646` edge `0.0524` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.8856` n `62` status `ready` deltaP `7.2637` edge `0.202` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.285` n `62` status `ready` deltaP `8.8275` edge `0.1671` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.1109` n `62` status `ready` deltaP `18.691` edge `0.1111` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.0241` n `93` status `ready` deltaP `14.0998` edge `0.1711` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0091` n `62` status `ready` deltaP `25.3236` edge `0.0136` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4461` n `62` status `ready` deltaP `20.4858` edge `0.0904` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.2042` n `93` status `ready` deltaP `4.9003` edge `0.4191` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `1.1838` n `62` status `ready` deltaP `3.4576` edge `0.1275` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.8342` n `93` status `ready` deltaP `13.5358` edge `0.0035` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.5918` n `93` status `ready` deltaP `16.6175` edge `0.0142` maxDD `-0.3868`
- `market_context_high->metal_24h` score `0.4434` n `93` status `ready` deltaP `16.6722` edge `0.0942` maxDD `-3.5466`
- `news_risk_high->commodity_24h` score `0.3309` n `62` status `ready` deltaP `25.8065` edge `0.027` maxDD `-8.196`
- `news_risk_high->metal_1h` score `0.188` n `62` status `ready` deltaP `7.3498` edge `0.0085` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.1227` n `93` status `ready` deltaP `9.9028` edge `0.0386` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `0.0618` n `93` status `ready` deltaP `5.2878` edge `0.0075` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
