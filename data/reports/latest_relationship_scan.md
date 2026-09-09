# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T23:37:30.426146+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.571` n `117` status `ready` deltaP `27.1501` edge `0.9729` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.571` n `117` status `ready` deltaP `27.1501` edge `0.9729` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `8.5236` n `241` status `ready` deltaP `19.8053` edge `0.661` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `7.4183` n `117` status `ready` deltaP `22.8366` edge `1.2056` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.4183` n `117` status `ready` deltaP `22.8366` edge `1.2056` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.8544` n `117` status `ready` deltaP `35.6655` edge `0.3706` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.8544` n `117` status `ready` deltaP `35.6655` edge `0.3706` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8159` n `117` status `ready` deltaP `25.8287` edge `0.315` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8159` n `117` status `ready` deltaP `25.8287` edge `0.315` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7589` n `117` status `ready` deltaP `27.4706` edge `0.051` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7589` n `117` status `ready` deltaP `27.4706` edge `0.051` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.039` n `241` status `ready` deltaP `10.9375` edge `0.097` maxDD `0.0`
- `market_context_high->index_24h` score `2.0374` n `241` status `ready` deltaP `22.5658` edge `0.0587` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.3538` n `117` status `ready` deltaP `10.9375` edge `0.0399` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.3538` n `117` status `ready` deltaP `10.9375` edge `0.0399` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.232` n `117` status `ready` deltaP `4.8455` edge `0.1056` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.232` n `117` status `ready` deltaP `4.8455` edge `0.1056` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.8136` n `117` status `ready` deltaP `19.7383` edge `0.0883` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.8136` n `117` status `ready` deltaP `19.7383` edge `0.0883` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.494` n `117` status `ready` deltaP `14.8217` edge `-0.0045` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
