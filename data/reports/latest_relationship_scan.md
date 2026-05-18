# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T11:52:17.049137+00:00`
- Price records: `672`
- Market context records: `1114`
- Flow alert records: `5113`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8704`

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

- `market_context_high->crypto_major_24h` score `18.1919` n `150` status `ready` deltaP `39.2917` edge `1.3004` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `7.809` n `150` status `ready` deltaP `15.6527` edge `0.6698` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.5421` n `150` status `ready` deltaP `16.5208` edge `0.4847` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5571` n `150` status `ready` deltaP `-1.8889` edge `0.6424` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.1959` n `150` status `ready` deltaP `15.4791` edge `0.3606` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.6136` n `168` status `ready` deltaP `9.2698` edge `0.139` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.862` n `168` status `ready` deltaP `7.9849` edge `0.0869` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4905` n `168` status `ready` deltaP `7.6454` edge `0.0216` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2681` n `168` status `ready` deltaP `2.5805` edge `0.0429` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.11` n `168` status `ready` deltaP `8.0161` edge `0.0013` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0561` n `168` status `ready` deltaP `7.1322` edge `0.0337` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0409` n `168` status `ready` deltaP `8.3043` edge `0.142` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1885` n `168` status `ready` deltaP `7.1001` edge `-0.002` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2742` n `168` status `ready` deltaP `2.7944` edge `0.0428` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7049` n `168` status `ready` deltaP `1.2412` edge `0.001` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7427` n `168` status `ready` deltaP `-1.9247` edge `-0.0016` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0121` n `168` status `ready` deltaP `5.6911` edge `0.1288` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.3984` n `168` status `ready` deltaP `6.3952` edge `-0.0471` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1621` n `168` status `ready` deltaP `-11.1208` edge `-0.0145` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.3322` n `168` status `ready` deltaP `9.1609` edge `-0.2171` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
