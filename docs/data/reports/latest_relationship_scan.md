# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T09:37:29.850834+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10233`

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

- `risk_on_high->crypto_alt_24h` score `8.0893` n `117` status `ready` deltaP `19.8584` edge `0.5647` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.0893` n `117` status `ready` deltaP `19.8584` edge `0.5647` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8658` n `117` status `ready` deltaP `32.007` edge `0.3126` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8658` n `117` status `ready` deltaP `32.007` edge `0.3126` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.9342` n `117` status `ready` deltaP `21.1005` edge `0.8987` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.9342` n `117` status `ready` deltaP `21.1005` edge `0.8987` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8183` n `117` status `ready` deltaP `25.8287` edge `0.3152` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8183` n `117` status `ready` deltaP `25.8287` edge `0.3152` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.0418` n `241` status `ready` deltaP `12.5136` edge `0.2528` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.9046` n `117` status `ready` deltaP `3.7976` edge `0.0853` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9046` n `117` status `ready` deltaP `3.7976` edge `0.0853` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.7722` n `117` status `ready` deltaP `9.7623` edge `0.0035` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.7722` n `117` status `ready` deltaP `9.7623` edge `0.0035` maxDD `-0.0051`
- `risk_on_high->equity_1h` score `0.5216` n `117` status `ready` deltaP `14.672` edge `-0.0012` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.5216` n `117` status `ready` deltaP `14.672` edge `-0.0012` maxDD `-2.2516`
- `risk_on_high->metal_1h` score `0.2598` n `117` status `ready` deltaP `9.6794` edge `0.0018` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2598` n `117` status `ready` deltaP `9.6794` edge `0.0018` maxDD `-0.3081`
- `risk_on_high->crypto_major_1h` score `0.2349` n `117` status `ready` deltaP `3.8846` edge `0.0664` maxDD `-3.1509`
- `risk_on_and_context->crypto_major_1h` score `0.2349` n `117` status `ready` deltaP `3.8846` edge `0.0664` maxDD `-3.1509`
- `risk_on_high->index_1h` score `0.1959` n `117` status `ready` deltaP `9.7178` edge `-0.0033` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
