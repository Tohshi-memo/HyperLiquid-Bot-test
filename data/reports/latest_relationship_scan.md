# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T20:38:00.594273+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `21.3847` n `71` status `ready` deltaP `19.5984` edge `1.6557` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3651` n `90` status `ready` deltaP `1.5955` edge `0.536` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4385` n `90` status `ready` deltaP `16.4702` edge `0.0947` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.3986` n `71` status `ready` deltaP `16.0773` edge `0.0645` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.3704` n `71` status `ready` deltaP `-4.9467` edge `0.1973` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.203` n `90` status `ready` deltaP `5.1929` edge `0.0239` maxDD `-1.3282`
- `market_context_high->crypto_alt_24h` score `0.1813` n `71` status `ready` deltaP `7.8051` edge `0.1116` maxDD `-4.2311`
- `market_context_high->fx_4h` score `0.1384` n `90` status `ready` deltaP `14.3767` edge `0.0079` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.135` n `90` status `ready` deltaP `7.4551` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->metal_1h` score `-0.5317` n `90` status `ready` deltaP `-1.4571` edge `-0.009` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5635` n `90` status `ready` deltaP `-0.0066` edge `-0.0188` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7164` n `90` status `ready` deltaP `-2.159` edge `-0.0064` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7574` n `90` status `ready` deltaP `2.5745` edge `0.0092` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8484` n `90` status `ready` deltaP `4.2479` edge `0.0019` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6495` n `90` status `ready` deltaP `4.9501` edge `-0.0909` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0059` n `90` status `ready` deltaP `-11.6734` edge `-0.0539` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.378` n `71` status `ready` deltaP `-10.3482` edge `-0.0164` maxDD `-7.8922`
- `market_context_high->commodity_24h` score `-2.967` n `71` status `ready` deltaP `11.7396` edge `-0.0015` maxDD `-28.2388`
- `market_context_high->unknown_1h` score `-3.3857` n `90` status `ready` deltaP `2.4983` edge `-0.2541` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4044` n `90` status `ready` deltaP `-11.5602` edge `-0.0693` maxDD `-7.6533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
