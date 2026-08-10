# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T18:52:36.865049+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->equity_24h` score `1.5741` n `139` status `ready` deltaP `4.4038` edge `0.4277` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.8625` n `175` status `ready` deltaP `11.9007` edge `0.064` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.778` n `139` status `ready` deltaP `19.3347` edge `0.0167` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7441` n `182` status `ready` deltaP `9.9461` edge `0.03` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.1264` n `182` status `ready` deltaP `4.2986` edge `0.0003` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1437` n `175` status `ready` deltaP `6.1498` edge `0.007` maxDD `-0.4647`
- `market_context_high->index_24h` score `-0.2233` n `139` status `ready` deltaP `4.0996` edge `0.1072` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6163` n `182` status `ready` deltaP `-4.1406` edge `-0.0037` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.78` n `139` status `ready` deltaP `1.5361` edge `0.0572` maxDD `-2.9283`
- `market_context_high->metal_1h` score `-0.8592` n `182` status `ready` deltaP `-5.2872` edge `-0.0113` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.0329` n `182` status `ready` deltaP `-3.2358` edge `-0.0161` maxDD `-5.247`
- `market_context_high->index_4h` score `-1.2191` n `175` status `ready` deltaP `-1.9268` edge `-0.0105` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.7933` n `182` status `ready` deltaP `-10.2323` edge `-0.0448` maxDD `-6.3518`
- `market_context_high->metal_4h` score `-2.0239` n `175` status `ready` deltaP `-6.9582` edge `-0.0367` maxDD `-6.1111`
- `market_context_high->crypto_major_24h` score `-3.2468` n `139` status `ready` deltaP `0.8491` edge `-0.0268` maxDD `-14.2873`
- `market_context_high->equity_4h` score `-3.2519` n `175` status `ready` deltaP `-11.2604` edge `-0.105` maxDD `-9.9471`
- `market_context_high->crypto_major_1h` score `-3.8776` n `182` status `ready` deltaP `-10.4873` edge `-0.0628` maxDD `-11.9002`
- `market_context_high->crypto_alt_24h` score `-3.9319` n `139` status `ready` deltaP `-10.658` edge `-0.1123` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-6.0076` n `175` status `ready` deltaP `-11.6795` edge `-0.1358` maxDD `-16.2912`
- `market_context_high->commodity_24h` score `-8.6876` n `139` status `ready` deltaP `-5.5409` edge `-0.2053` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
