# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T19:37:20.380881+00:00`
- Price records: `672`
- Market context records: `2488`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.3767` n `124` status `ready` deltaP `19.8869` edge `0.3483` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.1336` n `138` status `ready` deltaP `21.2045` edge `0.471` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8235` n `138` status `ready` deltaP `18.0784` edge `0.3791` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.9873` n `124` status `ready` deltaP `11.3911` edge `0.5681` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.2614` n `138` status `ready` deltaP `8.5786` edge `0.1529` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.4478` n `150` status `ready` deltaP `6.3533` edge `0.1137` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.4066` n `150` status `ready` deltaP `6.8703` edge `0.1075` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.0616` n `124` status `ready` deltaP `4.3514` edge `0.0742` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0177` n `124` status `ready` deltaP `1.4504` edge `0.6838` maxDD `-43.6595`
- `market_context_high->equity_24h` score `-0.1557` n `124` status `ready` deltaP `18.4084` edge `0.017` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1917` n `138` status `ready` deltaP `5.7264` edge `0.0214` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3376` n `150` status `ready` deltaP `0.8842` edge `0.0043` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.4953` n `150` status `ready` deltaP `1.9182` edge `0.0179` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.5117` n `150` status `ready` deltaP `3.1697` edge `0.0011` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5313` n `150` status `ready` deltaP `-0.0559` edge `0.0055` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.6027` n `138` status `ready` deltaP `0.0` edge `0.0087` maxDD `-0.8774`
- `market_context_high->metal_1h` score `-0.755` n `150` status `ready` deltaP `0.98` edge `0.0065` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.8603` n `150` status `ready` deltaP `-0.1257` edge `0.013` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9042` n `124` status `ready` deltaP `2.8506` edge `0.0036` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9918` n `138` status `ready` deltaP `2.8941` edge `0.0368` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
