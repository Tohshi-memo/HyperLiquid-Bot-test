# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T10:52:29.320135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11210`

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

- `news_risk_high->unknown_4h` score `396.8218` n `78` status `ready` deltaP `-22.303` edge `33.3065` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `22.0809` n `78` status `ready` deltaP `46.0337` edge `1.5723` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `21.8654` n `78` status `ready` deltaP `19.0972` edge `1.6948` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.8493` n `78` status `ready` deltaP `36.0844` edge `1.3106` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.211` n `78` status `ready` deltaP `48.4642` edge `1.1225` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6871` n `78` status `ready` deltaP `61.9391` edge `0.3286` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5885` n `78` status `ready` deltaP `39.0091` edge `0.3344` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9069` n `52` status `ready` deltaP `37.3264` edge `0.2434` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9069` n `52` status `ready` deltaP `37.3264` edge `0.2434` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6099` n `137` status `ready` deltaP `30.0271` edge `0.2365` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.6624` n `52` status `ready` deltaP `42.695` edge `0.0248` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.6624` n `52` status `ready` deltaP `42.695` edge `0.0248` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.2654` n `137` status `ready` deltaP `39.5086` edge `0.0303` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.8538` n `52` status `ready` deltaP `24.3082` edge `0.0274` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8538` n `52` status `ready` deltaP `24.3082` edge `0.0274` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7535` n `149` status `ready` deltaP `20.8105` edge `0.0492` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.803` n `149` status `ready` deltaP `13.0672` edge `0.0175` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7517` n `78` status `ready` deltaP `18.0308` edge `0.039` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2385` n `52` status `ready` deltaP `8.0608` edge `0.0074` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2385` n `52` status `ready` deltaP `8.0608` edge `0.0074` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
