# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T08:37:23.821540+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11581`

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

- `risk_on_high->unknown_4h` score `36.3203` n `124` status `ready` deltaP `14.703` edge `2.9905` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.3203` n `124` status `ready` deltaP `14.703` edge `2.9905` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `26.5775` n `162` status `ready` deltaP `12.2139` edge `2.2029` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.7331` n `133` status `ready` deltaP `2.3895` edge `1.6862` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.7331` n `133` status `ready` deltaP `2.3895` edge `1.6862` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.9336` n `174` status `ready` deltaP `1.9185` edge `1.2114` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.4848` n `107` status `ready` deltaP `21.0978` edge `0.6476` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.4848` n `107` status `ready` deltaP `21.0978` edge `0.6476` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.2912` n `107` status `ready` deltaP `21.2568` edge `0.8424` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.2912` n `107` status `ready` deltaP `21.2568` edge `0.8424` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2623` n `59` status `ready` deltaP `21.1776` edge `0.4423` maxDD `-19.4761`
- `market_context_high->equity_24h` score `1.822` n `143` status `ready` deltaP `18.6274` edge `0.5508` maxDD `-21.3114`
- `news_risk_high->crypto_major_24h` score `1.6565` n `59` status `ready` deltaP `14.6952` edge `0.4784` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.485` n `59` status `ready` deltaP `7.0474` edge `0.3235` maxDD `-15.4056`
- `risk_on_high->crypto_major_24h` score `0.9244` n `107` status `ready` deltaP `21.0313` edge `0.8527` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.9244` n `107` status `ready` deltaP `21.0313` edge `0.8527` maxDD `-56.9519`
- `market_context_high->crypto_alt_24h` score `0.5744` n `143` status `ready` deltaP `15.5121` edge `0.7201` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.5301` n `143` status `ready` deltaP `22.992` edge `0.8611` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2621` n `67` status `ready` deltaP `5.6425` edge `0.0319` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0502` n `133` status `ready` deltaP `11.2152` edge `0.0029` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
