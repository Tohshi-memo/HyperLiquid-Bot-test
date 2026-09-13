# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T00:22:27.439128+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12511`

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

- `market_context_high->unknown_24h` score `16571.5094` n `59` status `ready` deltaP `12.0616` edge `1380.8839` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.2856` n `82` status `ready` deltaP `-5.5499` edge `31.9363` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.2553` n `82` status `ready` deltaP `33.1004` edge `1.3494` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0754` n `82` status `ready` deltaP `39.8459` edge `1.3877` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.3568` n `59` status `ready` deltaP `23.055` edge `0.7921` maxDD `-3.9523`
- `market_context_high->equity_24h` score `10.2893` n `59` status `ready` deltaP `45.4861` edge `0.5542` maxDD `0.0`
- `news_risk_high->index_24h` score `6.0371` n `82` status `ready` deltaP `41.438` edge `0.2445` maxDD `-0.0797`
- `news_risk_high->equity_24h` score `6.0321` n `82` status `ready` deltaP `14.9983` edge `0.5807` maxDD `-6.5742`
- `news_risk_high->metal_24h` score `5.0788` n `82` status `ready` deltaP `28.9126` edge `0.2759` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2831` n `59` status `ready` deltaP `42.7083` edge `0.0722` maxDD `0.0`
- `market_context_high->index_24h` score `3.9157` n `59` status `ready` deltaP `42.0375` edge `0.0853` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.4102` n `59` status `ready` deltaP `9.7104` edge `0.1076` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.1167` n `82` status `ready` deltaP `7.4695` edge `0.028` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.0913` n `53` status `ready` deltaP `5.9739` edge `0.0008` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.0913` n `53` status `ready` deltaP `5.9739` edge `0.0008` maxDD `-0.3081`
- `risk_on_high->index_1h` score `-0.0008` n `53` status `ready` deltaP `5.8553` edge `0.0005` maxDD `-0.1711`
- `risk_on_and_context->index_1h` score `-0.0008` n `53` status `ready` deltaP `5.8553` edge `0.0005` maxDD `-0.1711`
- `risk_on_high->crypto_alt_4h` score `-0.0143` n `51` status `ready` deltaP `6.274` edge `0.1238` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `-0.0143` n `51` status `ready` deltaP `6.274` edge `0.1238` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `-0.0851` n `53` status `ready` deltaP `1.7512` edge `0.003` maxDD `-0.0464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
