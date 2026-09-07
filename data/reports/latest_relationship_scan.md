# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T02:37:24.159341+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10761`

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

- `risk_on_high->unknown_24h` score `472.7249` n `97` status `ready` deltaP `26.7361` edge `39.2155` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `472.7249` n `97` status `ready` deltaP `26.7361` edge `39.2155` maxDD `0.0`
- `market_context_high->unknown_1h` score `21.7589` n `245` status `ready` deltaP `-2.8358` edge `1.9046` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `20.3824` n `97` status `ready` deltaP `33.6035` edge `1.5262` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.3824` n `97` status `ready` deltaP `33.6035` edge `1.5262` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `14.0604` n `97` status `ready` deltaP `30.5556` edge `0.968` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.0604` n `97` status `ready` deltaP `30.5556` edge `0.968` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.9303` n `186` status `ready` deltaP `24.104` edge `0.641` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.5992` n `186` status `ready` deltaP `23.0903` edge `0.396` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.461` n `120` status `ready` deltaP `28.9126` edge `0.2995` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.461` n `120` status `ready` deltaP `28.9126` edge `0.2995` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.4556` n `97` status `ready` deltaP `23.0903` edge `0.3007` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.4556` n `97` status `ready` deltaP `23.0903` edge `0.3007` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.9299` n `120` status `ready` deltaP `22.0732` edge `0.2662` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.9299` n `120` status `ready` deltaP `22.0732` edge `0.2662` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7213` n `97` status `ready` deltaP `23.2961` edge `0.0757` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7213` n `97` status `ready` deltaP `23.2961` edge `0.0757` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.604` n `186` status `ready` deltaP `21.5502` edge `0.0948` maxDD `-0.0505`
- `risk_on_high->metal_24h` score `0.9041` n `97` status `ready` deltaP `16.153` edge `0.1238` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.9041` n `97` status `ready` deltaP `16.153` edge `0.1238` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
