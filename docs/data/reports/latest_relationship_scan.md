# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T14:37:32.323055+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10152`

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

- `risk_on_high->crypto_alt_24h` score `8.655` n `117` status `ready` deltaP `20.9001` edge `0.6049` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.655` n `117` status `ready` deltaP `20.9001` edge `0.6049` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.491` n `117` status `ready` deltaP `31.7021` edge `0.2834` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.491` n `117` status `ready` deltaP `31.7021` edge `0.2834` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.1384` n `117` status `ready` deltaP `17.1074` edge `0.8233` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.1384` n `117` status `ready` deltaP `17.1074` edge `0.8233` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `3.6892` n `117` status `ready` deltaP `22.1701` edge `0.2455` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.6892` n `117` status `ready` deltaP `22.1701` edge `0.2455` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.6076` n `241` status `ready` deltaP `13.5553` edge `0.293` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.9937` n `117` status `ready` deltaP `21.2206` edge `0.0289` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.9937` n `117` status `ready` deltaP `21.2206` edge `0.0289` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.2722` n `241` status `ready` deltaP `16.3158` edge `0.0366` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.8015` n `117` status `ready` deltaP `3.1988` edge `0.0807` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8015` n `117` status `ready` deltaP `3.1988` edge `0.0807` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6163` n `117` status `ready` deltaP `19.7383` edge `0.063` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.6163` n `117` status `ready` deltaP `19.7383` edge `0.063` maxDD `-0.9131`
- `risk_on_high->index_1h` score `0.1858` n `117` status `ready` deltaP `9.5681` edge `-0.0036` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1858` n `117` status `ready` deltaP `9.5681` edge `-0.0036` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `0.1742` n `117` status `ready` deltaP `8.3321` edge `-0.0002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1742` n `117` status `ready` deltaP `8.3321` edge `-0.0002` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
