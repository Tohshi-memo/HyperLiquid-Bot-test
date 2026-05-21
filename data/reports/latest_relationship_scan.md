# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T19:37:19.378637+00:00`
- Price records: `672`
- Market context records: `1454`
- Flow alert records: `6097`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `13.1338` n `162` status `ready` deltaP `28.8773` edge `1.1036` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0378` n `162` status `ready` deltaP `27.5463` edge `0.9327` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.5736` n `162` status `ready` deltaP `14.892` edge `1.0319` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.3508` n `162` status `ready` deltaP `19.8302` edge `0.339` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.2894` n `162` status `ready` deltaP `13.0402` edge `0.5032` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6152` n `224` status `ready` deltaP `7.3497` edge `0.1686` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2377` n `162` status `ready` deltaP `11.4776` edge `0.0482` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0383` n `227` status `ready` deltaP `4.2616` edge `0.0149` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0636` n `227` status `ready` deltaP `2.4479` edge `0.0384` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.3042` n `224` status `ready` deltaP `11.1607` edge `0.2322` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4068` n `224` status `ready` deltaP `1.3502` edge `0.066` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4801` n `227` status `ready` deltaP `0.6265` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.524` n `227` status `ready` deltaP `2.0549` edge `0.045` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0036` n `224` status `ready` deltaP `-3.4516` edge `-0.0086` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.0817` n `227` status `ready` deltaP `5.4209` edge `0.0073` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.1453` n `224` status `ready` deltaP `5.3463` edge `0.1398` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.2524` n `227` status `ready` deltaP `-1.5504` edge `-0.0019` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5882` n `227` status `ready` deltaP `-0.7294` edge `0.0082` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7071` n `224` status `ready` deltaP `8.4494` edge `0.0706` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.9756` n `224` status `ready` deltaP `-12.0427` edge `-0.0741` maxDD `-16.0917`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
