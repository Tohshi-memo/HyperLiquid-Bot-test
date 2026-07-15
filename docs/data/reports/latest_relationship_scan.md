# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T12:22:30.583034+00:00`
- Price records: `672`
- Market context records: `6816`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11668`

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

- `market_context_high->unknown_24h` score `0.8382` n `176` status `ready` deltaP `-1.5467` edge `0.493` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3875` n `176` status `ready` deltaP `10.9217` edge `0.1463` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2827` n `197` status `ready` deltaP `5.6157` edge `0.0123` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.3921` n `197` status `ready` deltaP `-0.2796` edge `0.0001` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5306` n `197` status `ready` deltaP `3.1361` edge `0.0113` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.8184` n `197` status `ready` deltaP `-3.9895` edge `-0.0041` maxDD `-0.9382`
- `market_context_high->metal_1h` score `-1.0072` n `197` status `ready` deltaP `-6.6377` edge `-0.011` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.0366` n `197` status `ready` deltaP `-1.9005` edge `-0.0054` maxDD `-2.1314`
- `market_context_high->commodity_4h` score `-1.3341` n `185` status `ready` deltaP `-1.9883` edge `-0.0088` maxDD `-5.5853`
- `market_context_high->fx_4h` score `-1.3397` n `185` status `ready` deltaP `5.5224` edge `-0.0022` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.653` n `185` status `ready` deltaP `1.99` edge `-0.0292` maxDD `-6.3458`
- `market_context_high->equity_1h` score `-1.7263` n `197` status `ready` deltaP `0.0646` edge `-0.0316` maxDD `-4.6821`
- `market_context_high->unknown_1h` score `-1.7709` n `197` status `ready` deltaP `-5.9804` edge `-0.0176` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.8867` n `185` status `ready` deltaP `-6.0094` edge `-0.0317` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.3459` n `185` status `ready` deltaP `-1.2673` edge `-0.0878` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.4697` n `185` status `ready` deltaP `-13.8126` edge `0.0395` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.5569` n `185` status `ready` deltaP `-1.9743` edge `-0.0845` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.4684` n `176` status `ready` deltaP `-9.7853` edge `-0.0035` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.057` n `185` status `ready` deltaP `-0.6576` edge `-0.1901` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.6563` n `176` status `ready` deltaP `-21.9697` edge `-0.243` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
