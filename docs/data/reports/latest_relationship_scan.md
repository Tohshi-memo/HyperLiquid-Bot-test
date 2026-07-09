# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T13:37:37.507146+00:00`
- Price records: `672`
- Market context records: `6185`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.6218` n `32` status `ready` deltaP `42.2194` edge `0.7851` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.0008` n `32` status `ready` deltaP `61.3946` edge `0.1741` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.064` n `32` status `ready` deltaP `42.3701` edge `0.0608` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.352` n `32` status `ready` deltaP `28.3632` edge `0.0208` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `1.9781` n `32` status `ready` deltaP `15.625` edge `0.2274` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8584` n `192` status `ready` deltaP `1.1514` edge `0.248` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3487` n `32` status `ready` deltaP `13.906` edge `0.1269` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7055` n `32` status `ready` deltaP `9.0013` edge `0.0766` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.45` n `192` status `ready` deltaP `-1.2859` edge `0.2993` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0528` n `192` status `ready` deltaP `19.8023` edge `0.1316` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.0966` n `192` status `ready` deltaP `2.4706` edge `0.0672` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1454` n `32` status `ready` deltaP `9.4813` edge `0.0053` maxDD `-2.3058`
- `news_risk_high->commodity_24h` score `-0.1623` n `32` status `ready` deltaP `15.4974` edge `-0.0963` maxDD `-0.3101`
- `market_context_high->fx_1h` score `-0.2881` n `192` status `ready` deltaP `1.2799` edge `-0.0009` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6695` n `192` status `ready` deltaP `3.4673` edge `0.0098` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.8072` n `192` status `ready` deltaP `-2.7653` edge `-0.0042` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8483` n `32` status `ready` deltaP `-4.1106` edge `-0.0316` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.951` n `192` status `ready` deltaP `4.0102` edge `0.0281` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9581` n `192` status `ready` deltaP `3.2721` edge `0.0306` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9642` n `192` status `ready` deltaP `1.0977` edge `-0.0078` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
