# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T07:22:30.362695+00:00`
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

- `market_context_high->unknown_4h` score `33.9829` n `119` status `ready` deltaP `-4.3144` edge `2.9253` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `10.1843` n `54` status `ready` deltaP `20.544` edge `1.4323` maxDD `-13.7531`
- `market_context_high->crypto_alt_24h` score `6.8522` n `54` status `ready` deltaP `3.8773` edge `1.2352` maxDD `-22.272`
- `risk_on_high->crypto_major_4h` score `5.7759` n `51` status `ready` deltaP `35.2492` edge `0.3316` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.7759` n `51` status `ready` deltaP `35.2492` edge `0.3316` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `4.7638` n `51` status `ready` deltaP `22.9436` edge `0.2888` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.7638` n `51` status `ready` deltaP `22.9436` edge `0.2888` maxDD `-1.9151`
- `market_context_high->equity_24h` score `3.8092` n `54` status `ready` deltaP `15.0463` edge `0.5079` maxDD `-5.921`
- `market_context_high->index_24h` score `2.4889` n `54` status `ready` deltaP `33.9699` edge `0.1348` maxDD `-0.3741`
- `risk_on_high->crypto_alt_1h` score `1.746` n `56` status `ready` deltaP `10.2438` edge `0.1369` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.746` n `56` status `ready` deltaP `10.2438` edge `0.1369` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.4922` n `56` status `ready` deltaP `9.9658` edge `0.1232` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.4922` n `56` status `ready` deltaP `9.9658` edge `0.1232` maxDD `-3.2233`
- `market_context_high->crypto_alt_1h` score `1.1039` n `124` status `ready` deltaP `8.8613` edge `0.128` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.8523` n `119` status `ready` deltaP `11.7198` edge `0.2417` maxDD `-11.1784`
- `market_context_high->crypto_major_1h` score `0.646` n `124` status `ready` deltaP `4.8967` edge `0.0975` maxDD `-3.4384`
- `risk_on_high->metal_4h` score `0.3876` n `51` status `ready` deltaP `10.0221` edge `0.0347` maxDD `-1.2037`
- `risk_on_and_context->metal_4h` score `0.3876` n `51` status `ready` deltaP `10.0221` edge `0.0347` maxDD `-1.2037`
- `market_context_high->unknown_1h` score `0.346` n `124` status `ready` deltaP `-4.9401` edge `0.0954` maxDD `-1.024`
- `market_context_high->crypto_alt_4h` score `0.2613` n `119` status `ready` deltaP `5.8567` edge `0.2503` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
