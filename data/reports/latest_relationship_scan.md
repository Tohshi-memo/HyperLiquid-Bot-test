# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T04:07:26.669414+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11617`

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

- `risk_on_high->equity_24h` score `5.3432` n `107` status `ready` deltaP `24.2228` edge `0.6983` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.3432` n `107` status `ready` deltaP `24.2228` edge `0.6983` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `4.5037` n `107` status `ready` deltaP `17.7813` edge `0.3186` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `4.5037` n `107` status `ready` deltaP `17.7813` edge `0.3186` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `2.5466` n `148` status `ready` deltaP `13.6578` edge `0.1907` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.3434` n `59` status `ready` deltaP `10.1724` edge `0.3742` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `2.3248` n `107` status `ready` deltaP `21.2568` edge `0.8467` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3248` n `107` status `ready` deltaP `21.2568` edge `0.8467` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2958` n `59` status `ready` deltaP `21.1776` edge `0.4466` maxDD `-19.4761`
- `market_context_high->equity_24h` score `1.8185` n `147` status `ready` deltaP `20.192` edge `0.5794` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.8043` n `118` status `ready` deltaP `0.9844` edge `0.2015` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.8043` n `118` status `ready` deltaP `0.9844` edge `0.2015` maxDD `-1.95`
- `news_risk_high->crypto_major_24h` score `1.2411` n `59` status `ready` deltaP `14.348` edge `0.4461` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.6544` n `107` status `ready` deltaP `20.6841` edge `0.8204` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.6544` n `107` status `ready` deltaP `20.6841` edge `0.8204` maxDD `-56.9519`
- `market_context_high->unknown_1h` score `0.6509` n `160` status `ready` deltaP `-0.0749` edge `0.1178` maxDD `-2.0446`
- `market_context_high->crypto_major_24h` score `0.4918` n `147` status `ready` deltaP `23.7104` edge `0.8514` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.4715` n `147` status `ready` deltaP `15.2742` edge `0.7085` maxDD `-46.3234`
- `risk_on_high->index_1h` score `0.3227` n `118` status `ready` deltaP `9.8701` edge `0.0056` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.3227` n `118` status `ready` deltaP `9.8701` edge `0.0056` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
