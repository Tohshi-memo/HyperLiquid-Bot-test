# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T05:07:25.485408+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11701`

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

- `risk_on_high->unknown_4h` score `41.0985` n `110` status `ready` deltaP `18.2401` edge `3.3651` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `41.0985` n `110` status `ready` deltaP `18.2401` edge `3.3651` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.1267` n `152` status `ready` deltaP `14.209` edge `2.3187` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `17.8727` n `122` status `ready` deltaP `0.2405` edge `1.5455` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `17.8727` n `122` status `ready` deltaP `0.2405` edge `1.5455` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.6774` n `164` status `ready` deltaP `-0.6792` edge `1.0407` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `5.1437` n `107` status `ready` deltaP `23.5284` edge `0.6863` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.1437` n `107` status `ready` deltaP `23.5284` edge `0.6863` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3185` n `107` status `ready` deltaP `21.2568` edge `0.8459` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3185` n `107` status `ready` deltaP `21.2568` edge `0.8459` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2896` n `59` status `ready` deltaP `21.1776` edge `0.4458` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `2.1438` n `59` status `ready` deltaP `9.478` edge `0.3622` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.6888` n `147` status `ready` deltaP `19.4976` edge `0.5674` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `1.3491` n `59` status `ready` deltaP `14.348` edge `0.4551` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.7246` n `107` status `ready` deltaP `20.6841` edge `0.8294` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.7246` n `107` status `ready` deltaP `20.6841` edge `0.8294` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.562` n `147` status `ready` deltaP `23.7104` edge `0.8604` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.4653` n `147` status `ready` deltaP `15.2742` edge `0.7077` maxDD `-46.3234`
- `risk_on_high->index_1h` score `0.2077` n `122` status `ready` deltaP `8.5673` edge `0.0047` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.2077` n `122` status `ready` deltaP `8.5673` edge `0.0047` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
