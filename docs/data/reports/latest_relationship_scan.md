# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T02:37:30.624262+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10385`

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

- `market_context_high->unknown_24h` score `2093.5007` n `241` status `ready` deltaP `18.2673` edge `174.3418` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `2064.1922` n `117` status `ready` deltaP `19.0972` edge `171.8887` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `2064.1922` n `117` status `ready` deltaP `19.0972` edge `171.8887` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `9.031` n `117` status `ready` deltaP `24.0251` edge `0.6154` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.031` n `117` status `ready` deltaP `24.0251` edge `0.6154` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.9408` n `117` status `ready` deltaP `31.5497` edge `0.3219` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9408` n `117` status `ready` deltaP `31.5497` edge `0.3219` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.1845` n `117` status `ready` deltaP `21.1005` edge `0.9308` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.1845` n `117` status `ready` deltaP `21.1005` edge `0.9308` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8939` n `117` status `ready` deltaP `25.8287` edge `0.3215` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8939` n `117` status `ready` deltaP `25.8287` edge `0.3215` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.9836` n `241` status `ready` deltaP `16.6803` edge `0.3035` maxDD `-3.9523`
- `market_context_high->equity_24h` score `1.4884` n `241` status `ready` deltaP `10.0694` edge `0.0569` maxDD `0.0`
- `risk_on_high->index_24h` score `1.2012` n `117` status `ready` deltaP `12.0192` edge `0.0242` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.2012` n `117` status `ready` deltaP `12.0192` edge `0.0242` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.9094` n `117` status `ready` deltaP `3.7976` edge `0.0857` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9094` n `117` status `ready` deltaP `3.7976` edge `0.0857` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `0.8032` n `117` status `ready` deltaP `10.0694` edge `-0.0002` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.8032` n `117` status `ready` deltaP `10.0694` edge `-0.0002` maxDD `0.0`
- `market_context_high->index_24h` score `0.4797` n `241` status `ready` deltaP `7.1144` edge `0.0319` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
