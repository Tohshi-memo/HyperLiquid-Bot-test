# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T09:52:29.032504+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10224`

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

- `risk_on_high->crypto_alt_24h` score `7.7639` n `117` status `ready` deltaP `19.5112` edge `0.5399` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `7.7639` n `117` status `ready` deltaP `19.5112` edge `0.5399` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.1382` n `117` status `ready` deltaP `29.8728` edge `0.2662` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.1382` n `117` status `ready` deltaP `29.8728` edge `0.2662` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `3.8662` n `117` status `ready` deltaP `17.1074` edge `0.7884` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `3.8662` n `117` status `ready` deltaP `17.1074` edge `0.7884` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `3.2729` n `117` status `ready` deltaP `20.3409` edge `0.223` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.2729` n `117` status `ready` deltaP `20.3409` edge `0.223` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `2.7165` n `241` status `ready` deltaP `12.1664` edge `0.228` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.6719` n `117` status `ready` deltaP `18.4428` edge `0.0206` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.6719` n `117` status `ready` deltaP `18.4428` edge `0.0206` maxDD `-0.0051`
- `market_context_high->index_24h` score `0.9504` n `241` status `ready` deltaP `13.538` edge `0.0283` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.7403` n `117` status `ready` deltaP `3.0491` edge `0.0766` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.7403` n `117` status `ready` deltaP `3.0491` edge `0.0766` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.3731` n `117` status `ready` deltaP `18.0022` edge `0.0434` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.3731` n `117` status `ready` deltaP `18.0022` edge `0.0434` maxDD `-0.9131`
- `risk_on_high->metal_1h` score `0.1415` n `117` status `ready` deltaP `7.883` edge `-0.0014` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1415` n `117` status `ready` deltaP `7.883` edge `-0.0014` maxDD `-0.3081`
- `risk_on_high->index_1h` score `0.1258` n `117` status `ready` deltaP `8.6699` edge `-0.0053` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1258` n `117` status `ready` deltaP `8.6699` edge `-0.0053` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
