# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T14:07:37.134866+00:00`
- Price records: `672`
- Market context records: `3998`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10226`

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

- `risk_on_high->unknown_4h` score `146.9366` n `40` status `ready` deltaP `-2.561` edge `12.443` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `146.9366` n `40` status `ready` deltaP `-2.561` edge `12.443` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `44.7383` n `139` status `ready` deltaP `-3.8781` edge `4.1559` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `24.7477` n `151` status `ready` deltaP `2.1907` edge `2.5886` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.2327` n `40` status `ready` deltaP `42.0139` edge `0.4893` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2327` n `40` status `ready` deltaP `42.0139` edge `0.4893` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.0264` n `40` status `ready` deltaP `38.2012` edge `0.0856` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.0264` n `40` status `ready` deltaP `38.2012` edge `0.0856` maxDD `-0.0458`
- `market_context_high->index_24h` score `2.9706` n `139` status `ready` deltaP `25.5446` edge `0.1912` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.9063` n `139` status `ready` deltaP `14.9243` edge `0.2942` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.7213` n `40` status `ready` deltaP `29.8611` edge `0.0277` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7213` n `40` status `ready` deltaP `29.8611` edge `0.0277` maxDD `0.0`
- `market_context_high->equity_4h` score `2.1325` n `151` status `ready` deltaP `20.1714` edge `0.1735` maxDD `-7.0879`
- `market_context_high->equity_24h` score `1.8522` n `139` status `ready` deltaP `16.834` edge `0.3451` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.6398` n `40` status `ready` deltaP `20.6707` edge `0.0654` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6398` n `40` status `ready` deltaP `20.6707` edge `0.0654` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.2659` n `151` status `ready` deltaP `12.8505` edge `0.0673` maxDD `-1.7983`
- `market_context_high->crypto_major_4h` score `1.1842` n `151` status `ready` deltaP `17.7071` edge `0.1373` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.1772` n `151` status `ready` deltaP `10.9678` edge `0.0792` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `1.0227` n `40` status `ready` deltaP `4.1667` edge `0.2856` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
