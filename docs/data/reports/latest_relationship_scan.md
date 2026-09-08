# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T02:07:29.341766+00:00`
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

- `market_context_high->unknown_24h` score `2414.0497` n `241` status `ready` deltaP `18.6145` edge `201.0519` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `2384.7412` n `117` status `ready` deltaP `19.4444` edge `198.5988` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `2384.7412` n `117` status `ready` deltaP `19.4444` edge `198.5988` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `9.1272` n `117` status `ready` deltaP `24.3723` edge `0.6211` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.1272` n `117` status `ready` deltaP `24.3723` edge `0.6211` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.948` n `117` status `ready` deltaP `31.5497` edge `0.3225` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.948` n `117` status `ready` deltaP `31.5497` edge `0.3225` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.2072` n `117` status `ready` deltaP `21.1005` edge `0.9337` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.2072` n `117` status `ready` deltaP `21.1005` edge `0.9337` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8891` n `117` status `ready` deltaP `25.8287` edge `0.3211` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8891` n `117` status `ready` deltaP `25.8287` edge `0.3211` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `4.0798` n `241` status `ready` deltaP `17.0275` edge `0.3092` maxDD `-3.9523`
- `market_context_high->equity_24h` score `1.6397` n `241` status `ready` deltaP `10.4167` edge `0.0672` maxDD `0.0`
- `risk_on_high->index_24h` score `1.2518` n `117` status `ready` deltaP `12.3665` edge `0.0261` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.2518` n `117` status `ready` deltaP `12.3665` edge `0.0261` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `0.9545` n `117` status `ready` deltaP `10.4167` edge `0.0101` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.9545` n `117` status `ready` deltaP `10.4167` edge `0.0101` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `0.8782` n `117` status `ready` deltaP `3.6479` edge `0.0841` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8782` n `117` status `ready` deltaP `3.6479` edge `0.0841` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.5303` n `241` status `ready` deltaP `7.4617` edge `0.0338` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
