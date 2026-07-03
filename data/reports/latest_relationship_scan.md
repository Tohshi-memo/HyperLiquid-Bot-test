# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T16:07:32.710224+00:00`
- Price records: `672`
- Market context records: `5573`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11396`

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

- `market_context_high->equity_24h` score `4.3765` n `175` status `ready` deltaP `15.12` edge `0.7718` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2419` n `190` status `ready` deltaP `11.1361` edge `0.2585` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `0.9595` n `175` status `ready` deltaP `13.9633` edge `0.4409` maxDD `-29.6555`
- `market_context_high->fx_24h` score `0.7978` n `175` status `ready` deltaP `16.9147` edge `0.0511` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.7392` n `190` status `ready` deltaP `6.5196` edge `0.182` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.656` n `190` status `ready` deltaP `6.5774` edge `0.1749` maxDD `-9.46`
- `market_context_high->index_1h` score `-0.1969` n `202` status `ready` deltaP `3.6951` edge `0.0083` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-0.2604` n `190` status `ready` deltaP `6.2981` edge `0.0097` maxDD `-0.8712`
- `market_context_high->equity_1h` score `-0.275` n `202` status `ready` deltaP `5.5019` edge `0.0411` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.4068` n `202` status `ready` deltaP `1.7727` edge `0.0011` maxDD `-0.4122`
- `market_context_high->metal_1h` score `-0.5173` n `202` status `ready` deltaP `-0.0459` edge `0.0015` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5785` n `202` status `ready` deltaP `0.9664` edge `0.0415` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7231` n `202` status `ready` deltaP `2.533` edge `0.0474` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.3013` n `202` status `ready` deltaP `-3.4194` edge `-0.0091` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.531` n `190` status `ready` deltaP `2.4358` edge `0.0171` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.9866` n `175` status `ready` deltaP `13.3194` edge `0.0552` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0872` n `190` status `ready` deltaP `-13.9746` edge `-0.062` maxDD `-11.9169`
- `market_context_high->commodity_4h` score `-4.5335` n `190` status `ready` deltaP `-8.2109` edge `-0.0555` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.8402` n `175` status `ready` deltaP `-7.5189` edge `-0.2187` maxDD `-32.9061`
- `market_context_high->crypto_alt_24h` score `-8.9973` n `175` status `ready` deltaP `3.996` edge `0.0933` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
