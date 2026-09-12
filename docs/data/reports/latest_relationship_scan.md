# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T06:07:23.706020+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11478`

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

- `market_context_high->unknown_24h` score `1492.4441` n `131` status `ready` deltaP `13.9247` edge `124.2827` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.4025` n `82` status `ready` deltaP `-3.6038` edge `32.0164` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.0074` n `59` status `ready` deltaP `54.505` edge `1.7273` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `22.8384` n `79` status `ready` deltaP `42.282` edge `1.6443` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.8384` n `79` status `ready` deltaP `42.282` edge `1.6443` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.3669` n `131` status `ready` deltaP `36.3974` edge `1.454` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.5054` n `59` status `ready` deltaP `29.967` edge `1.3078` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.091` n `59` status `ready` deltaP `33.5894` edge `0.7935` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0243` n `79` status `ready` deltaP `36.9792` edge `0.5055` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0243` n `79` status `ready` deltaP `36.9792` edge `0.5055` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7027` n `131` status `ready` deltaP `36.9792` edge `0.4787` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.1748` n `59` status `ready` deltaP `51.2153` edge `0.3398` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.1044` n `79` status `ready` deltaP `43.5647` edge `0.4221` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1044` n `79` status `ready` deltaP `43.5647` edge `0.4221` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9297` n `59` status `ready` deltaP `51.4713` edge `0.327` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.9631` n `79` status `ready` deltaP `29.6542` edge `0.3851` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.9631` n `79` status `ready` deltaP `29.6542` edge `0.3851` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.3297` n `79` status `ready` deltaP `19.5125` edge `0.96` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.3297` n `79` status `ready` deltaP `19.5125` edge `0.96` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.1371` n `79` status `ready` deltaP `51.0636` edge `0.0919` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
