# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T09:07:39.310558+00:00`
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

- `risk_on_high->crypto_alt_24h` score `8.1567` n `117` status `ready` deltaP `20.2057` edge `0.568` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.1567` n `117` status `ready` deltaP `20.2057` edge `0.568` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8488` n `117` status `ready` deltaP `31.8545` edge `0.3122` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8488` n `117` status `ready` deltaP `31.8545` edge `0.3122` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.9638` n `117` status `ready` deltaP `21.1005` edge `0.9025` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.9638` n `117` status `ready` deltaP `21.1005` edge `0.9025` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8377` n `117` status `ready` deltaP `25.9811` edge `0.3158` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8377` n `117` status `ready` deltaP `25.9811` edge `0.3158` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.1092` n `241` status `ready` deltaP `12.8609` edge `0.2561` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.907` n `117` status `ready` deltaP `3.7976` edge `0.0855` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.907` n `117` status `ready` deltaP `3.7976` edge `0.0855` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.7794` n `117` status `ready` deltaP `9.7623` edge `0.0041` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.7794` n `117` status `ready` deltaP `9.7623` edge `0.0041` maxDD `-0.0051`
- `risk_on_high->equity_1h` score `0.5252` n `117` status `ready` deltaP `14.672` edge `-0.0009` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.5252` n `117` status `ready` deltaP `14.672` edge `-0.0009` maxDD `-2.2516`
- `risk_on_high->metal_1h` score `0.2575` n `117` status `ready` deltaP `9.6794` edge `0.0015` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2575` n `117` status `ready` deltaP `9.6794` edge `0.0015` maxDD `-0.3081`
- `risk_on_high->crypto_major_1h` score `0.2313` n `117` status `ready` deltaP `3.8846` edge `0.0661` maxDD `-3.1509`
- `risk_on_and_context->crypto_major_1h` score `0.2313` n `117` status `ready` deltaP `3.8846` edge `0.0661` maxDD `-3.1509`
- `risk_on_high->index_1h` score `0.1967` n `117` status `ready` deltaP `9.7178` edge `-0.0032` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
