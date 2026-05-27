# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T10:37:19.926037+00:00`
- Price records: `672`
- Market context records: `2034`
- Flow alert records: `7746`
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

- `market_context_high->crypto_major_4h` score `8.8715` n `205` status `ready` deltaP `30.7927` edge `0.587` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3572` n `205` status `ready` deltaP `24.3903` edge `0.6483` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9053` n `205` status `ready` deltaP `18.9939` edge `0.4404` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9927` n `205` status `ready` deltaP `17.2561` edge `0.2438` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5201` n `205` status `ready` deltaP `12.328` edge `0.1431` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4522` n `205` status `ready` deltaP `12.9269` edge `0.1032` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2701` n `205` status `ready` deltaP `10.0825` edge `0.15` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `1.1355` n `203` status `ready` deltaP `17.0499` edge `0.513` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.4826` n `203` status `ready` deltaP `16.149` edge `0.4224` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.3806` n `203` status `ready` deltaP `4.5685` edge `0.1241` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.1972` n `205` status `ready` deltaP `6.7607` edge `0.0502` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0206` n `205` status `ready` deltaP `3.7462` edge `0.0487` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.281` n `205` status `ready` deltaP `2.7034` edge `0.0176` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5702` n `203` status `ready` deltaP `10.4064` edge `0.0214` maxDD `-2.7303`
- `market_context_high->fx_1h` score `-0.8398` n `205` status `ready` deltaP `-1.1421` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8826` n `205` status `ready` deltaP `3.8082` edge `0.0198` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.1474` n `205` status `ready` deltaP `8.872` edge `0.1075` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5695` n `205` status `ready` deltaP `-6.1281` edge `-0.0018` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.822` n `203` status `ready` deltaP `9.6295` edge `0.1325` maxDD `-20.5491`
- `market_context_high->commodity_1h` score `-1.8504` n `205` status `ready` deltaP `2.6055` edge `0.0012` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
