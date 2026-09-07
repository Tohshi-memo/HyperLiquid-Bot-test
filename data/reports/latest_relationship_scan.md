# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T15:22:49.288891+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10204`

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

- `risk_on_high->unknown_24h` score `375.1931` n `94` status `ready` deltaP `24.4792` edge `31.1029` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `375.1931` n `94` status `ready` deltaP `24.4792` edge `31.1029` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.1027` n `94` status `ready` deltaP `38.6673` edge `1.6358` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.1027` n `94` status `ready` deltaP `38.6673` edge `1.6358` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.0842` n `94` status `ready` deltaP `32.1181` edge `1.0429` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.0842` n `94` status `ready` deltaP `32.1181` edge `1.0429` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.3273` n `205` status `ready` deltaP `24.801` edge `0.5861` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.3385` n `117` status `ready` deltaP `28.8058` edge `0.29` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3385` n `117` status `ready` deltaP `28.8058` edge `0.29` maxDD `-1.9733`
- `market_context_high->equity_24h` score `4.8986` n `205` status `ready` deltaP `17.8819` edge `0.289` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.6255` n `117` status `ready` deltaP `25.2189` edge `0.3032` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.6255` n `117` status `ready` deltaP `25.2189` edge `0.3032` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `4.2482` n `94` status `ready` deltaP `17.8819` edge `0.2348` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.2482` n `94` status `ready` deltaP `17.8819` edge `0.2348` maxDD `0.0`
- `risk_on_high->index_24h` score `2.2236` n `94` status `ready` deltaP `19.2043` edge `0.0615` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.2236` n `94` status `ready` deltaP `19.2043` edge `0.0615` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.4474` n `205` status `ready` deltaP `13.6153` edge `0.0692` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.8745` n `117` status `ready` deltaP `4.097` edge `0.0808` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8745` n `117` status `ready` deltaP `4.097` edge `0.0808` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.7729` n `94` status `ready` deltaP `17.0213` edge `0.1012` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
