# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T01:07:37.764603+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11545`

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

- `risk_on_high->equity_24h` score `5.7403` n `107` status `ready` deltaP `25.0909` edge `0.7256` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.7403` n `107` status `ready` deltaP `25.0909` edge `0.7256` maxDD `-19.828`
- `risk_on_high->unknown_4h` score `5.7189` n `107` status `ready` deltaP `18.391` edge `0.4158` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `5.7189` n `107` status `ready` deltaP `18.391` edge `0.4158` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `3.7995` n `147` status `ready` deltaP `14.125` edge `0.292` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.7404` n `59` status `ready` deltaP `11.0405` edge `0.4015` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `2.2725` n `107` status `ready` deltaP `21.2568` edge `0.84` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.2725` n `107` status `ready` deltaP `21.2568` edge `0.84` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2435` n `59` status `ready` deltaP `21.1776` edge `0.4399` maxDD `-19.4761`
- `market_context_high->equity_24h` score `2.0766` n `147` status `ready` deltaP `21.0601` edge `0.6067` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `0.8655` n `59` status `ready` deltaP `14.348` edge `0.4148` maxDD `-30.7329`
- `market_context_high->crypto_alt_24h` score `0.4193` n `147` status `ready` deltaP `15.2742` edge `0.7018` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.4102` n `107` status `ready` deltaP `20.6841` edge `0.7891` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.4102` n `107` status `ready` deltaP `20.6841` edge `0.7891` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.2477` n `147` status `ready` deltaP `23.7104` edge `0.8201` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2301` n `67` status `ready` deltaP `5.6425` edge `0.0278` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.108` n `107` status `ready` deltaP `8.0936` edge `0.0044` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.108` n `107` status `ready` deltaP `8.0936` edge `0.0044` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.0613` n `107` status `ready` deltaP `19.5635` edge `0.0105` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.0613` n `107` status `ready` deltaP `19.5635` edge `0.0105` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
