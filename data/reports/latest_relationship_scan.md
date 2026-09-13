# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T06:07:31.371361+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12627`

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

- `market_context_high->unknown_24h` score `19210.1501` n `54` status `ready` deltaP `13.3102` edge `1600.7623` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `377.2574` n `82` status `ready` deltaP `-4.6517` edge `31.5113` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.7357` n `82` status `ready` deltaP `31.8851` edge `1.3142` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.7059` n `82` status `ready` deltaP `37.7626` edge `1.3708` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.9639` n `54` status `ready` deltaP `49.4792` edge `0.5838` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.7659` n `54` status `ready` deltaP `19.3287` edge `0.7677` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.7656` n `82` status `ready` deltaP `18.9914` edge `0.6152` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.2905` n `82` status `ready` deltaP `44.2157` edge `0.2471` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.6868` n `82` status `ready` deltaP `25.0932` edge `0.2687` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.3062` n `54` status `ready` deltaP `42.1875` edge `0.0776` maxDD `0.0`
- `market_context_high->index_24h` score `4.3024` n `54` status `ready` deltaP `45.2546` edge `0.0919` maxDD `-0.1382`
- `market_context_high->metal_24h` score `0.7995` n `54` status `ready` deltaP `11.2269` edge `0.1151` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.3129` n `60` status `ready` deltaP `10.7521` edge `0.1359` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.3129` n `60` status `ready` deltaP `10.7521` edge `0.1359` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.2782` n `82` status `ready` deltaP `10.3658` edge `0.0294` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1208` n `65` status `ready` deltaP `4.8526` edge `0.0033` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1208` n `65` status `ready` deltaP `4.8526` edge `0.0033` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.1358` n `65` status `ready` deltaP `3.0147` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.1358` n `65` status `ready` deltaP `3.0147` edge `0.0016` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1639` n `125` status `ready` deltaP `2.9449` edge `-0.0017` maxDD `-0.5274`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
