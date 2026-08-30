# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T17:37:27.761040+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11654`

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

- `risk_on_high->crypto_alt_24h` score `26.1923` n `31` status `ready` deltaP `52.6042` edge `1.832` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `26.1923` n `31` status `ready` deltaP `52.6042` edge `1.832` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.7487` n `31` status `ready` deltaP `46.3542` edge `1.0867` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `16.7487` n `31` status `ready` deltaP `46.3542` edge `1.0867` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.7416` n `61` status `ready` deltaP `26.1371` edge `0.6804` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.7416` n `61` status `ready` deltaP `26.1371` edge `0.6804` maxDD `-1.0945`
- `risk_on_high->equity_24h` score `7.0009` n `31` status `ready` deltaP `41.1458` edge `0.3091` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.0009` n `31` status `ready` deltaP `41.1458` edge `0.3091` maxDD `0.0`
- `risk_on_high->fx_24h` score `6.4832` n `31` status `ready` deltaP `73.0903` edge `0.053` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.4832` n `31` status `ready` deltaP `73.0903` edge `0.053` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.2458` n `31` status `ready` deltaP `53.4722` edge `0.164` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.2458` n `31` status `ready` deltaP `53.4722` edge `0.164` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.2381` n `149` status `ready` deltaP `21.054` edge `0.4265` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `5.172` n `61` status `ready` deltaP `25.0675` edge `0.2922` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `5.172` n `61` status `ready` deltaP `25.0675` edge `0.2922` maxDD `-0.5985`
- `market_context_high->metal_24h` score `4.5` n `117` status `ready` deltaP `36.3782` edge `0.2344` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `3.9871` n `72` status `ready` deltaP `11.9594` edge `0.2728` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.9871` n `72` status `ready` deltaP `11.9594` edge `0.2728` maxDD `-0.2885`
- `risk_on_high->crypto_alt_4h` score `3.9021` n `61` status `ready` deltaP `13.6295` edge `0.2826` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `3.9021` n `61` status `ready` deltaP `13.6295` edge `0.2826` maxDD `-1.5298`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
