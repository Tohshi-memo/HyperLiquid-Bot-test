# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T02:07:29.720786+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11593`

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

- `risk_on_high->equity_24h` score `5.6587` n `107` status `ready` deltaP `25.0909` edge `0.7188` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.6587` n `107` status `ready` deltaP `25.0909` edge `0.7188` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `4.5661` n `107` status `ready` deltaP `17.7813` edge `0.3238` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `4.5661` n `107` status `ready` deltaP `17.7813` edge `0.3238` maxDD `-2.2797`
- `news_risk_high->equity_24h` score `2.6588` n `59` status `ready` deltaP `11.0405` edge `0.3947` maxDD `-15.4056`
- `market_context_high->unknown_4h` score `2.6468` n `147` status `ready` deltaP `13.5153` edge `0.2` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `2.4243` n `110` status `ready` deltaP `1.9706` edge `0.2466` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `2.4243` n `110` status `ready` deltaP `1.9706` edge `0.2466` maxDD `-1.95`
- `risk_on_high->crypto_alt_24h` score `2.3271` n `107` status `ready` deltaP `21.2568` edge `0.847` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3271` n `107` status `ready` deltaP `21.2568` edge `0.847` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2981` n `59` status `ready` deltaP `21.1776` edge `0.4469` maxDD `-19.4761`
- `market_context_high->equity_24h` score `2.0235` n `147` status `ready` deltaP `21.0601` edge `0.5999` maxDD `-24.4698`
- `market_context_high->unknown_1h` score `1.0564` n `152` status `ready` deltaP `0.583` edge `0.1472` maxDD `-2.0446`
- `news_risk_high->crypto_major_24h` score `1.0467` n `59` status `ready` deltaP `14.348` edge `0.4299` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.528` n `107` status `ready` deltaP `20.6841` edge `0.8042` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.528` n `107` status `ready` deltaP `20.6841` edge `0.8042` maxDD `-56.9519`
- `market_context_high->crypto_alt_24h` score `0.4739` n `147` status `ready` deltaP `15.2742` edge `0.7088` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.3655` n `147` status `ready` deltaP `23.7104` edge `0.8352` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.1898` n `67` status `ready` deltaP `5.0328` edge `0.0267` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.1313` n `110` status `ready` deltaP `8.4812` edge `0.0048` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
