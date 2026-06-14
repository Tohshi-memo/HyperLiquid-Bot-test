# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T16:07:28.758897+00:00`
- Price records: `672`
- Market context records: `3907`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11356`

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

- `risk_on_high->unknown_4h` score `46.9041` n `72` status `ready` deltaP `4.2174` edge `6.1994` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `46.9041` n `72` status `ready` deltaP `4.2174` edge `6.1994` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `23.7349` n `40` status `ready` deltaP `17.0833` edge `1.99` maxDD `-7.0785`
- `risk_on_and_context->crypto_major_24h` score `23.7349` n `40` status `ready` deltaP `17.0833` edge `1.99` maxDD `-7.0785`
- `risk_on_high->equity_24h` score `22.9127` n `40` status `ready` deltaP `42.0139` edge `1.6293` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.9127` n `40` status `ready` deltaP `42.0139` edge `1.6293` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `11.7662` n `40` status `ready` deltaP `15.0` edge `1.0786` maxDD `-12.8464`
- `risk_on_and_context->crypto_alt_24h` score `11.7662` n `40` status `ready` deltaP `15.0` edge `1.0786` maxDD `-12.8464`
- `risk_on_high->index_24h` score `9.4288` n `40` status `ready` deltaP `30.0347` edge `0.5855` maxDD `0.0`
- `risk_on_and_context->index_24h` score `9.4288` n `40` status `ready` deltaP `30.0347` edge `0.5855` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.6166` n `208` status `ready` deltaP `-1.7121` edge `1.4006` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.2856` n `165` status `ready` deltaP `20.8018` edge `0.6881` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.7628` n `72` status `ready` deltaP `20.5284` edge `0.4556` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.7628` n `72` status `ready` deltaP `20.5284` edge `0.4556` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.6896` n `165` status `ready` deltaP `25.7923` edge `0.3328` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.8963` n `165` status `ready` deltaP `19.3245` edge `0.2557` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.7949` n `208` status `ready` deltaP `17.0028` edge `0.296` maxDD `-9.4488`
- `risk_on_high->equity_4h` score `2.5809` n `72` status `ready` deltaP `24.9492` edge `0.1622` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5809` n `72` status `ready` deltaP `24.9492` edge `0.1622` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.2355` n `165` status `ready` deltaP `2.6136` edge `0.5319` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
