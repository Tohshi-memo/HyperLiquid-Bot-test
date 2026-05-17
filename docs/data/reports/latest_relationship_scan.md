# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T17:07:13.393494+00:00`
- Price records: `672`
- Market context records: `1032`
- Flow alert records: `4880`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8635`

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

- `market_context_high->crypto_major_24h` score `14.26` n `182` status `ready` deltaP `32.9375` edge `1.0276` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.4946` n `182` status `ready` deltaP `11.3176` edge `0.4225` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.5219` n `182` status `ready` deltaP `11.928` edge `0.2928` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.6196` n `182` status `ready` deltaP `11.2202` edge `0.2243` maxDD `-2.1308`
- `market_context_high->metal_24h` score `1.3338` n `182` status `ready` deltaP `-5.7119` edge `0.4211` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.089` n `182` status `ready` deltaP `5.0487` edge `0.0005` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4323` n `182` status `ready` deltaP `4.5107` edge `0.0119` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6526` n `182` status `ready` deltaP `-0.0346` edge `0.0215` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6557` n `182` status `ready` deltaP `1.2963` edge `0.0175` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9837` n `182` status `ready` deltaP `2.2296` edge `0.0028` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.1473` n `182` status `ready` deltaP `5.6969` edge `-0.0096` maxDD `-7.9187`
- `market_context_high->crypto_alt_1h` score `-1.4345` n `182` status `ready` deltaP `-0.1431` edge `-0.01` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.4366` n `182` status `ready` deltaP `-0.6718` edge `0.0324` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.6589` n `182` status `ready` deltaP `1.4942` edge `0.067` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.9776` n `182` status `ready` deltaP `2.2538` edge `-0.035` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-3.1288` n `182` status `ready` deltaP `0.5059` edge `0.0137` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.1476` n `182` status `ready` deltaP `3.5697` edge `-0.0197` maxDD `-19.2774`
- `market_context_high->crypto_major_4h` score `-3.3669` n `182` status `ready` deltaP `7.0541` edge `0.043` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.56` n `182` status `ready` deltaP `-4.8312` edge `0.0523` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9892` n `182` status `ready` deltaP `-1.6065` edge `-0.1574` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
