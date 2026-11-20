# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T04:07:32.507459+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2778`

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

- `market_context_high->unknown_1h` score `11997.6068` n `108` status `ready` deltaP `1.1367` edge `999.8128` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7455.1473` n `108` status `ready` deltaP `-0.0903` edge `621.2913` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `18.87` n `96` status `ready` deltaP `35.2431` edge `1.5235` maxDD `-12.2098`
- `market_context_high->crypto_alt_24h` score `8.4292` n `96` status `ready` deltaP `20.3125` edge `1.264` maxDD `-21.8334`
- `market_context_high->crypto_major_4h` score `1.2224` n `108` status `ready` deltaP `3.7883` edge `0.3585` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.8607` n `108` status `ready` deltaP `5.1603` edge `0.2449` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.7995` n `108` status `ready` deltaP `20.0034` edge `0.0677` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0332` n `108` status `ready` deltaP `6.2874` edge `0.0218` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2468` n `108` status `ready` deltaP `3.5651` edge `0.0058` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.3147` n `108` status `ready` deltaP `4.5465` edge `0.069` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.7418` n `108` status `ready` deltaP `-1.935` edge `0.04` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.111` n `108` status `ready` deltaP `6.6423` edge `0.041` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6588` n `108` status `ready` deltaP `-11.9982` edge `-0.0023` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8344` n `108` status `ready` deltaP `-2.2245` edge `-0.0037` maxDD `-4.7471`
- `market_context_high->metal_24h` score `-2.4107` n `96` status `ready` deltaP `16.3194` edge `0.151` maxDD `-26.855`
- `market_context_high->fx_4h` score `-2.4198` n `108` status `ready` deltaP `-15.56` edge `-0.0049` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4343` n `108` status `ready` deltaP `-9.969` edge `-0.0282` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-6.7533` n `96` status `ready` deltaP `-19.2708` edge `-0.007` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1224` n `108` status `ready` deltaP `-29.2626` edge `-0.1125` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.3739` n `108` status `ready` deltaP `-6.8992` edge `-0.053` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
