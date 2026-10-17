# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T13:07:32.800184+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0257` n `54` status `ready` deltaP `38.5017` edge `0.3288` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0257` n `54` status `ready` deltaP `38.5017` edge `0.3288` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.1011` n `152` status `ready` deltaP `19.5523` edge `0.4269` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `3.9943` n `78` status `ready` deltaP `23.6515` edge `0.2815` maxDD `-4.1721`
- `risk_on_and_context->crypto_major_4h` score `3.9943` n `78` status `ready` deltaP `23.6515` edge `0.2815` maxDD `-4.1721`
- `market_context_high->crypto_alt_4h` score `3.7981` n `152` status `ready` deltaP `11.7458` edge `0.4935` maxDD `-12.424`
- `market_context_high->crypto_major_1h` score `0.5581` n `164` status `ready` deltaP `5.0058` edge `0.0937` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2873` n `152` status `ready` deltaP `12.2513` edge `0.0468` maxDD `-1.6961`
- `market_context_high->crypto_alt_1h` score `0.2102` n `164` status `ready` deltaP `6.5247` edge `0.1056` maxDD `-5.8599`
- `risk_on_high->index_1h` score `0.0219` n `90` status `ready` deltaP `5.2553` edge `0.0052` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0219` n `90` status `ready` deltaP `5.2553` edge `0.0052` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.2119` n `164` status `ready` deltaP `6.4748` edge `0.0045` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2434` n `164` status `ready` deltaP `7.1016` edge `0.0084` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.2912` n `90` status `ready` deltaP `0.5705` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2912` n `90` status `ready` deltaP `0.5705` edge `-0.0031` maxDD `-0.376`
- `market_context_high->equity_4h` score `-0.3937` n `152` status `ready` deltaP `13.5804` edge `0.2016` maxDD `-17.4086`
- `market_context_high->equity_1h` score `-0.4071` n `164` status `ready` deltaP `9.3276` edge `0.0366` maxDD `-7.0778`
- `market_context_high->fx_1h` score `-0.409` n `164` status `ready` deltaP `0.1776` edge `-0.0015` maxDD `-0.503`
- `risk_on_high->crypto_alt_4h` score `-0.4482` n `78` status `ready` deltaP `2.5016` edge `0.1803` maxDD `-12.3548`
- `risk_on_and_context->crypto_alt_4h` score `-0.4482` n `78` status `ready` deltaP `2.5016` edge `0.1803` maxDD `-12.3548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
