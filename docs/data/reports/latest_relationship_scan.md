# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T05:52:27.784428+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9810`

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

- `market_context_high->crypto_alt_4h` score `6.7331` n `111` status `ready` deltaP `17.8313` edge `0.5871` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.2573` n `111` status `ready` deltaP `21.6972` edge `0.5327` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.6918` n `52` status `ready` deltaP `20.6379` edge `0.3815` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.6918` n `52` status `ready` deltaP `20.6379` edge `0.3815` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3278` n `48` status `ready` deltaP `30.087` edge `0.2434` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3278` n `48` status `ready` deltaP `30.087` edge `0.2434` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.8149` n `52` status `ready` deltaP `35.7997` edge `0.4639` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.8149` n `52` status `ready` deltaP `35.7997` edge `0.4639` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `3.181` n `111` status `ready` deltaP `-3.5226` edge `0.3532` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.8707` n `117` status `ready` deltaP `13.5665` edge `0.1722` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.5019` n `117` status `ready` deltaP `7.7576` edge `0.154` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.1786` n `111` status `ready` deltaP `10.208` edge `0.0216` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1802` n `54` status `ready` deltaP `3.1992` edge `0.0278` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1802` n `54` status `ready` deltaP `3.1992` edge `0.0278` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3323` n `117` status `ready` deltaP `1.2474` edge `0.002` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.5173` n `54` status `ready` deltaP `3.3101` edge `0.0142` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5173` n `54` status `ready` deltaP `3.3101` edge `0.0142` maxDD `-5.8734`
- `market_context_high->index_1h` score `-0.5336` n `117` status `ready` deltaP `1.2243` edge `-0.0018` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5794` n `117` status `ready` deltaP `5.1692` edge `0.0042` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.591` n `54` status `ready` deltaP `-0.2439` edge `-0.001` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
