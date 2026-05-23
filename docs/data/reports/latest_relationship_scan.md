# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T10:07:17.603168+00:00`
- Price records: `672`
- Market context records: `1620`
- Flow alert records: `6571`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8824`

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

- `market_context_high->metal_24h` score `10.6209` n `190` status `ready` deltaP `26.0673` edge `0.9366` maxDD `-11.6913`
- `market_context_high->index_24h` score `3.1231` n `190` status `ready` deltaP `18.2383` edge `0.2723` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.3985` n `191` status `ready` deltaP `11.5343` edge `0.1491` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.5295` n `191` status `ready` deltaP `13.9606` edge `0.3016` maxDD `-19.4759`
- `market_context_high->equity_24h` score `0.4597` n `190` status `ready` deltaP `16.8275` edge `0.3928` maxDD `-31.6675`
- `market_context_high->crypto_major_4h` score `0.3145` n `191` status `ready` deltaP `9.9908` edge `0.2446` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.2561` n `190` status `ready` deltaP `7.8545` edge `0.0312` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.2563` n `194` status `ready` deltaP `1.0803` edge `0.0623` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.4183` n `194` status `ready` deltaP `2.0094` edge `0.0326` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6398` n `194` status `ready` deltaP `0.8782` edge `0.004` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8053` n `194` status `ready` deltaP `-0.1173` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.8417` n `191` status `ready` deltaP `0.4733` edge `0.0356` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `-0.8666` n `190` status `ready` deltaP `22.2424` edge `0.5859` maxDD `-58.5122`
- `market_context_high->crypto_major_1h` score `-0.9021` n `194` status `ready` deltaP `-1.3303` edge `0.0289` maxDD `-6.1883`
- `market_context_high->commodity_1h` score `-1.0161` n `194` status `ready` deltaP `0.8643` edge `0.0017` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.2314` n `194` status `ready` deltaP `3.9401` edge `0.0047` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3828` n `191` status `ready` deltaP `-10.5279` edge `-0.0142` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4021` n `191` status `ready` deltaP `8.8111` edge `0.0936` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-2.5172` n `190` status `ready` deltaP `22.2917` edge `0.7521` maxDD `-83.5046`
- `market_context_high->commodity_4h` score `-5.1889` n `191` status `ready` deltaP `-13.8808` edge `-0.11` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
