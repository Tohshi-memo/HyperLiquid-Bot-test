# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T13:22:24.647478+00:00`
- Price records: `672`
- Market context records: `2043`
- Flow alert records: `7774`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `9.0` n `205` status `ready` deltaP `31.5739` edge `0.5925` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3929` n `205` status `ready` deltaP `24.4014` edge `0.6512` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.1883` n `205` status `ready` deltaP `19.7709` edge `0.4588` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9285` n `205` status `ready` deltaP `16.9938` edge `0.2402` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.2287` n `205` status `ready` deltaP `17.5146` edge `0.601` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.6339` n `205` status `ready` deltaP `13.0765` edge `0.1476` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4703` n `205` status `ready` deltaP `13.1233` edge `0.1034` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2905` n `205` status `ready` deltaP `10.2322` edge `0.1507` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.7014` n `205` status `ready` deltaP `16.6638` edge `0.4372` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.5646` n `205` status `ready` deltaP `4.9928` edge `0.1366` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.2679` n `205` status `ready` deltaP `7.3595` edge `0.0521` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.1345` n `205` status `ready` deltaP `4.345` edge `0.0542` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.251` n `205` status `ready` deltaP `3.0028` edge `0.0181` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5594` n `205` status `ready` deltaP `10.6034` edge `0.022` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.7316` n `205` status `ready` deltaP `4.7064` edge `0.0264` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8266` n `205` status `ready` deltaP `-0.9924` edge `0.0005` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-1.0093` n `205` status `ready` deltaP `9.4729` edge `0.115` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.444` n `205` status `ready` deltaP `-4.7394` edge `-0.0006` maxDD `-1.0513`
- `market_context_high->crypto_major_24h` score `-1.589` n `205` status `ready` deltaP `16.7044` edge `0.6148` maxDD `-62.3533`
- `market_context_high->commodity_1h` score `-1.8925` n `205` status `ready` deltaP `2.1564` edge `-0.0012` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
