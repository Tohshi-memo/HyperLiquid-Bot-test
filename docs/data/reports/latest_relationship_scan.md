# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T05:07:18.507812+00:00`
- Price records: `672`
- Market context records: `942`
- Flow alert records: `2639`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `1320`

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

- `risk_on_high->crypto_major_24h` score `22.3372` n `32` status `ready` deltaP `33.6806` edge `1.6369` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.3372` n `32` status `ready` deltaP `33.6806` edge `1.6369` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.4638` n `169` status `ready` deltaP `30.722` edge `1.0339` maxDD `-1.3382`
- `risk_on_high->crypto_alt_24h` score `13.59` n `32` status `ready` deltaP `6.9444` edge `1.0862` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.59` n `32` status `ready` deltaP `6.9444` edge `1.0862` maxDD `0.0`
- `risk_on_high->equity_24h` score `12.8468` n `32` status `ready` deltaP `25.0` edge `0.9039` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.8468` n `32` status `ready` deltaP `25.0` edge `0.9039` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.5348` n `169` status `ready` deltaP `6.9444` edge `0.5816` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9497` n `32` status `ready` deltaP `26.7361` edge `0.1509` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9497` n `32` status `ready` deltaP `26.7361` edge `0.1509` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.3771` n `32` status `ready` deltaP `24.314` edge `0.1398` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.3771` n `32` status `ready` deltaP `24.314` edge `0.1398` maxDD `-0.6377`
- `risk_on_high->equity_4h` score `3.0025` n `32` status `ready` deltaP `4.0396` edge `0.2598` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.0025` n `32` status `ready` deltaP `4.0396` edge `0.2598` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.8955` n `32` status `ready` deltaP `21.4939` edge `0.1352` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8955` n `32` status `ready` deltaP `21.4939` edge `0.1352` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.1351` n `32` status `ready` deltaP `9.6799` edge `0.1222` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.1351` n `32` status `ready` deltaP `9.6799` edge `0.1222` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `0.9575` n `32` status `ready` deltaP `-13.1944` edge `0.2853` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `0.9575` n `32` status `ready` deltaP `-13.1944` edge `0.2853` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
