# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T07:17:29.716303+00:00`
- Price records: `672`
- Market context records: `6164`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.6433` n `32` status `ready` deltaP `42.8034` edge `0.783` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.4326` n `32` status `ready` deltaP `65.2324` edge `0.1845` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1409` n `32` status `ready` deltaP `43.1212` edge `0.0622` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3795` n `32` status `ready` deltaP `28.6622` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6912` n `195` status `ready` deltaP `0.8923` edge `0.2358` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.4369` n `32` status `ready` deltaP `16.2274` edge `0.154` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.175` n `32` status `ready` deltaP `12.5607` edge `0.1136` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5794` n `32` status `ready` deltaP `7.8055` edge `0.0684` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.255` n `195` status `ready` deltaP `-0.9783` edge `0.281` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.13` n `195` status `ready` deltaP `20.5675` edge `0.1364` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.0052` n `32` status `ready` deltaP `10.1226` edge `0.019` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.08` n `195` status `ready` deltaP `2.6626` edge `0.0673` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2835` n `195` status `ready` deltaP `1.3545` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6006` n `195` status `ready` deltaP `4.1165` edge `0.0143` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7545` n `195` status `ready` deltaP `-2.0605` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7837` n `32` status `ready` deltaP `-3.2138` edge `-0.0293` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.84` n `195` status `ready` deltaP `2.1708` edge `-0.0046` maxDD `-2.0564`
- `news_risk_high->commodity_24h` score `-0.8504` n `32` status `ready` deltaP `11.7416` edge `-0.1286` maxDD `-0.3101`
- `market_context_high->equity_1h` score `-0.9703` n `195` status `ready` deltaP `-2.4216` edge `0.0033` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9965` n `195` status `ready` deltaP `2.7895` edge `0.0289` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
