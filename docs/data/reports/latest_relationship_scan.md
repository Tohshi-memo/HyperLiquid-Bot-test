# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T08:52:35.459515+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `37.1348` n `46` status `ready` deltaP `24.9094` edge `2.9328` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.4735` n `46` status `ready` deltaP `42.9575` edge `0.4371` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9582` n `46` status `ready` deltaP `36.5262` edge `0.4376` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.6507` n `88` status `ready` deltaP `1.2056` edge `0.5624` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.198` n `88` status `ready` deltaP `15.3687` edge `0.082` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.2741` n `88` status `ready` deltaP `16.8653` edge `0.0087` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2157` n `88` status `ready` deltaP `5.5321` edge `0.0227` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.182` n `88` status `ready` deltaP `7.9818` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4577` n `88` status `ready` deltaP `1.7284` edge `-0.0168` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5409` n `88` status `ready` deltaP `-1.6195` edge `-0.0091` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.5922` n `88` status `ready` deltaP `4.2822` edge `0.019` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9592` n `88` status `ready` deltaP `3.2567` edge `-0.0057` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2707` n `88` status `ready` deltaP `-3.4703` edge `-0.0117` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5666` n `88` status `ready` deltaP `5.3144` edge `-0.0827` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.8603` n `46` status `ready` deltaP `-5.9632` edge `0.0053` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.8617` n `88` status `ready` deltaP `-10.1164` edge `-0.0458` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.4196` n `88` status `ready` deltaP `2.5994` edge `-0.2576` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6163` n `88` status `ready` deltaP `-12.7994` edge `-0.0787` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.9367` n `46` status `ready` deltaP `-24.683` edge `-0.13` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.6821` n `88` status `ready` deltaP `0.1801` edge `-0.3248` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
