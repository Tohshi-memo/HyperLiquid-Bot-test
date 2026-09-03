# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T03:37:26.070553+00:00`
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

- `risk_on_high->equity_24h` score `5.4442` n `107` status `ready` deltaP `24.57` edge `0.7044` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.4442` n `107` status `ready` deltaP `24.57` edge `0.7044` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `4.5061` n `107` status `ready` deltaP `17.7813` edge `0.3188` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `4.5061` n `107` status `ready` deltaP `17.7813` edge `0.3188` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `2.5868` n `147` status `ready` deltaP `13.5153` edge `0.195` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.4443` n `59` status `ready` deltaP `10.5196` edge `0.3803` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `2.3302` n `107` status `ready` deltaP `21.2568` edge `0.8474` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3302` n `107` status `ready` deltaP `21.2568` edge `0.8474` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.3013` n `59` status `ready` deltaP `21.1776` edge `0.4473` maxDD `-19.4761`
- `risk_on_high->unknown_1h` score `2.0887` n `116` status `ready` deltaP `2.0803` edge `0.2179` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `2.0887` n `116` status `ready` deltaP `2.0803` edge `0.2179` maxDD `-1.95`
- `market_context_high->equity_24h` score `1.8841` n `147` status `ready` deltaP `20.5392` edge `0.5855` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `1.1895` n `59` status `ready` deltaP `14.348` edge `0.4418` maxDD `-30.7329`
- `market_context_high->unknown_1h` score `0.8498` n `158` status `ready` deltaP `0.7162` edge `0.1291` maxDD `-2.0446`
- `risk_on_high->crypto_major_24h` score `0.6208` n `107` status `ready` deltaP `20.6841` edge `0.8161` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.6208` n `107` status `ready` deltaP `20.6841` edge `0.8161` maxDD `-56.9519`
- `market_context_high->crypto_alt_24h` score `0.477` n `147` status `ready` deltaP `15.2742` edge `0.7092` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.4583` n `147` status `ready` deltaP `23.7104` edge `0.8471` maxDD `-61.3797`
- `risk_on_high->index_1h` score `0.2893` n `116` status `ready` deltaP `9.4828` edge `0.0054` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.2893` n `116` status `ready` deltaP `9.4828` edge `0.0054` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
