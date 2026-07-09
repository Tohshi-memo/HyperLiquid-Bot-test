# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T03:22:25.350579+00:00`
- Price records: `672`
- Market context records: `6152`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `12.0845` n `30` status `ready` deltaP `42.118` edge `0.741` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.6444` n `30` status `ready` deltaP `67.5347` edge `0.1868` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2787` n `32` status `ready` deltaP `44.5884` edge `0.0639` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3907` n `32` status `ready` deltaP `28.7425` edge `0.0215` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6338` n `195` status `ready` deltaP `0.8046` edge `0.2316` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3127` n `32` status `ready` deltaP `13.9783` edge `0.1218` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7055` n `32` status `ready` deltaP `9.0756` edge `0.0761` maxDD `-1.6923`
- `news_risk_high->crypto_major_24h` score `0.6229` n `30` status `ready` deltaP `12.8125` edge `0.0724` maxDD `-4.2368`
- `market_context_high->equity_4h` score `0.0332` n `195` status `ready` deltaP `2.6829` edge `0.0766` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2274` n `30` status `ready` deltaP `7.5` edge `0.008` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2762` n `195` status `ready` deltaP `1.4348` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.2951` n `195` status `ready` deltaP `-2.1545` edge `0.243` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.3408` n `195` status `ready` deltaP `18.2933` edge `0.0912` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.5746` n `195` status `ready` deltaP `4.1518` edge `0.0174` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6079` n `30` status `ready` deltaP `14.0973` edge `-0.1241` maxDD `-0.3101`
- `news_risk_high->metal_1h` score `-0.7224` n `32` status `ready` deltaP `-2.3952` edge `-0.0269` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7457` n `195` status `ready` deltaP `2.9894` edge `-0.0022` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.7763` n `195` status `ready` deltaP `-2.2885` edge `-0.0048` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.8491` n `195` status `ready` deltaP `-1.4571` edge `0.0124` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.8704` n `195` status `ready` deltaP `4.0596` edge `0.0366` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
