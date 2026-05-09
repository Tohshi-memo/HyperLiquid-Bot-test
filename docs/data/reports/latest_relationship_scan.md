# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T19:22:19.985706+00:00`
- Price records: `672`
- Market context records: `897`
- Flow alert records: `2517`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `21.3673` n `32` status `ready` deltaP `31.7708` edge `1.5688` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.3673` n `32` status `ready` deltaP `31.7708` edge `1.5688` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.4938` n `169` status `ready` deltaP `28.8122` edge `0.9658` maxDD `-1.3382`
- `risk_on_high->equity_24h` score `13.1158` n `32` status `ready` deltaP `25.3472` edge `0.924` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.1158` n `32` status `ready` deltaP `25.3472` edge `0.924` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `12.5581` n `32` status `ready` deltaP `6.0764` edge `1.006` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.5581` n `32` status `ready` deltaP `6.0764` edge `1.006` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.5029` n `169` status `ready` deltaP `6.0764` edge `0.5014` maxDD `0.0`
- `risk_on_high->index_24h` score `4.2413` n `32` status `ready` deltaP `27.9514` edge `0.1671` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.2413` n `32` status `ready` deltaP `27.9514` edge `0.1671` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.5482` n `32` status `ready` deltaP `8.4604` edge `0.2758` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.5482` n `32` status `ready` deltaP `8.4604` edge `0.2758` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `3.5201` n `32` status `ready` deltaP `24.4665` edge `0.1507` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.5201` n `32` status `ready` deltaP `24.4665` edge `0.1507` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `3.0195` n `32` status `ready` deltaP `21.7988` edge `0.1435` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `3.0195` n `32` status `ready` deltaP `21.7988` edge `0.1435` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5691` n `32` status `ready` deltaP `14.1006` edge `0.1289` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5691` n `32` status `ready` deltaP `14.1006` edge `0.1289` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.3892` n `32` status `ready` deltaP `-9.7222` edge `0.3175` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.3892` n `32` status `ready` deltaP `-9.7222` edge `0.3175` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
