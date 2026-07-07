# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T16:07:27.428712+00:00`
- Price records: `672`
- Market context records: `5996`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->fx_24h` score `7.5455` n `30` status `ready` deltaP `68.9236` edge `0.1693` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.2183` n `30` status `ready` deltaP `32.5` edge `0.1554` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1543` n `30` status `ready` deltaP `43.0488` edge `0.0638` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2298` n `30` status `ready` deltaP `26.7764` edge `0.0212` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1344` n `225` status `ready` deltaP `7.4215` edge `0.1545` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7288` n `30` status `ready` deltaP `9.5908` edge `0.0762` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1413` n `30` status `ready` deltaP `5.02` edge `0.0308` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1125` n `30` status `ready` deltaP `9.2361` edge `0.04` maxDD `-2.3058`
- `market_context_high->equity_24h` score `-0.2391` n `198` status `ready` deltaP `22.8536` edge `0.3641` maxDD `-31.2441`
- `news_risk_high->metal_1h` score `-0.3939` n `30` status `ready` deltaP `1.8363` edge `-0.0261` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4758` n `225` status `ready` deltaP `3.1557` edge `0.0308` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5021` n `225` status `ready` deltaP `2.2808` edge `0.0003` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5818` n `225` status `ready` deltaP `-0.517` edge `0.0021` maxDD `-0.771`
- `market_context_high->fx_1h` score `-0.7268` n `225` status `ready` deltaP `-1.2236` edge `-0.0016` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0088` n `30` status `ready` deltaP `-8.9521` edge `-0.0182` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.0391` n `225` status `ready` deltaP `-0.0935` edge `-0.0007` maxDD `-3.2179`
- `market_context_high->crypto_major_1h` score `-1.1661` n `225` status `ready` deltaP `2.2575` edge `0.0122` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.2066` n `225` status `ready` deltaP `-0.2351` edge `0.0156` maxDD `-3.165`
- `market_context_high->index_1h` score `-1.2099` n `225` status `ready` deltaP `-1.841` edge `0.0028` maxDD `-1.3078`
- `market_context_high->crypto_alt_1h` score `-1.2376` n `225` status `ready` deltaP `1.2422` edge `0.0083` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
