# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T07:22:28.391494+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.2705` n `75` status `ready` deltaP `5.8348` edge `0.2711` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.093` n `75` status `ready` deltaP `13.4327` edge `0.2339` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.9092` n `97` status `ready` deltaP `8.4265` edge `0.05` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.6249` n `94` status `ready` deltaP `13.3725` edge `0.0205` maxDD `-1.273`
- `market_context_high->index_1h` score `0.5704` n `97` status `ready` deltaP `11.9035` edge `0.0069` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5136` n `97` status `ready` deltaP `9.3108` edge `0.0034` maxDD `-0.4807`
- `market_context_high->crypto_major_4h` score `0.372` n `94` status `ready` deltaP `8.5042` edge `0.0931` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `0.3253` n `94` status `ready` deltaP `10.6383` edge `0.1025` maxDD `-5.5373`
- `market_context_high->unknown_24h` score `0.1167` n `75` status `ready` deltaP `14.6759` edge `-0.0693` maxDD `-0.1719`
- `market_context_high->metal_1h` score `-0.1288` n `97` status `ready` deltaP `3.1591` edge `0.0069` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.248` n `94` status `ready` deltaP `2.7309` edge `0.0005` maxDD `-0.3734`
- `market_context_high->equity_4h` score `-0.2498` n `94` status `ready` deltaP `1.1611` edge `0.0619` maxDD `-2.5696`
- `market_context_high->commodity_4h` score `-0.2551` n `94` status `ready` deltaP `5.6143` edge `0.0149` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.3159` n `97` status `ready` deltaP `2.71` edge `0.0216` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4533` n `97` status `ready` deltaP `-3.4416` edge `0.001` maxDD `-0.2273`
- `market_context_high->crypto_major_1h` score `-0.5099` n `97` status `ready` deltaP `0.9306` edge `0.0129` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5378` n `94` status `ready` deltaP `1.0249` edge `0.0099` maxDD `-0.2574`
- `market_context_high->metal_24h` score `-0.8868` n `75` status `ready` deltaP `-1.3911` edge `0.0452` maxDD `-4.3026`
- `market_context_high->commodity_1h` score `-0.9307` n `97` status `ready` deltaP `-7.5823` edge `-0.0075` maxDD `-1.5684`
- `market_context_high->index_24h` score `-2.9694` n `75` status `ready` deltaP `-8.9497` edge `-0.1384` maxDD `-6.9435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
