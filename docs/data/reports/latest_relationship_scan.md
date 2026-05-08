# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T15:37:12.685970+00:00`
- Price records: `658`
- Market context records: `769`
- Flow alert records: `2168`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `13.4422` n `147` status `ready` deltaP `32.0818` edge `0.9397` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6737` n `147` status `ready` deltaP `7.3268` edge `0.5121` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.0677` n `33` status `ready` deltaP `13.1221` edge `0.0245` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0677` n `33` status `ready` deltaP `13.1221` edge `0.0245` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5681` n `147` status `ready` deltaP `3.1124` edge `0.2261` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.2868` n `33` status `ready` deltaP `8.7133` edge `0.0022` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2868` n `33` status `ready` deltaP `8.7133` edge `0.0022` maxDD `-0.2147`
- `risk_on_high->commodity_1h` score `0.2562` n `33` status `ready` deltaP `7.7763` edge `0.0186` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.2562` n `33` status `ready` deltaP `7.7763` edge `0.0186` maxDD `-0.6739`
- `market_context_high->equity_24h` score `-0.0133` n `147` status `ready` deltaP `1.6751` edge `0.2482` maxDD `-10.5047`
- `risk_on_high->crypto_major_1h` score `-0.0305` n `33` status `ready` deltaP `5.1293` edge `-0.0077` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.0305` n `33` status `ready` deltaP `5.1293` edge `-0.0077` maxDD `-1.0995`
- `risk_on_high->index_1h` score `-0.1938` n `33` status `ready` deltaP `-0.1631` edge `0.0133` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.1938` n `33` status `ready` deltaP `-0.1631` edge `0.0133` maxDD `-0.2687`
- `market_context_high->commodity_1h` score `-0.4444` n `184` status `ready` deltaP `2.6873` edge `0.0425` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.4556` n `172` status `ready` deltaP `3.2605` edge `0.007` maxDD `-1.6381`
- `market_context_high->equity_1h` score `-0.4987` n `184` status `ready` deltaP `0.5101` edge `0.0137` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.5299` n `184` status `ready` deltaP `1.1873` edge `0.0095` maxDD `-2.8282`
- `market_context_high->fx_1h` score `-0.5442` n `184` status `ready` deltaP `1.5986` edge `0.0018` maxDD `-0.291`
- `risk_on_high->crypto_alt_1h` score `-0.6326` n `33` status `ready` deltaP `1.8905` edge `-0.0278` maxDD `-1.0015`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
