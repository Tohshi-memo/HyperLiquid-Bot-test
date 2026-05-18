# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T10:52:15.219461+00:00`
- Price records: `672`
- Market context records: `1110`
- Flow alert records: `5101`
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

- `market_context_high->crypto_major_24h` score `17.8195` n `150` status `ready` deltaP `38.5973` edge `1.274` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `7.3935` n `150` status `ready` deltaP `14.9583` edge `0.6398` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.3505` n `150` status `ready` deltaP `16.0` edge `0.4722` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.4657` n `150` status `ready` deltaP `-2.2361` edge `0.6371` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.0457` n `150` status `ready` deltaP `15.1319` edge `0.3504` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.6972` n `168` status `ready` deltaP `9.8795` edge `0.1419` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.896` n `168` status `ready` deltaP `8.2897` edge `0.0877` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4702` n `168` status `ready` deltaP `7.4957` edge `0.0209` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2872` n `168` status `ready` deltaP `2.7302` edge `0.0435` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.11` n `168` status `ready` deltaP `8.0161` edge `0.0013` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0921` n `168` status `ready` deltaP `7.2819` edge `0.0357` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.052` n `168` status `ready` deltaP `8.4567` edge `0.1424` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1956` n `168` status `ready` deltaP `6.9504` edge `-0.0016` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2034` n `168` status `ready` deltaP `3.2435` edge `0.0457` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6954` n `168` status `ready` deltaP `1.3937` edge `0.0012` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7263` n `168` status `ready` deltaP `-1.6253` edge `-0.0015` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0058` n `168` status `ready` deltaP `5.6911` edge `0.1296` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.3803` n `168` status `ready` deltaP `6.5476` edge `-0.0466` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1282` n `168` status `ready` deltaP `-10.6635` edge `-0.0132` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.3354` n `150` status `ready` deltaP `1.1736` edge `-0.0278` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
