# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T10:22:28.707300+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9833`

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

- `market_context_high->unknown_24h` score `36.8463` n `46` status `ready` deltaP `23.8678` edge `2.9157` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `8.1381` n `46` status `ready` deltaP `41.9158` edge `0.4161` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `7.9234` n `46` status `ready` deltaP `36.5262` edge `0.4347` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.5437` n `88` status `ready` deltaP `1.0532` edge `0.5545` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1956` n `88` status `ready` deltaP `15.3687` edge `0.0818` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2433` n `88` status `ready` deltaP `5.8315` edge `0.023` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2369` n `88` status `ready` deltaP `16.2555` edge `0.008` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1293` n `88` status `ready` deltaP `7.383` edge `-0.0036` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4764` n `88` status `ready` deltaP `1.429` edge `-0.0172` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5533` n `88` status `ready` deltaP `-1.7692` edge `-0.0097` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.612` n `88` status `ready` deltaP `3.9773` edge `0.0185` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.9395` n `88` status `ready` deltaP `3.5615` edge `-0.0052` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2371` n `88` status `ready` deltaP `-3.1709` edge `-0.0109` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5946` n `88` status `ready` deltaP `5.015` edge `-0.0843` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.8831` n `88` status `ready` deltaP `-10.4213` edge `-0.0465` maxDD `-4.7021`
- `market_context_high->fx_24h` score `-1.9665` n `46` status `ready` deltaP `-7.0048` edge `0.0034` maxDD `-4.3126`
- `market_context_high->unknown_1h` score `-3.4747` n `88` status `ready` deltaP `2.0006` edge `-0.2582` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6343` n `88` status `ready` deltaP `-12.9491` edge `-0.0792` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.9939` n `46` status `ready` deltaP `-25.2038` edge `-0.1313` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.8576` n `88` status `ready` deltaP `-0.7345` edge `-0.3412` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
