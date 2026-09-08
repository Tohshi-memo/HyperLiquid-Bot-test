# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T07:52:31.303515+00:00`
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

- `risk_on_high->crypto_alt_24h` score `8.2583` n `117` status `ready` deltaP `20.7265` edge `0.573` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.2583` n `117` status `ready` deltaP `20.7265` edge `0.573` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.7942` n `117` status `ready` deltaP `31.3972` edge `0.3107` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7942` n `117` status `ready` deltaP `31.3972` edge `0.3107` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.0059` n `117` status `ready` deltaP `21.1005` edge `0.9079` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.0059` n `117` status `ready` deltaP `21.1005` edge `0.9079` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8207` n `117` status `ready` deltaP `25.8287` edge `0.3154` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8207` n `117` status `ready` deltaP `25.8287` edge `0.3154` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.2109` n `241` status `ready` deltaP `13.3817` edge `0.2611` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `0.9502` n `117` status `ready` deltaP `3.9473` edge `0.0881` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9502` n `117` status `ready` deltaP `3.9473` edge `0.0881` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.8092` n `117` status `ready` deltaP `9.7623` edge `0.0066` maxDD `-0.0066`
- `risk_on_and_context->index_24h` score `0.8092` n `117` status `ready` deltaP `9.7623` edge `0.0066` maxDD `-0.0066`
- `risk_on_high->equity_1h` score `0.496` n `117` status `ready` deltaP `14.672` edge `-0.0008` maxDD `-2.4547`
- `risk_on_and_context->equity_1h` score `0.496` n `117` status `ready` deltaP `14.672` edge `-0.0008` maxDD `-2.4547`
- `risk_on_high->crypto_major_1h` score `0.2745` n `117` status `ready` deltaP `4.184` edge `0.0677` maxDD `-3.1509`
- `risk_on_and_context->crypto_major_1h` score `0.2745` n `117` status `ready` deltaP `4.184` edge `0.0677` maxDD `-3.1509`
- `risk_on_high->metal_1h` score `0.262` n `117` status `ready` deltaP `9.6794` edge `0.0025` maxDD `-0.3423`
- `risk_on_and_context->metal_1h` score `0.262` n `117` status `ready` deltaP `9.6794` edge `0.0025` maxDD `-0.3423`
- `risk_on_high->index_1h` score `0.1743` n `117` status `ready` deltaP `9.7178` edge `-0.0039` maxDD `-0.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
