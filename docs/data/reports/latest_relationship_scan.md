# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T00:07:36.946225+00:00`
- Price records: `672`
- Market context records: `3941`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11355`

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

- `risk_on_high->unknown_4h` score `144.4547` n `41` status `ready` deltaP `3.811` edge `12.1937` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.4547` n `41` status `ready` deltaP `3.811` edge `12.1937` maxDD `-10.8303`
- `market_context_high->unknown_4h` score `16.1282` n `177` status `ready` deltaP `-3.3132` edge `1.907` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.0167` n `40` status `ready` deltaP `42.0139` edge `0.4713` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0167` n `40` status `ready` deltaP `42.0139` edge `0.4713` maxDD `0.0`
- `market_context_high->unknown_24h` score `7.1921` n `165` status `ready` deltaP `-10.7986` edge `2.1806` maxDD `-106.4084`
- `risk_on_high->equity_4h` score `3.7365` n `41` status `ready` deltaP `37.6525` edge `0.0651` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.7365` n `41` status `ready` deltaP `37.6525` edge `0.0651` maxDD `-0.0458`
- `market_context_high->equity_24h` score `3.5628` n `165` status `ready` deltaP `20.8018` edge `0.4612` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.4152` n `165` status `ready` deltaP `25.7923` edge `0.2266` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.1109` n `165` status `ready` deltaP `16.2973` edge `0.3021` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.7952` n `40` status `ready` deltaP `30.0347` edge `0.0327` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7952` n `40` status `ready` deltaP `30.0347` edge `0.0327` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.4928` n `41` status `ready` deltaP `23.3231` edge `0.1188` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.4928` n `41` status `ready` deltaP `23.3231` edge `0.1188` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.3546` n `177` status `ready` deltaP `16.8191` edge `0.1772` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.0125` n `40` status `ready` deltaP `4.1667` edge `0.2813` maxDD `-12.9764`
- `risk_on_and_context->commodity_24h` score `1.0125` n `40` status `ready` deltaP `4.1667` edge `0.2813` maxDD `-12.9764`
- `market_context_high->equity_4h` score `0.9514` n `177` status `ready` deltaP `14.8469` edge `0.1507` maxDD `-8.2982`
- `risk_on_high->metal_24h` score `0.4567` n `40` status `ready` deltaP `-16.3542` edge `0.229` maxDD `-1.9133`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
