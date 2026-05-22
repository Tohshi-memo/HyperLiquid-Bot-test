# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T15:22:17.287629+00:00`
- Price records: `672`
- Market context records: `1538`
- Flow alert records: `6341`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8803`

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

- `market_context_high->metal_24h` score `12.6259` n `178` status `ready` deltaP `22.9362` edge `0.9993` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.5814` n `178` status `ready` deltaP `28.5229` edge `0.9766` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.777` n `178` status `ready` deltaP `27.7563` edge `0.7429` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.101` n `178` status `ready` deltaP `20.607` edge `0.313` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6662` n `178` status `ready` deltaP `13.5397` edge `0.3646` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.7848` n `178` status `ready` deltaP `17.4606` edge `0.0539` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1665` n `199` status `ready` deltaP `4.0239` edge `0.0965` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.4631` n `199` status `ready` deltaP `11.5777` edge `0.1954` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.5367` n `199` status `ready` deltaP `7.6028` edge `0.1514` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.5382` n `199` status `ready` deltaP `-0.0805` edge `0.0339` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5907` n `199` status `ready` deltaP `-1.3954` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7512` n `199` status `ready` deltaP `0.0256` edge `0.0004` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.7577` n `199` status `ready` deltaP `-0.6469` edge `-0.0007` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7641` n `199` status `ready` deltaP `4.6987` edge `0.0043` maxDD `-6.3532`
- `market_context_high->equity_1h` score `-0.8751` n `199` status `ready` deltaP `-1.6316` edge `0.0188` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0665` n `199` status `ready` deltaP `-1.6414` edge `0.0099` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.2937` n `199` status `ready` deltaP `-9.0253` edge `-0.0128` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.3994` n `199` status `ready` deltaP `-4.5923` edge `0.0229` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.4929` n `199` status `ready` deltaP `9.2965` edge `0.0828` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.3136` n `199` status `ready` deltaP `-15.9196` edge `-0.1124` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
