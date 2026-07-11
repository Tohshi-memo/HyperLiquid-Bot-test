# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T04:37:29.076468+00:00`
- Price records: `672`
- Market context records: `6356`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `14.9865` n `32` status `ready` deltaP `41.4931` edge `0.987` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.2027` n `32` status `ready` deltaP `51.3889` edge `0.1743` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.46` n `32` status `ready` deltaP `17.7083` edge `0.5317` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.09` n `32` status `ready` deltaP `42.4543` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.759` n `32` status `ready` deltaP `32.6389` edge `0.1162` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3632` n `32` status `ready` deltaP `28.4431` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4905` n `32` status `ready` deltaP `14.5771` edge `0.1406` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8894` n `32` status `ready` deltaP `11.3211` edge `0.0847` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.7188` n `201` status `ready` deltaP `14.5575` edge `0.0425` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0268` n `201` status `ready` deltaP `7.135` edge `0.0223` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `-0.0392` n `213` status `ready` deltaP `-7.7331` edge `0.1491` maxDD `-3.7317`
- `market_context_high->commodity_24h` score `-0.5598` n `129` status `ready` deltaP `-4.4493` edge `0.1443` maxDD `-6.2457`
- `market_context_high->metal_1h` score `-0.6084` n `213` status `ready` deltaP `3.6842` edge `0.0025` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6507` n `213` status `ready` deltaP `-2.0719` edge `-0.0013` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.6603` n `129` status `ready` deltaP `14.5631` edge `0.0751` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.7027` n `32` status `ready` deltaP `0.5208` edge `-0.0064` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.7059` n `32` status `ready` deltaP `5.6325` edge `-0.0619` maxDD `-0.7581`
- `market_context_high->fx_1h` score `-0.746` n `213` status `ready` deltaP `-1.017` edge `-0.002` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.773` n `32` status `ready` deltaP `-3.5928` edge `-0.0254` maxDD `-1.6464`
- `market_context_high->unknown_4h` score `-0.8715` n `201` status `ready` deltaP `-12.5743` edge `0.2295` maxDD `-11.925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
