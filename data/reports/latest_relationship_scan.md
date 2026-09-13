# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T04:40:30.318170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12599`

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

- `market_context_high->unknown_24h` score `16610.4896` n `59` status `ready` deltaP `13.1033` edge `1384.1253` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `379.373` n `82` status `ready` deltaP `-4.6517` edge `31.6876` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.8792` n `82` status `ready` deltaP `32.0587` edge `1.325` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.8785` n `82` status `ready` deltaP `38.6306` edge `1.3794` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.8122` n `59` status `ready` deltaP `48.4375` edge `0.5781` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.9806` n `59` status `ready` deltaP `22.0133` edge `0.7677` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.555` n `82` status `ready` deltaP `17.9497` edge `0.6046` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.2091` n `82` status `ready` deltaP `43.3477` edge `0.2461` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.799` n `82` status `ready` deltaP `26.1349` edge `0.2711` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.239` n `59` status `ready` deltaP `42.1875` edge `0.072` maxDD `0.0`
- `market_context_high->index_24h` score `4.0877` n `59` status `ready` deltaP `43.9472` edge `0.0869` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.2283` n `59` status `ready` deltaP `6.9327` edge `0.1028` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.2268` n `82` status `ready` deltaP `9.4512` edge `0.0289` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.1117` n `54` status `ready` deltaP `7.4074` edge `0.1324` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.1117` n `54` status `ready` deltaP `7.4074` edge `0.1324` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.1089` n `65` status `ready` deltaP `4.7029` edge `0.0033` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1089` n `65` status `ready` deltaP `4.7029` edge `0.0033` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.094` n `124` status `ready` deltaP `3.2017` edge `-0.0018` maxDD `-0.5274`
- `risk_on_high->metal_1h` score `-0.0999` n `65` status `ready` deltaP `3.4638` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0999` n `65` status `ready` deltaP `3.4638` edge `0.0016` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
