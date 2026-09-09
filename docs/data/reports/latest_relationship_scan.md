# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T19:52:26.578459+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10148`

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

- `risk_on_high->crypto_alt_24h` score `11.2807` n `117` status `ready` deltaP `24.5459` edge `0.7994` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `11.2807` n `117` status `ready` deltaP `24.5459` edge `0.7994` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `6.2332` n `241` status `ready` deltaP `17.2011` edge `0.4875` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `5.9531` n `117` status `ready` deltaP `33.6838` edge `0.3087` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.9531` n `117` status `ready` deltaP `33.6838` edge `0.3087` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.882` n `117` status `ready` deltaP `20.2324` edge `1.026` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.882` n `117` status `ready` deltaP `20.2324` edge `1.026` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.1416` n `117` status `ready` deltaP `23.9994` edge `0.271` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.1416` n `117` status `ready` deltaP `23.9994` edge `0.271` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4546` n `117` status `ready` deltaP `24.8665` edge `0.043` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4546` n `117` status `ready` deltaP `24.8665` edge `0.043` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.7331` n `241` status `ready` deltaP `19.9617` edge `0.0507` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.2523` n `241` status `ready` deltaP `8.3333` edge `0.0488` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0089` n `117` status `ready` deltaP `4.2467` edge `0.091` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0089` n `117` status `ready` deltaP `4.2467` edge `0.091` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7598` n `117` status `ready` deltaP `19.7383` edge `0.0814` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7598` n `117` status `ready` deltaP `19.7383` edge `0.0814` maxDD `-0.9131`
- `risk_on_high->equity_24h` score `0.5671` n `117` status `ready` deltaP `8.3333` edge `-0.0083` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.5671` n `117` status `ready` deltaP `8.3333` edge `-0.0083` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.367` n `117` status `ready` deltaP `13.7738` edge `-0.0081` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
