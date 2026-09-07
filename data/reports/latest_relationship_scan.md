# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T23:07:35.126436+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10273`

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

- `risk_on_high->unknown_24h` score `4332.3153` n `117` status `ready` deltaP `20.4861` edge `360.8897` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `4332.3153` n `117` status `ready` deltaP `20.4861` edge `360.8897` maxDD `0.0`
- `market_context_high->unknown_24h` score `2549.5912` n `236` status `ready` deltaP `19.6386` edge `212.3402` maxDD `-0.0819`
- `risk_on_high->crypto_alt_24h` score `9.5093` n `117` status `ready` deltaP `25.414` edge `0.646` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.5093` n `117` status `ready` deltaP `25.414` edge `0.646` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.832` n `117` status `ready` deltaP `30.9399` edge `0.3169` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.832` n `117` status `ready` deltaP `30.9399` edge `0.3169` maxDD `-1.9733`
- `market_context_high->crypto_alt_24h` score `5.397` n `236` status `ready` deltaP `19.9417` edge `0.3743` maxDD `-2.5998`
- `risk_on_high->crypto_major_24h` score `5.3382` n `117` status `ready` deltaP `21.1005` edge `0.9505` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.3382` n `117` status `ready` deltaP `21.1005` edge `0.9505` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8167` n `117` status `ready` deltaP `25.5238` edge `0.3171` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8167` n `117` status `ready` deltaP `25.5238` edge `0.3171` maxDD `-3.8693`
- `market_context_high->equity_24h` score `2.5684` n `236` status `ready` deltaP `12.5` edge `0.1307` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.7944` n `117` status `ready` deltaP `12.5` edge `0.0662` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7944` n `117` status `ready` deltaP `12.5` edge `0.0662` maxDD `0.0`
- `risk_on_high->index_24h` score `1.5372` n `117` status `ready` deltaP `14.4498` edge `0.036` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.5372` n `117` status `ready` deltaP `14.4498` edge `0.036` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.0089` n `117` status `ready` deltaP `4.5461` edge `0.089` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0089` n `117` status `ready` deltaP `4.5461` edge `0.089` maxDD `-1.1521`
- `market_context_high->index_24h` score `0.8139` n `236` status `ready` deltaP `9.3868` edge `0.0446` maxDD `-0.1483`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
