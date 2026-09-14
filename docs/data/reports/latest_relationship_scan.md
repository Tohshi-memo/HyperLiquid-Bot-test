# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T12:52:29.354724+00:00`
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

- `news_risk_high->unknown_4h` score `254.9684` n `81` status `ready` deltaP `-21.0611` edge `21.4771` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `20.6687` n `81` status `ready` deltaP `42.9784` edge `1.4844` maxDD `-2.2157`
- `news_risk_high->crypto_major_24h` score `16.9446` n `81` status `ready` deltaP `33.6613` edge `1.3347` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.448` n `81` status `ready` deltaP `36.5162` edge `0.9719` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.4047` n `81` status `ready` deltaP `60.3588` edge `0.3156` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1731` n `98` status `ready` deltaP `40.1042` edge `0.3304` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1675` n `41` status `ready` deltaP `40.1042` edge `0.2466` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1675` n `41` status `ready` deltaP `40.1042` edge `0.2466` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.0872` n `81` status `ready` deltaP `36.6126` edge `0.3086` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.9287` n `41` status `ready` deltaP `55.3735` edge `0.0458` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.9287` n `41` status `ready` deltaP `55.3735` edge `0.0458` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.5039` n `98` status `ready` deltaP `51.6901` edge `0.0523` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9983` n `52` status `ready` deltaP `26.5947` edge `0.0242` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9983` n `52` status `ready` deltaP `26.5947` edge `0.0242` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7986` n `137` status `ready` deltaP `22.0046` edge `0.045` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7071` n `137` status `ready` deltaP `12.2132` edge `0.0152` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6893` n `81` status `ready` deltaP `16.6064` edge `0.0405` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.308` n `137` status `ready` deltaP `11.6833` edge `0.0092` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1917` n `52` status `ready` deltaP `6.5984` edge `0.0072` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1917` n `52` status `ready` deltaP `6.5984` edge `0.0072` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
