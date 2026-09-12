# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T06:52:28.736349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11496`

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

- `market_context_high->unknown_24h` score `1730.868` n `128` status `ready` deltaP `13.8889` edge `144.1516` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.2585` n `82` status `ready` deltaP `-3.6038` edge `32.0044` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.1334` n `59` status `ready` deltaP `54.505` edge `1.7378` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `22.4428` n `76` status `ready` deltaP `42.0322` edge `1.613` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.4428` n `76` status `ready` deltaP `42.0322` edge `1.613` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.0932` n `128` status `ready` deltaP `36.1111` edge `1.4331` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.569` n `59` status `ready` deltaP `29.967` edge `1.3131` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.0994` n `59` status `ready` deltaP `33.5894` edge `0.7942` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0111` n `76` status `ready` deltaP `36.9792` edge `0.5044` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0111` n `76` status `ready` deltaP `36.9792` edge `0.5044` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6895` n `128` status `ready` deltaP `36.9792` edge `0.4776` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.2213` n `59` status `ready` deltaP `51.7361` edge `0.3402` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.098` n `76` status `ready` deltaP `43.3648` edge `0.4229` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.098` n `76` status `ready` deltaP `43.3648` edge `0.4229` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9237` n `59` status `ready` deltaP `51.4713` edge `0.3265` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.7728` n `76` status `ready` deltaP `29.0597` edge `0.3732` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.7728` n `76` status `ready` deltaP `29.0597` edge `0.3732` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.1083` n `76` status `ready` deltaP `50.9137` edge `0.0905` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.1083` n `76` status `ready` deltaP `50.9137` edge `0.0905` maxDD `-0.0051`
- `risk_on_high->crypto_major_24h` score `4.6145` n `76` status `ready` deltaP `17.8636` edge `0.8793` maxDD `-24.5429`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
