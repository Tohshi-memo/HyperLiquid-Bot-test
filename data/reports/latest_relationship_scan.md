# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T07:41:21.916667+00:00`
- Price records: `672`
- Market context records: `6166`
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

- `news_risk_high->crypto_alt_24h` score `12.6853` n `32` status `ready` deltaP `42.8034` edge `0.7865` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.4128` n `32` status `ready` deltaP `65.0602` edge `0.184` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1264` n `32` status `ready` deltaP `42.9699` edge `0.062` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3663` n `32` status `ready` deltaP `28.5127` edge `0.021` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6936` n `195` status `ready` deltaP `0.8923` edge `0.236` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.483` n `32` status `ready` deltaP `16.2274` edge `0.1599` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.182` n `32` status `ready` deltaP `12.7102` edge `0.1135` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5895` n `32` status `ready` deltaP `7.955` edge `0.0687` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.2718` n `195` status `ready` deltaP `-0.9783` edge `0.2824` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.1562` n `195` status `ready` deltaP `20.7397` edge `0.1386` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.0052` n `32` status `ready` deltaP `10.1226` edge `0.019` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.0908` n `195` status `ready` deltaP `2.6626` edge `0.0664` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.292` n `195` status `ready` deltaP `1.205` edge `-0.0009` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6178` n `195` status `ready` deltaP `3.9653` edge `0.0131` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7521` n `195` status `ready` deltaP `-2.0605` edge `-0.0043` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7969` n `32` status `ready` deltaP `-3.3632` edge `-0.03` maxDD `-1.6464`
- `news_risk_high->commodity_24h` score `-0.8408` n `32` status `ready` deltaP `11.7416` edge `-0.1278` maxDD `-0.3101`
- `market_context_high->metal_1h` score `-0.8603` n `195` status `ready` deltaP `2.0214` edge `-0.0053` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.9858` n `195` status `ready` deltaP `-2.571` edge `0.0023` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9864` n `195` status `ready` deltaP `2.939` edge `0.0292` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
