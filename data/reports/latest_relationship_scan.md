# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T15:22:13.848068+00:00`
- Price records: `672`
- Market context records: `3904`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11356`

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

- `risk_on_high->unknown_4h` score `47.0213` n `72` status `ready` deltaP `4.5223` edge `6.2124` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.0213` n `72` status `ready` deltaP `4.5223` edge `6.2124` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `27.3775` n `37` status `ready` deltaP `22.8463` edge `2.2121` maxDD `-4.6361`
- `risk_on_and_context->crypto_major_24h` score `27.3775` n `37` status `ready` deltaP `22.8463` edge `2.2121` maxDD `-4.6361`
- `risk_on_high->equity_24h` score `24.2603` n `37` status `ready` deltaP `42.0139` edge `1.7416` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.2603` n `37` status `ready` deltaP `42.0139` edge `1.7416` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `15.9088` n `37` status `ready` deltaP `20.763` edge `1.3143` maxDD `-8.1589`
- `risk_on_and_context->crypto_alt_24h` score `15.9088` n `37` status `ready` deltaP `20.763` edge `1.3143` maxDD `-8.1589`
- `risk_on_high->index_24h` score `10.006` n `37` status `ready` deltaP `30.0347` edge `0.6336` maxDD `0.0`
- `risk_on_and_context->index_24h` score `10.006` n `37` status `ready` deltaP `30.0347` edge `0.6336` maxDD `0.0`
- `market_context_high->equity_24h` score `6.4949` n `164` status `ready` deltaP `20.6724` edge `0.7064` maxDD `-14.5715`
- `market_context_high->unknown_4h` score `6.2665` n `210` status `ready` deltaP `-1.9062` edge `1.357` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `5.7712` n `72` status `ready` deltaP `20.5284` edge `0.4563` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.7712` n `72` status `ready` deltaP `20.5284` edge `0.4563` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.8003` n `164` status `ready` deltaP `25.7664` edge `0.3422` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.0365` n `164` status `ready` deltaP `20.5073` edge `0.2595` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5989` n `72` status `ready` deltaP `24.9492` edge `0.1637` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5989` n `72` status `ready` deltaP `24.9492` edge `0.1637` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.5852` n `210` status `ready` deltaP `16.3618` edge `0.2828` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `1.8166` n `164` status `ready` deltaP `3.6966` edge `0.5731` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
