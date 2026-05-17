# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T19:52:19.691390+00:00`
- Price records: `672`
- Market context records: `1045`
- Flow alert records: `4915`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8652`

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

- `market_context_high->crypto_major_24h` score `14.273` n `182` status `ready` deltaP `32.9352` edge `1.0287` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.569` n `182` status `ready` deltaP `11.5278` edge `0.4273` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.0384` n `182` status `ready` deltaP `10.5042` edge `0.262` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.3303` n `182` status `ready` deltaP `9.7936` edge `0.2097` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.6285` n `182` status `ready` deltaP `-7.088` edge `0.3715` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0699` n `184` status `ready` deltaP `5.4023` edge `0.0006` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4111` n `184` status `ready` deltaP `4.5951` edge `0.0131` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5749` n `184` status `ready` deltaP `0.2473` edge `0.0261` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.7054` n `184` status `ready` deltaP `0.7648` edge `0.0169` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-0.9901` n `184` status `ready` deltaP `5.9067` edge `0.0021` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.1275` n `182` status `ready` deltaP `0.5528` edge `0.002` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.2807` n `184` status `ready` deltaP `0.2343` edge `0.0003` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.346` n `182` status `ready` deltaP `-0.2144` edge `0.0369` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.5891` n `182` status `ready` deltaP `1.6467` edge `0.0718` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.8782` n `184` status `ready` deltaP `3.2121` edge `-0.0331` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.7145` n `182` status `ready` deltaP `1.7254` edge `0.0401` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.1605` n `182` status `ready` deltaP `7.0541` edge `0.0602` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.207` n `182` status `ready` deltaP `2.5915` edge `-0.0208` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.6146` n `182` status `ready` deltaP `-5.2885` edge `0.0508` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9527` n `182` status `ready` deltaP `-0.8443` edge `-0.1578` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
