# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T19:43:14.481377+00:00`
- Price records: `672`
- Market context records: `3615`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13162`

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

- `risk_on_high->crypto_major_24h` score `43.5079` n `32` status `ready` deltaP `47.5694` edge `3.3128` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `43.5079` n `32` status `ready` deltaP `47.5694` edge `3.3128` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `40.5422` n `32` status `ready` deltaP `49.6528` edge `3.0475` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `40.5422` n `32` status `ready` deltaP `49.6528` edge `3.0475` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `36.3624` n `32` status `ready` deltaP `46.7014` edge `2.734` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `36.3624` n `32` status `ready` deltaP `46.7014` edge `2.734` maxDD `-0.8779`
- `risk_on_high->index_24h` score `23.5886` n `32` status `ready` deltaP `49.6528` edge `1.6347` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.5886` n `32` status `ready` deltaP `49.6528` edge `1.6347` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.4414` n `32` status `ready` deltaP `35.2431` edge `1.1613` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.4414` n `32` status `ready` deltaP `35.2431` edge `1.1613` maxDD `-0.7574`
- `market_context_high->equity_24h` score `14.8122` n `158` status `ready` deltaP `26.2351` edge `1.7007` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.8545` n `32` status `ready` deltaP `23.7805` edge `1.0249` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.8545` n `32` status `ready` deltaP `23.7805` edge `1.0249` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.2387` n `158` status `ready` deltaP `34.4629` edge `1.0118` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `8.1853` n `158` status `ready` deltaP `13.3526` edge `1.3662` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.2113` n `158` status `ready` deltaP `29.1513` edge `1.056` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.5077` n `32` status `ready` deltaP `4.3445` edge `0.5311` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.5077` n `32` status `ready` deltaP `4.3445` edge `0.5311` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.3439` n `32` status `ready` deltaP `13.6433` edge `0.4512` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.3439` n `32` status `ready` deltaP `13.6433` edge `0.4512` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
