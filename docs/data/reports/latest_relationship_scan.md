# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T17:52:17.462194+00:00`
- Price records: `672`
- Market context records: `1036`
- Flow alert records: `4890`
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

- `market_context_high->crypto_major_24h` score `14.3194` n `182` status `ready` deltaP `33.1103` edge `1.0314` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5423` n `182` status `ready` deltaP `11.3742` edge `0.4261` maxDD `-9.5387`
- `market_context_high->equity_24h` score `3.406` n `182` status `ready` deltaP `11.5446` edge `0.2857` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.5457` n `182` status `ready` deltaP `10.8361` edge `0.2207` maxDD `-2.1308`
- `market_context_high->metal_24h` score `1.129` n `182` status `ready` deltaP `-6.0824` edge `0.4065` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0765` n `183` status `ready` deltaP `5.2739` edge `0.0006` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4364` n `183` status `ready` deltaP `4.4288` edge `0.0121` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6321` n `183` status `ready` deltaP `0.0572` edge `0.0226` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.6651` n `183` status `ready` deltaP `1.1788` edge `0.0175` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0239` n `182` status `ready` deltaP `1.7723` edge `0.0025` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.0924` n `183` status `ready` deltaP `5.8277` edge `-0.0059` maxDD `-7.9187`
- `market_context_high->index_4h` score `-1.3942` n `182` status `ready` deltaP `-0.3669` edge `0.0339` maxDD `-6.1444`
- `market_context_high->crypto_alt_1h` score `-1.4029` n `183` status `ready` deltaP `-0.0032` edge `-0.0083` maxDD `-5.3538`
- `market_context_high->equity_4h` score `-1.5817` n `182` status `ready` deltaP `1.7991` edge `0.0714` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.963` n `183` status `ready` deltaP `2.4819` edge `-0.0353` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.9231` n `182` status `ready` deltaP `0.9632` edge `0.0278` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.1563` n `182` status `ready` deltaP `7.5114` edge `0.0575` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.1628` n `182` status `ready` deltaP `3.3063` edge `-0.0199` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5296` n `182` status `ready` deltaP `-4.5263` edge `0.0528` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9679` n `182` status `ready` deltaP `-1.3016` edge `-0.1567` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
