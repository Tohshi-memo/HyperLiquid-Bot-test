# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T05:37:14.644185+00:00`
- Price records: `672`
- Market context records: `945`
- Flow alert records: `2645`
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

- `risk_on_high->crypto_major_24h` score `22.5318` n `32` status `ready` deltaP `34.0278` edge `1.6508` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.5318` n `32` status `ready` deltaP `34.0278` edge `1.6508` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.6584` n `169` status `ready` deltaP `31.0692` edge `1.0478` maxDD `-1.3382`
- `risk_on_high->crypto_alt_24h` score `13.7965` n `32` status `ready` deltaP `7.2917` edge `1.1011` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.7965` n `32` status `ready` deltaP `7.2917` edge `1.1011` maxDD `0.0`
- `risk_on_high->equity_24h` score `12.8564` n `32` status `ready` deltaP `25.0` edge `0.9047` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.8564` n `32` status `ready` deltaP `25.0` edge `0.9047` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.7413` n `169` status `ready` deltaP `7.2917` edge `0.5965` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9497` n `32` status `ready` deltaP `26.7361` edge `0.1509` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9497` n `32` status `ready` deltaP `26.7361` edge `0.1509` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.3663` n `32` status `ready` deltaP `24.314` edge `0.1389` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.3663` n `32` status `ready` deltaP `24.314` edge `0.1389` maxDD `-0.6377`
- `risk_on_high->equity_4h` score `2.9589` n `32` status `ready` deltaP `3.7348` edge `0.2582` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `2.9589` n `32` status `ready` deltaP `3.7348` edge `0.2582` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.8859` n `32` status `ready` deltaP `21.4939` edge `0.1344` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8859` n `32` status `ready` deltaP `21.4939` edge `0.1344` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.1351` n `32` status `ready` deltaP `9.6799` edge `0.1222` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.1351` n `32` status `ready` deltaP `9.6799` edge `0.1222` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `0.9528` n `32` status `ready` deltaP `-13.1944` edge `0.2847` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `0.9528` n `32` status `ready` deltaP `-13.1944` edge `0.2847` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
