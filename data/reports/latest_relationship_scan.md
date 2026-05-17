# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T18:22:17.373480+00:00`
- Price records: `672`
- Market context records: `1038`
- Flow alert records: `4896`
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

- `market_context_high->crypto_major_24h` score `14.3563` n `182` status `ready` deltaP `33.2264` edge `1.0337` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5766` n `182` status `ready` deltaP `11.4122` edge `0.4287` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.3266` n `182` status `ready` deltaP `11.287` edge `0.2808` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.4962` n `182` status `ready` deltaP `10.578` edge `0.2183` maxDD `-2.1308`
- `market_context_high->metal_24h` score `1.0082` n `182` status `ready` deltaP `-6.3314` edge `0.3981` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0602` n `183` status `ready` deltaP `5.5733` edge `0.0007` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4328` n `183` status `ready` deltaP `4.4288` edge `0.0124` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6165` n `183` status `ready` deltaP `0.0572` edge `0.0239` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6651` n `183` status `ready` deltaP `1.1788` edge `0.0175` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-1.0444` n `183` status `ready` deltaP `5.8277` edge `-0.0019` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.0507` n `182` status `ready` deltaP `1.4674` edge `0.0023` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.343` n `183` status `ready` deltaP `0.1465` edge `-0.0043` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.37` n `182` status `ready` deltaP `-0.2144` edge `0.0349` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.5467` n `182` status `ready` deltaP `1.9515` edge `0.0733` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.9306` n `183` status `ready` deltaP `2.7813` edge `-0.0346` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.8231` n `182` status `ready` deltaP `1.2681` edge `0.0341` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.0819` n `182` status `ready` deltaP `7.5114` edge `0.0637` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.1736` n `182` status `ready` deltaP `3.1293` edge `-0.0201` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5526` n `182` status `ready` deltaP `-4.6787` edge `0.0519` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9458` n `182` status `ready` deltaP `-0.9967` edge `-0.1559` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
