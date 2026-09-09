# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T13:22:29.750605+00:00`
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

- `risk_on_high->crypto_alt_24h` score `8.4995` n `117` status `ready` deltaP `20.7265` edge `0.5931` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.4995` n `117` status `ready` deltaP `20.7265` edge `0.5931` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.5032` n `117` status `ready` deltaP `31.8545` edge `0.2834` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5032` n `117` status `ready` deltaP `31.8545` edge `0.2834` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.0659` n `117` status `ready` deltaP `17.1074` edge `0.814` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.0659` n `117` status `ready` deltaP `17.1074` edge `0.814` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `3.7038` n `117` status `ready` deltaP `22.3226` edge `0.2457` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.7038` n `117` status `ready` deltaP `22.3226` edge `0.2457` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.4521` n `241` status `ready` deltaP `13.3817` edge `0.2812` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.9376` n `117` status `ready` deltaP `20.6998` edge `0.0277` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.9376` n `117` status `ready` deltaP `20.6998` edge `0.0277` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.2162` n `241` status `ready` deltaP `15.795` edge `0.0354` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.7883` n `117` status `ready` deltaP `3.1988` edge `0.0796` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.7883` n `117` status `ready` deltaP `3.1988` edge `0.0796` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6108` n `117` status `ready` deltaP `19.7383` edge `0.0623` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.6108` n `117` status `ready` deltaP `19.7383` edge `0.0623` maxDD `-0.9131`
- `risk_on_high->metal_1h` score `0.2225` n `117` status `ready` deltaP `8.9309` edge `0.002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.2225` n `117` status `ready` deltaP `8.9309` edge `0.002` maxDD `-0.3081`
- `risk_on_high->equity_1h` score `0.216` n `117` status `ready` deltaP `12.5762` edge `-0.0127` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.216` n `117` status `ready` deltaP `12.5762` edge `-0.0127` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
