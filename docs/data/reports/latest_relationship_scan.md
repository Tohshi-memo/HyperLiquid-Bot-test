# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T04:22:25.065792+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11629`

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

- `risk_on_high->equity_24h` score `5.2885` n `107` status `ready` deltaP `24.0492` edge `0.6949` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.2885` n `107` status `ready` deltaP `24.0492` edge `0.6949` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `4.2157` n `107` status `ready` deltaP `17.7813` edge `0.2946` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `4.2157` n `107` status `ready` deltaP `17.7813` edge `0.2946` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `3.4866` n `149` status `ready` deltaP `13.7983` edge `0.2681` maxDD `-2.563`
- `risk_on_high->crypto_alt_24h` score `2.3209` n `107` status `ready` deltaP `21.2568` edge `0.8462` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3209` n `107` status `ready` deltaP `21.2568` edge `0.8462` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2919` n `59` status `ready` deltaP `21.1776` edge `0.4461` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `2.2887` n `59` status `ready` deltaP `9.9988` edge `0.3708` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.783` n `147` status `ready` deltaP `20.0184` edge `0.576` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.6655` n `119` status `ready` deltaP `0.4503` edge `0.1935` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.6655` n `119` status `ready` deltaP `0.4503` edge `0.1935` maxDD `-1.95`
- `news_risk_high->crypto_major_24h` score `1.2651` n `59` status `ready` deltaP `14.348` edge `0.4481` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.67` n `107` status `ready` deltaP `20.6841` edge `0.8224` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.67` n `107` status `ready` deltaP `20.6841` edge `0.8224` maxDD `-56.9519`
- `market_context_high->unknown_1h` score `0.5551` n `161` status `ready` deltaP `-0.4631` edge `0.1124` maxDD `-2.0446`
- `market_context_high->crypto_major_24h` score `0.5074` n `147` status `ready` deltaP `23.7104` edge `0.8534` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.4676` n `147` status `ready` deltaP `15.2742` edge `0.708` maxDD `-46.3234`
- `risk_on_high->index_1h` score `0.3375` n `119` status `ready` deltaP `10.0551` edge `0.0056` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.3375` n `119` status `ready` deltaP `10.0551` edge `0.0056` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
