# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T19:52:20.594045+00:00`
- Price records: `672`
- Market context records: `2070`
- Flow alert records: `7855`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9145`

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

- `market_context_high->crypto_major_4h` score `9.7284` n `206` status `ready` deltaP `34.6347` edge `0.6328` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.0698` n `206` status `ready` deltaP `26.9077` edge `0.6909` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.6978` n `206` status `ready` deltaP `21.9852` edge `0.4865` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `6.2343` n `205` status `ready` deltaP `20.1098` edge `0.9175` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5199` n `206` status `ready` deltaP `19.302` edge `0.2741` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0366` n `206` status `ready` deltaP `15.4467` edge `0.1351` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.8258` n `206` status `ready` deltaP `14.005` edge `0.1574` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.7854` n `205` status `ready` deltaP `20.9891` edge `0.4987` maxDD `-33.1875`
- `market_context_high->index_24h` score `1.504` n `205` status `ready` deltaP `9.4911` edge `0.1849` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `1.4716` n `206` status `ready` deltaP `11.011` edge `0.1606` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.5768` n `205` status `ready` deltaP `21.2026` edge `0.7653` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `0.4643` n `206` status `ready` deltaP `5.7075` edge `0.0726` maxDD `-3.0902`
- `market_context_high->equity_1h` score `0.4249` n `206` status `ready` deltaP `8.1217` edge `0.0601` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.0684` n `206` status `ready` deltaP `4.2062` edge `0.0253` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.2472` n `205` status `ready` deltaP `13.8906` edge `0.0261` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5633` n `206` status `ready` deltaP `11.6741` edge `0.1375` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7524` n `206` status `ready` deltaP `4.1466` edge `0.0284` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8287` n `206` status `ready` deltaP `-1.0479` edge `0.0007` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.4359` n `206` status `ready` deltaP `-4.6975` edge `-0.0002` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.8014` n `205` status `ready` deltaP `11.0549` edge `0.1663` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
