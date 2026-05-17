# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T21:37:12.071876+00:00`
- Price records: `672`
- Market context records: `1053`
- Flow alert records: `4937`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8668`

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

- `market_context_high->crypto_major_24h` score `14.0959` n `182` status `ready` deltaP `32.3711` edge `1.0177` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.4576` n `182` status `ready` deltaP `11.6655` edge `0.4171` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.6722` n `182` status `ready` deltaP `9.5715` edge `0.2377` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.1331` n `182` status `ready` deltaP `8.8592` edge `0.1995` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.1472` n `182` status `ready` deltaP `-7.9894` edge `0.3374` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0551` n `184` status `ready` deltaP `5.7017` edge `0.0005` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4243` n `184` status `ready` deltaP `4.4454` edge `0.013` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6731` n `184` status `ready` deltaP `-0.6509` edge `0.0239` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6874` n `184` status `ready` deltaP `0.9145` edge `0.0174` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-0.9984` n `184` status `ready` deltaP `5.757` edge `0.0024` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.0937` n `183` status `ready` deltaP `0.9604` edge `0.0021` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.2951` n `184` status `ready` deltaP `0.0846` edge `0.0001` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.3287` n `183` status `ready` deltaP `-0.0733` edge `0.0374` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.7477` n `183` status `ready` deltaP `0.7147` edge `0.0648` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.9297` n `184` status `ready` deltaP `2.763` edge `-0.0344` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.8634` n `183` status `ready` deltaP `0.9138` edge `0.0331` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.2096` n `182` status `ready` deltaP `2.6023` edge `-0.0212` maxDD `-19.2774`
- `market_context_high->crypto_major_4h` score `-3.4069` n `183` status `ready` deltaP `6.2091` edge `0.0453` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.4849` n `183` status `ready` deltaP `-4.4315` edge `0.0559` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-4.0479` n `183` status `ready` deltaP `-1.1596` edge `-0.1679` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
