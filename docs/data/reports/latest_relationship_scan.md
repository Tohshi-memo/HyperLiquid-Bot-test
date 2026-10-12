# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T07:37:32.375992+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9600`

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

- `market_context_high->unknown_4h` score `34.1075` n `119` status `ready` deltaP `-3.6265` edge `2.9311` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `10.4089` n `54` status `ready` deltaP `20.544` edge `1.4611` maxDD `-13.7531`
- `market_context_high->crypto_alt_24h` score `7.3895` n `54` status `ready` deltaP `5.5556` edge `1.2838` maxDD `-21.8774`
- `risk_on_high->crypto_alt_4h` score `4.6114` n `51` status `ready` deltaP `22.9436` edge `0.2761` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.6114` n `51` status `ready` deltaP `22.9436` edge `0.2761` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.7068` n `51` status `ready` deltaP `35.2492` edge `0.3255` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.7068` n `51` status `ready` deltaP `35.2492` edge `0.3255` maxDD `-4.1548`
- `market_context_high->equity_24h` score `3.5759` n `54` status `ready` deltaP `13.368` edge `0.4959` maxDD `-6.4593`
- `market_context_high->index_24h` score `2.3425` n `54` status `ready` deltaP `32.2917` edge `0.1319` maxDD `-0.4152`
- `risk_on_high->crypto_alt_1h` score `1.6628` n `55` status `ready` deltaP `9.7442` edge `0.1333` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.6628` n `55` status `ready` deltaP `9.7442` edge `0.1333` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.3894` n `55` status `ready` deltaP `9.2515` edge `0.1194` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.3894` n `55` status `ready` deltaP `9.2515` edge `0.1194` maxDD `-3.2233`
- `market_context_high->crypto_alt_1h` score `1.0773` n `123` status `ready` deltaP `8.7094` edge `0.1268` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.8344` n `119` status `ready` deltaP `11.7198` edge `0.2394` maxDD `-11.1784`
- `market_context_high->crypto_major_1h` score `0.5967` n `123` status `ready` deltaP `4.5361` edge `0.0958` maxDD `-3.4384`
- `market_context_high->unknown_1h` score `0.3909` n `123` status `ready` deltaP `-5.1434` edge `0.1005` maxDD `-1.024`
- `market_context_high->crypto_alt_4h` score `0.2239` n `119` status `ready` deltaP `5.8567` edge `0.2455` maxDD `-13.8008`
- `risk_on_high->metal_4h` score `0.1165` n `51` status `ready` deltaP `8.2137` edge `0.0287` maxDD `-1.2335`
- `risk_on_and_context->metal_4h` score `0.1165` n `51` status `ready` deltaP `8.2137` edge `0.0287` maxDD `-1.2335`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
