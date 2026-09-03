# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T10:07:25.966032+00:00`
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

- `risk_on_high->unknown_4h` score `37.5458` n `130` status `ready` deltaP `14.4371` edge `3.0944` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `37.5458` n `130` status `ready` deltaP `14.4371` edge `3.0944` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.6848` n `164` status `ready` deltaP `11.5854` edge `2.3827` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.733` n `133` status `ready` deltaP `2.5392` edge `1.6852` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.733` n `133` status `ready` deltaP `2.5392` edge `1.6852` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.6824` n `176` status `ready` deltaP `1.8984` edge `1.1906` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.0499` n `107` status `ready` deltaP `20.0562` edge `0.6183` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.0499` n `107` status `ready` deltaP `20.0562` edge `0.6183` maxDD `-19.828`
- `market_context_high->equity_24h` score `2.9805` n `139` status `ready` deltaP `19.2359` edge `0.5547` maxDD `-20.7654`
- `risk_on_high->crypto_alt_24h` score `2.0062` n `107` status `ready` deltaP `20.2152` edge `0.8128` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.0062` n `107` status `ready` deltaP `20.2152` edge `0.8128` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.9772` n `59` status `ready` deltaP `20.136` edge `0.4127` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `1.3194` n `59` status `ready` deltaP `13.8271` edge `0.4561` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.05` n `59` status `ready` deltaP `6.0058` edge `0.2942` maxDD `-15.4056`
- `market_context_high->crypto_alt_24h` score `0.7633` n `139` status `ready` deltaP `16.1609` edge `0.74` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.7053` n `107` status `ready` deltaP `20.1632` edge `0.8304` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.7053` n `107` status `ready` deltaP `20.1632` edge `0.8304` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.5191` n `139` status `ready` deltaP `23.1552` edge `0.8586` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2644` n `67` status `ready` deltaP `5.6425` edge `0.0322` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0494` n `133` status `ready` deltaP `11.2152` edge `0.0028` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
