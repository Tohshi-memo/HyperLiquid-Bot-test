# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T12:22:30.362786+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_4h` score `984.6633` n `82` status `ready` deltaP `-20.5793` edge `82.2818` maxDD `-4.1464`
- `news_risk_high->unknown_1h` score `562.1526` n `82` status `ready` deltaP `-6.7475` edge `46.9332` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.4257` n `82` status `ready` deltaP `41.781` edge `1.4724` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `16.7309` n `82` status `ready` deltaP `33.0751` edge `1.3208` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.2406` n `82` status `ready` deltaP `35.4844` edge `0.9615` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2728` n `82` status `ready` deltaP `59.3199` edge `0.3116` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `7.1419` n `96` status `ready` deltaP `40.1042` edge `0.3278` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1843` n `41` status `ready` deltaP `40.1042` edge `0.248` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1843` n `41` status `ready` deltaP `40.1042` edge `0.248` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.0523` n `82` status `ready` deltaP `36.5515` edge `0.3061` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.9648` n `41` status `ready` deltaP `55.7207` edge `0.0465` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.9648` n `41` status `ready` deltaP `55.7207` edge `0.0465` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.5203` n `96` status `ready` deltaP `51.9097` edge `0.0522` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0153` n `52` status `ready` deltaP `26.7472` edge `0.0246` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0153` n `52` status `ready` deltaP `26.7472` edge `0.0246` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8156` n `137` status `ready` deltaP `22.1571` edge `0.0454` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.737` n `137` status `ready` deltaP `12.5126` edge `0.0157` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6954` n `82` status `ready` deltaP `16.7683` edge `0.0402` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3254` n `137` status `ready` deltaP `11.9881` edge `0.0094` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2216` n `52` status `ready` deltaP `6.8978` edge `0.0077` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
