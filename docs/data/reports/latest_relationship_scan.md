# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T18:37:21.154197+00:00`
- Price records: `672`
- Market context records: `2483`
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

- `market_context_high->unknown_24h` score `5.2795` n `124` status `ready` deltaP `19.8869` edge `0.3402` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.3114` n `136` status `ready` deltaP `21.8077` edge `0.4818` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.058` n `136` status `ready` deltaP `19.0907` edge `0.3919` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.8693` n `124` status `ready` deltaP `10.6967` edge `0.5576` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.4827` n `136` status `ready` deltaP `9.5409` edge `0.162` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.5905` n `146` status `ready` deltaP `8.1782` edge `0.1141` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.549` n `146` status `ready` deltaP `7.1077` edge `0.1171` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.0388` n `124` status `ready` deltaP `4.3514` edge `0.0723` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1557` n `124` status `ready` deltaP `18.4084` edge `0.017` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.2236` n `136` status `ready` deltaP `5.4878` edge `0.0189` maxDD `-2.3986`
- `market_context_high->crypto_alt_24h` score `-0.252` n `124` status `ready` deltaP `0.756` edge `0.6584` maxDD `-43.6595`
- `market_context_high->fx_1h` score `-0.2699` n `146` status `ready` deltaP `2.1409` edge `0.0046` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.4987` n `146` status `ready` deltaP `1.7554` edge `0.0187` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.5008` n `146` status `ready` deltaP `0.7259` edge `0.0069` maxDD `-3.0759`
- `market_context_high->commodity_1h` score `-0.557` n `146` status `ready` deltaP `2.4629` edge `0.0` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.578` n `146` status `ready` deltaP `-0.445` edge `0.0042` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.5962` n `136` status `ready` deltaP `0.1255` edge `0.0087` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8972` n `146` status `ready` deltaP `-0.6316` edge `0.0133` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9034` n `124` status `ready` deltaP `2.8506` edge `0.0037` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.91` n `136` status `ready` deltaP `3.5868` edge `0.039` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
