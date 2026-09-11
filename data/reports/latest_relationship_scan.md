# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T22:37:25.342228+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11335`

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

- `news_risk_high->unknown_1h` score `462.3828` n `76` status `ready` deltaP `-4.1601` edge `38.6018` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.5281` n `91` status `ready` deltaP `42.943` edge `1.7807` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.5281` n `91` status `ready` deltaP `42.943` edge `1.7807` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.1139` n `35` status `ready` deltaP `49.8561` edge `1.6005` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.6185` n `151` status `ready` deltaP `37.8415` edge `1.632` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `12.809` n `35` status `ready` deltaP `19.8661` edge `0.9796` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `9.913` n `35` status `ready` deltaP `31.2649` edge `0.6275` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.4239` n `91` status `ready` deltaP `36.9792` edge `0.5388` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.4239` n `91` status `ready` deltaP `36.9792` edge `0.5388` maxDD `0.0`
- `market_context_high->equity_24h` score `9.1347` n `151` status `ready` deltaP `36.9792` edge `0.5147` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6923` n `91` status `ready` deltaP `42.7081` edge `0.4768` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6923` n `91` status `ready` deltaP `42.7081` edge `0.4768` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.9341` n `35` status `ready` deltaP `51.0417` edge `0.3209` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.7144` n `91` status `ready` deltaP `25.021` edge `1.229` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.7144` n `91` status `ready` deltaP `25.021` edge `1.229` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.6262` n `35` status `ready` deltaP `49.1468` edge `0.3172` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.6833` n `91` status `ready` deltaP `31.5918` edge `0.4322` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.6833` n `91` status `ready` deltaP `31.5918` edge `0.4322` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3728` n `91` status `ready` deltaP `51.5644` edge `0.1082` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3728` n `91` status `ready` deltaP `51.5644` edge `0.1082` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
