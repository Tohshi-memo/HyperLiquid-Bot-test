# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T12:07:23.319109+00:00`
- Price records: `672`
- Market context records: `1421`
- Flow alert records: `6005`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_major_24h` score `11.8304` n `154` status `ready` deltaP `27.3539` edge `0.9167` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.5937` n `154` status `ready` deltaP `28.7811` edge `0.9759` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.5528` n `154` status `ready` deltaP `11.4673` edge `1.053` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7581` n `154` status `ready` deltaP `19.3813` edge `0.2926` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4351` n `154` status `ready` deltaP `12.5271` edge `0.3521` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8591` n `202` status `ready` deltaP `4.9324` edge `0.1217` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0527` n `154` status `ready` deltaP `9.3592` edge `0.0469` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.099` n `207` status `ready` deltaP `4.0579` edge `0.0112` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2174` n `207` status `ready` deltaP `2.5948` edge `0.0246` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3514` n `207` status `ready` deltaP `2.861` edge `-0.0018` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5482` n `207` status `ready` deltaP `0.6972` edge `0.0244` maxDD `-3.946`
- `market_context_high->commodity_1h` score `-0.7021` n `207` status `ready` deltaP `-0.8743` edge `0.0088` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.776` n `202` status `ready` deltaP `-0.6248` edge `0.0484` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.8647` n `207` status `ready` deltaP `4.4462` edge `-0.0103` maxDD `-6.0825`
- `market_context_high->crypto_major_1h` score `-1.1821` n `207` status `ready` deltaP `-1.97` edge `-0.0069` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.3019` n `202` status `ready` deltaP `7.3442` edge `0.1745` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3576` n `202` status `ready` deltaP `5.1376` edge `0.1235` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.6408` n `202` status `ready` deltaP `-4.4207` edge `-0.0102` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5844` n `202` status `ready` deltaP `-10.0896` edge `-0.0094` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8567` n `202` status `ready` deltaP `4.149` edge `-0.0059` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
