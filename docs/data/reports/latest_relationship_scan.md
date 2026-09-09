# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T11:52:43.645478+00:00`
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

- `risk_on_high->crypto_alt_24h` score `8.2847` n `117` status `ready` deltaP `20.7265` edge `0.5752` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.2847` n `117` status `ready` deltaP `20.7265` edge `0.5752` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.3568` n `117` status `ready` deltaP `30.9399` edge `0.2773` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3568` n `117` status `ready` deltaP `30.9399` edge `0.2773` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.0089` n `117` status `ready` deltaP `17.1074` edge `0.8067` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.0089` n `117` status `ready` deltaP `17.1074` edge `0.8067` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `3.5672` n `117` status `ready` deltaP `21.5604` edge `0.2394` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.5672` n `117` status `ready` deltaP `21.5604` edge `0.2394` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.2373` n `241` status `ready` deltaP `13.3817` edge `0.2633` maxDD `-3.9523`
- `risk_on_high->index_24h` score `1.831` n `117` status `ready` deltaP `19.8317` edge `0.0246` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.831` n `117` status `ready` deltaP `19.8317` edge `0.0246` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.1095` n `241` status `ready` deltaP `14.9269` edge `0.0323` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.8338` n `117` status `ready` deltaP `3.4982` edge `0.0814` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8338` n `117` status `ready` deltaP `3.4982` edge `0.0814` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.5131` n `117` status `ready` deltaP `19.0438` edge `0.0544` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.5131` n `117` status `ready` deltaP `19.0438` edge `0.0544` maxDD `-0.9131`
- `risk_on_high->index_1h` score `0.1842` n `117` status `ready` deltaP `9.5681` edge `-0.0038` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.1842` n `117` status `ready` deltaP `9.5681` edge `-0.0038` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `0.1788` n `117` status `ready` deltaP `8.3321` edge `0.0004` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.1788` n `117` status `ready` deltaP `8.3321` edge `0.0004` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
