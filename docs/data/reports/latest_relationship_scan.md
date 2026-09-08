# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T06:07:27.785308+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10223`

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

- `risk_on_high->crypto_alt_24h` score `8.5133` n `117` status `ready` deltaP `21.7682` edge `0.5873` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.5133` n `117` status `ready` deltaP `21.7682` edge `0.5873` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.84` n `117` status `ready` deltaP `31.5497` edge `0.3135` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.84` n `117` status `ready` deltaP `31.5497` edge `0.3135` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.0582` n `117` status `ready` deltaP `21.1005` edge `0.9146` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.0582` n `117` status `ready` deltaP `21.1005` edge `0.9146` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8679` n `117` status `ready` deltaP `26.1335` edge `0.3173` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8679` n `117` status `ready` deltaP `26.1335` edge `0.3173` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.4658` n `241` status `ready` deltaP `14.4234` edge `0.2754` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `1.0065` n `117` status `ready` deltaP `4.097` edge `0.0918` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0065` n `117` status `ready` deltaP `4.097` edge `0.0918` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.8454` n `117` status `ready` deltaP `9.7623` edge `0.0096` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.8454` n `117` status `ready` deltaP `9.7623` edge `0.0096` maxDD `-0.0051`
- `risk_on_high->equity_1h` score `0.6031` n `117` status `ready` deltaP `15.1211` edge `0.0026` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.6031` n `117` status `ready` deltaP `15.1211` edge `0.0026` maxDD `-2.2516`
- `market_context_high->equity_24h` score `0.4522` n `241` status `ready` deltaP `7.8125` edge `-0.0144` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.362` n `117` status `ready` deltaP `4.6331` edge `0.072` maxDD `-3.1509`
- `risk_on_and_context->crypto_major_1h` score `0.362` n `117` status `ready` deltaP `4.6331` edge `0.072` maxDD `-3.1509`
- `risk_on_high->metal_1h` score `0.2926` n `117` status `ready` deltaP `9.9788` edge `0.004` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2926` n `117` status `ready` deltaP `9.9788` edge `0.004` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
