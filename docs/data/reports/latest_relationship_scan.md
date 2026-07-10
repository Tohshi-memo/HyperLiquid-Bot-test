# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T12:37:28.446001+00:00`
- Price records: `672`
- Market context records: `6283`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `15.2037` n `32` status `ready` deltaP `43.1434` edge `0.9941` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9649` n `32` status `ready` deltaP `50.6066` edge `0.1597` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1987` n `32` status `ready` deltaP `43.9787` edge `0.0613` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0838` n `32` status `ready` deltaP `16.5782` edge `0.491` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.6752` n `32` status `ready` deltaP `25.7961` edge `0.0715` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3344` n `32` status `ready` deltaP `28.1437` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6337` n `206` status `ready` deltaP `1.2529` edge `0.2286` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3377` n `32` status `ready` deltaP `13.6789` edge `0.127` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.827` n `32` status `ready` deltaP `11.0217` edge `0.0787` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.757` n `194` status `ready` deltaP `-1.6328` edge `0.3272` maxDD `-11.925`
- `market_context_high->equity_4h` score `0.2254` n `194` status `ready` deltaP `6.1353` edge `0.0696` maxDD `-2.671`
- `market_context_high->metal_4h` score `-0.2598` n `194` status `ready` deltaP `4.9519` edge `0.03` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.2841` n `32` status `ready` deltaP `7.5498` edge `0.0004` maxDD `-2.3058`
- `market_context_high->metal_24h` score `-0.3254` n `185` status `ready` deltaP `17.7038` edge `0.0971` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.4412` n `206` status `ready` deltaP `0.7441` edge `0.0043` maxDD `-0.682`
- `market_context_high->fx_1h` score `-0.4896` n `206` status `ready` deltaP `0.7165` edge `-0.001` maxDD `-0.5659`
- `news_risk_high->metal_1h` score `-0.6959` n `32` status `ready` deltaP `-2.3952` edge `-0.0235` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7472` n `206` status `ready` deltaP `2.4592` edge `-0.0009` maxDD `-1.8877`
- `market_context_high->crypto_alt_1h` score `-0.7575` n `206` status `ready` deltaP `6.5011` edge `0.0348` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8738` n `206` status `ready` deltaP `4.85` edge `0.0324` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
