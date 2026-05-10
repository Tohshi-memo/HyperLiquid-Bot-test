# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T07:37:06.813686+00:00`
- Price records: `672`
- Market context records: `953`
- Flow alert records: `2670`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.7737` n `162` status `ready` deltaP `32.3303` edge `1.049` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.4068` n `162` status `ready` deltaP `8.6806` edge `0.6427` maxDD `0.0`
- `market_context_high->equity_24h` score `1.0433` n `162` status `ready` deltaP `2.7778` edge `0.3289` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.2833` n `162` status `ready` deltaP `1.4275` edge `0.2136` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2316` n `204` status `ready` deltaP `3.402` edge `0.0388` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3919` n `204` status `ready` deltaP `1.0098` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.5812` n `204` status `ready` deltaP `1.8199` edge `0.0163` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6709` n `192` status `ready` deltaP `1.7149` edge `0.0022` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7267` n `204` status `ready` deltaP `2.8942` edge `0.0055` maxDD `-2.8282`
- `market_context_high->equity_4h` score `-1.2063` n `192` status `ready` deltaP `2.6677` edge `0.0969` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-1.3808` n `192` status `ready` deltaP `-0.7749` edge `0.0824` maxDD `-13.0076`
- `market_context_high->unknown_1h` score `-1.3986` n `204` status `ready` deltaP `-3.2817` edge `-0.0175` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.4692` n `192` status `ready` deltaP `0.3049` edge `0.0278` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6642` n `204` status `ready` deltaP `5.7473` edge `-0.0047` maxDD `-11.4508`
- `market_context_high->metal_1h` score `-1.8352` n `204` status `ready` deltaP `-1.494` edge `-0.0294` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.9364` n `204` status `ready` deltaP `1.2299` edge `-0.0256` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.4461` n `192` status `ready` deltaP `8.9939` edge `0.1068` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.3804` n `192` status `ready` deltaP `6.2881` edge `-0.1358` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.3876` n `192` status `ready` deltaP `-2.2485` edge `0.0105` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.4873` n `162` status `ready` deltaP `4.8419` edge `-0.057` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
