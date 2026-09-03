# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T00:22:29.808061+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11521`

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

- `risk_on_high->equity_24h` score `5.8034` n `107` status `ready` deltaP `25.2645` edge `0.7297` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.8034` n `107` status `ready` deltaP `25.2645` edge `0.7297` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `5.7249` n `107` status `ready` deltaP `18.391` edge `0.4163` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `5.7249` n `107` status `ready` deltaP `18.391` edge `0.4163` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `3.8055` n `147` status `ready` deltaP `14.125` edge `0.2925` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.8035` n `59` status `ready` deltaP `11.2141` edge `0.4056` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `2.2081` n `107` status `ready` deltaP `21.0832` edge `0.8329` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.2081` n `107` status `ready` deltaP `21.0832` edge `0.8329` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.1791` n `59` status `ready` deltaP `21.004` edge `0.4328` maxDD `-19.4761`
- `market_context_high->equity_24h` score `2.1176` n `147` status `ready` deltaP `21.2337` edge `0.6108` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `0.6661` n `59` status `ready` deltaP `14.0007` edge `0.4005` maxDD `-30.7329`
- `market_context_high->crypto_alt_24h` score `0.3549` n `147` status `ready` deltaP `15.1006` edge `0.6947` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.2806` n `107` status `ready` deltaP `20.3368` edge `0.7748` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.2806` n `107` status `ready` deltaP `20.3368` edge `0.7748` maxDD `-56.9519`
- `news_risk_high->commodity_4h` score `0.2301` n `67` status `ready` deltaP `5.6425` edge `0.0278` maxDD `-0.8733`
- `market_context_high->crypto_major_24h` score `0.1181` n `147` status `ready` deltaP `23.3631` edge `0.8058` maxDD `-61.3797`
- `risk_on_high->index_1h` score `0.1073` n `107` status `ready` deltaP `8.0936` edge `0.0043` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1073` n `107` status `ready` deltaP `8.0936` edge `0.0043` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0621` n `107` status `ready` deltaP `19.5635` edge `0.0106` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0621` n `107` status `ready` deltaP `19.5635` edge `0.0106` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
