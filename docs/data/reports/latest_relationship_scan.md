# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T19:43:20.272143+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13790`

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

- `market_context_high->unknown_1h` score `1.2204` n `133` status `ready` deltaP `8.3878` edge `0.0685` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.208` n `133` status `ready` deltaP `10.0392` edge `0.01` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1818` n `133` status `ready` deltaP `10.7559` edge `0.0047` maxDD `-0.9144`
- `market_context_high->unknown_4h` score `-0.0158` n `133` status `ready` deltaP `21.0904` edge `-0.098` maxDD `-0.5133`
- `market_context_high->fx_1h` score `-0.1245` n `133` status `ready` deltaP `2.3288` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2186` n `133` status `ready` deltaP `6.5643` edge `0.0352` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3441` n `133` status `ready` deltaP `0.5324` edge `-0.0058` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.4859` n `133` status `ready` deltaP `3.27` edge `-0.0225` maxDD `-1.5942`
- `market_context_high->crypto_alt_1h` score `-0.6008` n `133` status `ready` deltaP `0.7193` edge `0.0253` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.6029` n `133` status `ready` deltaP `2.4689` edge `0.0098` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6762` n `133` status `ready` deltaP `-1.3135` edge `0.0071` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6776` n `133` status `ready` deltaP `-4.5709` edge `0.0002` maxDD `-1.1941`
- `market_context_high->commodity_24h` score `-0.906` n `105` status `ready` deltaP `0.7689` edge `0.1027` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.1617` n `133` status `ready` deltaP `-0.9511` edge `-0.0401` maxDD `-4.1996`
- `market_context_high->crypto_alt_4h` score `-1.435` n `133` status `ready` deltaP `3.1359` edge `-0.0135` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.8643` n `133` status `ready` deltaP `-2.4299` edge `0.0577` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.6097` n `105` status `ready` deltaP `-8.3086` edge `-0.0011` maxDD `-2.2121`
- `market_context_high->crypto_major_4h` score `-4.0185` n `133` status `ready` deltaP `-0.5822` edge `-0.2289` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.2605` n `105` status `ready` deltaP `-6.4633` edge `-0.0529` maxDD `-18.6848`
- `market_context_high->metal_24h` score `-4.7755` n `105` status `ready` deltaP `-18.4574` edge `-0.1584` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
