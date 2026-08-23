# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T22:22:24.019582+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `57.4438` n `31` status `ready` deltaP `17.1875` edge `4.6724` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.3579` n `31` status `ready` deltaP `51.6073` edge `1.2173` maxDD `-1.522`
- `news_risk_high->unknown_4h` score `13.0757` n `51` status `ready` deltaP `23.4965` edge `0.9376` maxDD `-0.0348`
- `news_risk_high->index_24h` score `6.7797` n `31` status `ready` deltaP `56.5692` edge `0.1963` maxDD `-0.0095`
- `news_risk_high->crypto_alt_24h` score `5.7552` n `31` status `ready` deltaP `28.125` edge `0.2921` maxDD `0.0`
- `risk_on_high->unknown_1h` score `3.8912` n `37` status `ready` deltaP `-9.5606` edge `0.6075` maxDD `-1.5916`
- `risk_on_and_context->unknown_1h` score `3.8912` n `37` status `ready` deltaP `-9.5606` edge `0.6075` maxDD `-1.5916`
- `news_risk_high->fx_4h` score `3.0265` n `51` status `ready` deltaP `35.7963` edge `0.027` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.0018` n `51` status `ready` deltaP `16.0355` edge `0.1737` maxDD `-0.7693`
- `risk_on_high->equity_4h` score `2.8119` n `37` status `ready` deltaP `2.7934` edge `0.2587` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `2.8119` n `37` status `ready` deltaP `2.7934` edge `0.2587` maxDD `-0.773`
- `news_risk_high->equity_4h` score `2.55` n `51` status `ready` deltaP `22.5072` edge `0.1395` maxDD `-2.164`
- `news_risk_high->metal_24h` score `2.4439` n `31` status `ready` deltaP `40.1042` edge `-0.0637` maxDD `0.0`
- `risk_on_high->metal_4h` score `2.2605` n `37` status `ready` deltaP `29.8904` edge `-0.0021` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2605` n `37` status `ready` deltaP `29.8904` edge `-0.0021` maxDD `-0.0367`
- `market_context_high->unknown_1h` score `1.4288` n `150` status `ready` deltaP `8.3493` edge `0.1083` maxDD `-1.5916`
- `market_context_high->unknown_4h` score `1.4272` n `138` status `ready` deltaP `21.1095` edge `-0.0081` maxDD `-0.0956`
- `news_risk_high->fx_1h` score `1.2302` n `51` status `ready` deltaP `16.8457` edge `0.0072` maxDD `-0.0257`
- `market_context_high->crypto_alt_4h` score `1.1346` n `138` status `ready` deltaP `11.1125` edge `0.1669` maxDD `-7.0478`
- `risk_on_high->index_4h` score `0.9532` n `37` status `ready` deltaP `12.4671` edge `0.0443` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
