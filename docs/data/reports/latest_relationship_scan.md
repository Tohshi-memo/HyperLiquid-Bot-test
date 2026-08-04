# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T21:07:33.667983+00:00`
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

- `market_context_high->unknown_24h` score `20.5752` n `73` status `ready` deltaP `19.2898` edge `1.5903` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3651` n `90` status `ready` deltaP `1.5955` edge `0.536` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4929` n `90` status `ready` deltaP `16.7751` edge `0.0972` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.5223` n `73` status `ready` deltaP `-3.7505` edge `0.2088` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5065` n `73` status `ready` deltaP `17.5822` edge `0.0683` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2378` n `90` status `ready` deltaP `5.4923` edge `0.0248` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.1377` n `90` status `ready` deltaP `14.3767` edge `0.0078` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1362` n `90` status `ready` deltaP `7.4551` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->crypto_alt_24h` score `0.0538` n `73` status `ready` deltaP `7.3035` edge `0.0986` maxDD `-4.2311`
- `market_context_high->metal_1h` score `-0.5153` n `90` status `ready` deltaP `-1.1577` edge `-0.0089` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5448` n `90` status `ready` deltaP `0.2928` edge `-0.0184` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7141` n `90` status `ready` deltaP `-2.159` edge `-0.0061` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7369` n `90` status `ready` deltaP `2.8794` edge `0.0098` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.857` n `90` status `ready` deltaP `4.2479` edge `0.0008` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6144` n `90` status `ready` deltaP `5.2495` edge `-0.0884` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0036` n `90` status `ready` deltaP `-11.6734` edge `-0.0536` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.2554` n `73` status `ready` deltaP `-9.4606` edge `-0.0066` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.384` n `90` status `ready` deltaP `-11.4105` edge `-0.0686` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.418` n `90` status `ready` deltaP `2.1989` edge `-0.2548` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-3.5109` n `73` status `ready` deltaP `10.5047` edge `-0.0239` maxDD `-30.6995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
