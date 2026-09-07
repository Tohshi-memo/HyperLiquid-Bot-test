# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T16:37:25.524745+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10441`

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

- `risk_on_high->unknown_24h` score `322.394` n `98` status `ready` deltaP `23.7847` edge `26.7076` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `322.394` n `98` status `ready` deltaP `23.7847` edge `26.7076` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.669` n `98` status `ready` deltaP `35.0199` edge `1.5037` maxDD `-5.18`
- `risk_on_and_context->crypto_major_24h` score `19.669` n `98` status `ready` deltaP `35.0199` edge `1.5037` maxDD `-5.18`
- `risk_on_high->crypto_alt_24h` score `14.04` n `98` status `ready` deltaP `31.4449` edge `0.9665` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `14.04` n `98` status `ready` deltaP `31.4449` edge `0.9665` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `7.9184` n `210` status `ready` deltaP `24.3701` edge `0.5549` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.5302` n `117` status `ready` deltaP `29.568` edge `0.3009` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5302` n `117` status `ready` deltaP `29.568` edge `0.3009` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.8557` n `117` status `ready` deltaP `25.9811` edge `0.3173` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8557` n `117` status `ready` deltaP `25.9811` edge `0.3173` maxDD `-3.8693`
- `market_context_high->equity_24h` score `4.5711` n `210` status `ready` deltaP `17.0139` edge `0.2675` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.8655` n `98` status `ready` deltaP `17.0139` edge `0.2087` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.8655` n `98` status `ready` deltaP `17.0139` edge `0.2087` maxDD `0.0`
- `risk_on_high->index_24h` score `2.1178` n `98` status `ready` deltaP `18.4666` edge `0.0576` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.1178` n `98` status `ready` deltaP `18.4666` edge `0.0576` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.3575` n `210` status `ready` deltaP `12.9564` edge `0.0661` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.01` n `117` status `ready` deltaP `4.6958` edge `0.0881` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.01` n `117` status `ready` deltaP `4.6958` edge `0.0881` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6797` n `98` status `ready` deltaP `16.6525` edge `0.0917` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
