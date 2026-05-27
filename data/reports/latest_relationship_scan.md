# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T15:52:30.263352+00:00`
- Price records: `672`
- Market context records: `2053`
- Flow alert records: `7805`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9125`

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

- `market_context_high->crypto_major_4h` score `9.383` n `205` status `ready` deltaP `32.9269` edge `0.6154` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.7016` n `205` status `ready` deltaP `25.3049` edge `0.6709` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.3243` n `205` status `ready` deltaP `20.0609` edge `0.4682` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `3.5229` n `205` status `ready` deltaP `17.6876` edge `0.7077` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.2556` n `205` status `ready` deltaP `18.3232` edge `0.2586` maxDD `-5.0894`
- `market_context_high->index_4h` score `1.8154` n `205` status `ready` deltaP `14.4512` edge `0.1233` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.6484` n `206` status `ready` deltaP `13.1068` edge `0.1486` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.2426` n `206` status `ready` deltaP `10.1128` edge `0.1475` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.1091` n `205` status `ready` deltaP `18.2209` edge `0.4608` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.985` n `205` status `ready` deltaP `6.7229` edge `0.1601` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4081` n `206` status `ready` deltaP `8.2714` edge `0.0577` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.2544` n `206` status `ready` deltaP `4.6596` edge `0.0621` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1295` n `206` status `ready` deltaP `3.7571` edge `0.0232` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.412` n `205` status `ready` deltaP `12.1605` edge `0.0239` maxDD `-2.811`
- `market_context_high->crypto_major_24h` score `-0.6442` n `205` status `ready` deltaP `18.4345` edge `0.682` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-0.7381` n `205` status `ready` deltaP `10.8537` edge `0.1284` maxDD `-11.9812`
- `market_context_high->fx_1h` score `-0.7783` n `206` status `ready` deltaP `-0.4491` edge `0.0009` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8052` n `206` status `ready` deltaP `4.1466` edge `0.024` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.432` n `205` status `ready` deltaP `-4.6037` edge `-0.0005` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9371` n `206` status `ready` deltaP `1.792` edge `-0.0045` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
