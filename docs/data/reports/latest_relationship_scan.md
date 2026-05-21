# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T04:07:14.421145+00:00`
- Price records: `672`
- Market context records: `1387`
- Flow alert records: `5907`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.4037` n `156` status `ready` deltaP `29.0197` edge `1.0367` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.7313` n `156` status `ready` deltaP `28.8061` edge `0.9872` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.64` n `156` status `ready` deltaP `12.6469` edge `1.0524` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.2341` n `156` status `ready` deltaP `20.3659` edge `0.3257` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6892` n `156` status `ready` deltaP `13.5283` edge `0.3666` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6716` n `184` status `ready` deltaP `8.5498` edge `0.1653` maxDD `-3.6396`
- `market_context_high->index_1h` score `0.0359` n `196` status `ready` deltaP `4.9493` edge `0.0165` maxDD `-1.7205`
- `market_context_high->fx_24h` score `0.023` n `156` status `ready` deltaP `9.7088` edge `0.0421` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0484` n `196` status `ready` deltaP `3.1528` edge `0.0308` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.1963` n `184` status `ready` deltaP `10.041` edge `0.0598` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.359` n `196` status `ready` deltaP `2.8565` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.4161` n `196` status `ready` deltaP `2.5022` edge `0.0357` maxDD `-3.6309`
- `market_context_high->index_4h` score `-0.4688` n `184` status `ready` deltaP `0.8152` edge `0.0644` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.5403` n `196` status `ready` deltaP `5.5909` edge `0.0013` maxDD `-4.2945`
- `market_context_high->commodity_1h` score `-0.8792` n `196` status `ready` deltaP `-1.497` edge `-0.0018` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.1463` n `184` status `ready` deltaP `8.225` edge `0.1816` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.1972` n `196` status `ready` deltaP `-0.0825` edge `0.0073` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.2208` n `184` status `ready` deltaP `4.7786` edge `0.1373` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.7657` n `184` status `ready` deltaP `-5.8324` edge `-0.0112` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.6322` n `184` status `ready` deltaP `-13.2821` edge `-0.0428` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
