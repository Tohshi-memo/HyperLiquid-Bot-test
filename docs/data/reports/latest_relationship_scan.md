# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T18:51:05.364683+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11830`

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

- `market_context_high->unknown_24h` score `230.9411` n `88` status `ready` deltaP `-21.512` edge `30.0196` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `8.0653` n `88` status `ready` deltaP `41.3037` edge `0.4025` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.4776` n `125` status `ready` deltaP `14.2268` edge `0.0754` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0446` n `128` status `ready` deltaP `2.6572` edge `0.0197` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.3158` n `125` status `ready` deltaP `4.2073` edge `0.0061` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.3572` n `128` status `ready` deltaP `0.814` edge `0.0013` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.4516` n `128` status `ready` deltaP `2.8911` edge `-0.0056` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.7918` n `128` status `ready` deltaP `-6.9517` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.9156` n `125` status `ready` deltaP `7.9805` edge `-0.0132` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.2972` n `88` status `ready` deltaP `-5.9344` edge `0.034` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6527` n `128` status `ready` deltaP `-9.4966` edge `-0.0446` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.886` n `88` status `ready` deltaP `-9.0909` edge `0.07` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.9494` n `128` status `ready` deltaP `-1.5297` edge `-0.0183` maxDD `-7.0497`
- `market_context_high->index_4h` score `-2.0094` n `125` status `ready` deltaP `-11.5659` edge `-0.0091` maxDD `-0.8328`
- `market_context_high->crypto_major_1h` score `-2.1288` n `128` status `ready` deltaP `-5.7682` edge `-0.0323` maxDD `-5.5318`
- `market_context_high->index_24h` score `-2.1745` n `88` status `ready` deltaP `-8.144` edge `-0.0705` maxDD `-2.3194`
- `market_context_high->crypto_major_4h` score `-3.7603` n `125` status `ready` deltaP `-1.8476` edge `-0.0653` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-5.1521` n `88` status `ready` deltaP `-6.7392` edge `-0.0299` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.1565` n `128` status `ready` deltaP `0.5474` edge `-0.5543` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-7.8893` n `125` status `ready` deltaP `-10.9902` edge `-0.0963` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
