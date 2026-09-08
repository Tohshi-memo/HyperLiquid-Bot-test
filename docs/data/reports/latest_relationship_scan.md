# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T04:22:31.628892+00:00`
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

- `market_context_high->unknown_24h` score `1017.9414` n `241` status `ready` deltaP `17.2257` edge `84.7188` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `988.6328` n `117` status `ready` deltaP `18.0556` edge `82.2657` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `988.6328` n `117` status `ready` deltaP `18.0556` edge `82.2657` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `8.7929` n `117` status `ready` deltaP `22.9834` edge `0.6025` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.7929` n `117` status `ready` deltaP `22.9834` edge `0.6025` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.942` n `117` status `ready` deltaP `31.5497` edge `0.322` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.942` n `117` status `ready` deltaP `31.5497` edge `0.322` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.126` n `117` status `ready` deltaP `21.1005` edge `0.9233` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.126` n `117` status `ready` deltaP `21.1005` edge `0.9233` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.9387` n `117` status `ready` deltaP `26.1335` edge `0.3232` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9387` n `117` status `ready` deltaP `26.1335` edge `0.3232` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.7454` n `241` status `ready` deltaP `15.6386` edge `0.2906` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.0116` n `117` status `ready` deltaP `10.804` edge `0.0165` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.0116` n `117` status `ready` deltaP `10.804` edge `0.0165` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `1.0017` n `117` status `ready` deltaP `4.097` edge `0.0914` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0017` n `117` status `ready` deltaP `4.097` edge `0.0914` maxDD `-1.1521`
- `market_context_high->equity_24h` score `0.9471` n `241` status `ready` deltaP `8.8542` edge `0.0199` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.4965` n `117` status `ready` deltaP `14.3726` edge `-0.0013` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.4965` n `117` status `ready` deltaP `14.3726` edge `-0.0013` maxDD `-2.2516`
- `risk_on_high->crypto_major_1h` score `0.3584` n `117` status `ready` deltaP `4.6331` edge `0.0717` maxDD `-3.1509`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
