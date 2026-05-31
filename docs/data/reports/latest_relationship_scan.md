# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T18:50:02.649745+00:00`
- Price records: `672`
- Market context records: `2484`
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

- `market_context_high->unknown_24h` score `5.2951` n `124` status `ready` deltaP `19.8869` edge `0.3415` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.2908` n `136` status `ready` deltaP `21.6553` edge `0.4811` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.0568` n `136` status `ready` deltaP `19.0907` edge `0.3918` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.8947` n `124` status `ready` deltaP `10.8703` edge `0.5597` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.4525` n `136` status `ready` deltaP `9.3885` edge `0.1605` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.5265` n `147` status `ready` deltaP `7.7681` edge `0.1115` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.5013` n `147` status `ready` deltaP `6.707` edge `0.1158` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.0472` n `124` status `ready` deltaP `4.3514` edge `0.073` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1569` n `124` status `ready` deltaP `18.4084` edge `0.0169` maxDD `-6.8828`
- `market_context_high->crypto_alt_24h` score `-0.1993` n `124` status `ready` deltaP `0.9296` edge `0.664` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.2259` n `136` status `ready` deltaP `5.4878` edge `0.0186` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.2815` n `147` status `ready` deltaP `1.9319` edge `0.0045` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.463` n `147` status `ready` deltaP `1.9319` edge `0.0205` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.492` n `147` status `ready` deltaP `0.9257` edge `0.0067` maxDD `-3.0759`
- `market_context_high->commodity_1h` score `-0.5369` n `147` status `ready` deltaP `2.7751` edge `0.0005` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.5875` n `136` status `ready` deltaP `0.278` edge `0.0088` maxDD `-0.8774`
- `market_context_high->index_1h` score `-0.6138` n `147` status `ready` deltaP `-0.8177` edge `0.0037` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.8763` n `147` status `ready` deltaP `-0.3706` edge `0.0133` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9034` n `124` status `ready` deltaP `2.8506` edge `0.0037` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9124` n `136` status `ready` deltaP `3.5868` edge `0.0388` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
