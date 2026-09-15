# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T10:37:32.040950+00:00`
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

- `news_risk_high->unknown_4h` score `396.823` n `78` status `ready` deltaP `-22.303` edge `33.3066` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `22.0653` n `78` status `ready` deltaP `46.0337` edge `1.571` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `21.8227` n `78` status `ready` deltaP `18.9236` edge `1.6924` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.8114` n `78` status `ready` deltaP `35.9108` edge `1.3086` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.2038` n `78` status `ready` deltaP `48.4642` edge `1.1219` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7046` n `78` status `ready` deltaP `62.1127` edge `0.3289` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.606` n `78` status `ready` deltaP `39.1827` edge `0.3347` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9069` n `52` status `ready` deltaP `37.3264` edge `0.2434` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9069` n `52` status `ready` deltaP `37.3264` edge `0.2434` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6099` n `137` status `ready` deltaP `30.0271` edge `0.2365` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.6811` n `52` status `ready` deltaP `42.8686` edge `0.0252` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.6811` n `52` status `ready` deltaP `42.8686` edge `0.0252` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.2841` n `137` status `ready` deltaP `39.6822` edge `0.0307` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.8574` n `52` status `ready` deltaP `24.3082` edge `0.0277` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8574` n `52` status `ready` deltaP `24.3082` edge `0.0277` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7571` n `149` status `ready` deltaP `20.8105` edge `0.0495` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8006` n `149` status `ready` deltaP `13.0672` edge `0.0173` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7525` n `78` status `ready` deltaP `18.0308` edge `0.0391` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2486` n `52` status `ready` deltaP `8.2105` edge `0.0077` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2486` n `52` status `ready` deltaP `8.2105` edge `0.0077` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
