# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T10:37:30.017521+00:00`
- Price records: `672`
- Market context records: `6700`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_24h` score `0.8662` n `184` status `ready` deltaP `0.5208` edge `0.4828` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.1519` n `184` status `ready` deltaP `8.8291` edge `0.0466` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `0.0496` n `184` status `ready` deltaP `9.4279` edge `0.1281` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `0.0439` n `184` status `ready` deltaP `5.757` edge `0.0417` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3842` n `184` status `ready` deltaP `0.0488` edge `0.0003` maxDD `-0.6567`
- `market_context_high->unknown_1h` score `-0.5281` n `184` status `ready` deltaP `-6.7658` edge `0.0912` maxDD `-3.2083`
- `market_context_high->index_1h` score `-0.5546` n `184` status `ready` deltaP `-0.4328` edge `0.0032` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.5622` n `184` status `ready` deltaP `-3.1893` edge `0.0017` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6678` n `184` status `ready` deltaP `-0.781` edge `-0.0121` maxDD `-2.1314`
- `market_context_high->index_4h` score `-1.003` n `184` status `ready` deltaP `9.1928` edge `-0.0019` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.0487` n `184` status `ready` deltaP `2.5514` edge `-0.0017` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.3317` n `184` status `ready` deltaP `6.8398` edge `-0.0014` maxDD `-2.8612`
- `market_context_high->crypto_major_4h` score `-1.6511` n `184` status `ready` deltaP `7.0454` edge `0.0728` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.8096` n `184` status `ready` deltaP `-5.4481` edge `-0.0462` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.8672` n `184` status `ready` deltaP `5.1299` edge `0.0666` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.2768` n `184` status `ready` deltaP `-3.2476` edge `0.0158` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-4.055` n `184` status `ready` deltaP `-17.4245` edge `0.0148` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.6772` n `184` status `ready` deltaP `-9.3825` edge `-0.003` maxDD `-7.2707`
- `market_context_high->equity_4h` score `-5.5345` n `184` status `ready` deltaP `5.8059` edge `-0.073` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0927` n `184` status `ready` deltaP `-6.9596` edge `-0.0144` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
