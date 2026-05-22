# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T17:52:17.503580+00:00`
- Price records: `672`
- Market context records: `1550`
- Flow alert records: `6372`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.3029` n `182` status `ready` deltaP `22.9491` edge `0.9723` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.9026` n `182` status `ready` deltaP `26.9974` edge `0.9302` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.2733` n `182` status `ready` deltaP `26.7399` edge `0.7077` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1184` n `182` status `ready` deltaP `20.7799` edge `0.3133` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6104` n `182` status `ready` deltaP `13.5474` edge `0.3599` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.6513` n `182` status `ready` deltaP `16.182` edge `0.0513` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.3097` n `199` status `ready` deltaP `5.2434` edge `0.1003` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.1849` n `199` status `ready` deltaP `13.1021` edge `0.2209` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.2789` n `199` status `ready` deltaP `8.9747` edge `0.1753` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.4564` n `199` status `ready` deltaP `0.5183` edge `0.0404` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6249` n `199` status `ready` deltaP `-1.9942` edge `-0.0036` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.6845` n `199` status `ready` deltaP `0.1016` edge `0.0037` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7532` n `199` status `ready` deltaP `4.9981` edge `0.0037` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7944` n `199` status `ready` deltaP `-0.4235` edge `-0.0002` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.8476` n `199` status `ready` deltaP `-1.3322` edge `0.0191` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.9761` n `199` status `ready` deltaP `-0.8929` edge `0.0165` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.3342` n `199` status `ready` deltaP `10.516` edge `0.0879` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3547` n `199` status `ready` deltaP `-10.0924` edge `-0.0135` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.4366` n `199` status `ready` deltaP `-4.5923` edge `0.0198` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.1636` n `199` status `ready` deltaP `-14.7001` edge `-0.1013` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
