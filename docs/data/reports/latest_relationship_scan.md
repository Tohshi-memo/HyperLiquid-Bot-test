# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T22:22:36.199807+00:00`
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

- `market_context_high->fx_24h` score `1.0365` n `145` status `ready` deltaP `20.4064` edge `0.0311` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.8465` n `176` status `ready` deltaP `11.6408` edge `0.0644` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6549` n `180` status `ready` deltaP `8.9055` edge `0.0295` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0122` n `176` status `ready` deltaP `7.7189` edge `0.0075` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1161` n `180` status `ready` deltaP `4.5276` edge `0.0001` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.686` n `180` status `ready` deltaP `-5.4524` edge `-0.0037` maxDD `-0.832`
- `market_context_high->index_24h` score `-0.7493` n `145` status `ready` deltaP `-1.8789` edge `0.0696` maxDD `-5.9181`
- `market_context_high->index_4h` score `-0.9901` n `176` status `ready` deltaP `-4.9612` edge `-0.0139` maxDD `-1.3973`
- `market_context_high->metal_24h` score `-1.089` n `145` status `ready` deltaP `2.5482` edge `0.0247` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.0958` n `180` status `ready` deltaP `-4.0252` edge `-0.01` maxDD `-5.9591`
- `market_context_high->metal_1h` score `-1.2564` n `180` status `ready` deltaP `-4.8137` edge `-0.009` maxDD `-2.0884`
- `market_context_high->equity_24h` score `-2.7899` n `145` status `ready` deltaP `-1.7235` edge `0.146` maxDD `-29.7081`
- `market_context_high->crypto_alt_1h` score `-2.8055` n `180` status `ready` deltaP `-10.7318` edge `-0.0425` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.0708` n `176` status `ready` deltaP `-6.7212` edge `-0.0347` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.7135` n `180` status `ready` deltaP `-9.8303` edge `-0.0535` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-3.9183` n `176` status `ready` deltaP `-14.0937` edge `-0.1242` maxDD `-13.7353`
- `market_context_high->crypto_major_24h` score `-4.0628` n `145` status `ready` deltaP `-4.4642` edge `-0.1099` maxDD `-23.1638`
- `market_context_high->commodity_24h` score `-6.4253` n `145` status `ready` deltaP `-0.4853` edge `-0.0834` maxDD `-44.3029`
- `market_context_high->crypto_alt_4h` score `-6.7427` n `176` status `ready` deltaP `-14.1353` edge `-0.1508` maxDD `-18.6816`
- `market_context_high->crypto_alt_24h` score `-7.084` n `145` status `ready` deltaP `-12.8226` edge `-0.2013` maxDD `-18.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
