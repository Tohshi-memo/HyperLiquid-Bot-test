# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T09:37:32.331971+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11471`

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

- `news_risk_high->unknown_4h` score `365.9258` n `83` status `ready` deltaP `-21.6629` edge `30.7277` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `24.1743` n `78` status `ready` deltaP `47.7698` edge `1.7351` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.0733` n `78` status `ready` deltaP `39.7303` edge `1.6383` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.2881` n `78` status `ready` deltaP `47.9434` edge `1.1318` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.931` n `78` status `ready` deltaP `55.8627` edge `0.3061` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.7556` n `78` status `ready` deltaP `38.4882` edge `0.3518` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.466` n `52` status `ready` deltaP `35.0694` edge `0.2217` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.466` n `52` status `ready` deltaP `35.0694` edge `0.2217` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.1668` n `149` status `ready` deltaP `28.358` edge `0.2107` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3657` n `52` status `ready` deltaP `31.9311` edge `-0.0115` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3657` n `52` status `ready` deltaP `31.9311` edge `-0.0115` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2308` n `149` status `ready` deltaP `29.1562` edge `0.0131` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0613` n `52` status `ready` deltaP `27.0521` edge `0.0264` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0613` n `52` status `ready` deltaP `27.0521` edge `0.0264` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.961` n `149` status `ready` deltaP `23.5544` edge `0.0482` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8126` n `149` status `ready` deltaP `13.3666` edge `0.0163` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5765` n `83` status `ready` deltaP `15.5469` edge `0.0331` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.5708` n `52` status `ready` deltaP `10.7646` edge `0.1629` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5708` n `52` status `ready` deltaP `10.7646` edge `0.1629` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.1893` n `52` status `ready` deltaP `6.4487` edge `0.008` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
