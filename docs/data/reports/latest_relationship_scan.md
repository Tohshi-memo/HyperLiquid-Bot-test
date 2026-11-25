# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T14:52:33.538548+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32204.7829` n `45` status `ready` deltaP `2.465` edge `2683.7249` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21918.5149` n `45` status `ready` deltaP `3.1776` edge `1826.5356` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `969.8279` n `31` status `ready` deltaP `2.6801` edge `80.8187` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `665.5674` n `31` status `ready` deltaP `4.3962` edge `55.4403` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `493.9787` n `31` status `ready` deltaP `5.7292` edge `41.1267` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.0104` n `31` status `ready` deltaP `50.6944` edge `3.4129` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.809` n `31` status `ready` deltaP `52.2569` edge `3.1357` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.4125` n `31` status `ready` deltaP `54.8611` edge `2.8353` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.9249` n `31` status `ready` deltaP `27.3701` edge `0.8983` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.8934` n `31` status `ready` deltaP `41.2355` edge `0.7437` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.2919` n `31` status `ready` deltaP `37.9869` edge `0.7358` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5026` n `31` status `ready` deltaP `19.0647` edge `0.9765` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.1687` n `31` status `ready` deltaP `51.3889` edge `0.2548` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3329` n `31` status `ready` deltaP `45.5309` edge `0.1537` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0469` n `31` status `ready` deltaP `20.8856` edge `0.2167` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4268` n `31` status `ready` deltaP `36.4625` edge `0.0685` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7674` n `31` status `ready` deltaP `11.807` edge `0.3222` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7226` n `31` status `ready` deltaP `31.9925` edge `0.0221` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.5115` n `31` status `ready` deltaP `13.6034` edge `0.267` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.4834` n `45` status `ready` deltaP `30.3929` edge `0.0328` maxDD `-0.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
