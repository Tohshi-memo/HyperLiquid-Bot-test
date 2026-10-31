# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T11:22:26.971553+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7317`

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

- `market_context_high->unknown_24h` score `2094.4411` n `118` status `ready` deltaP `-6.5943` edge `174.6237` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `102.2874` n `98` status `ready` deltaP `-5.493` edge `8.5892` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `53.2855` n `118` status `ready` deltaP `1.5373` edge `4.4435` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.6223` n `39` status `ready` deltaP `46.0871` edge `1.1664` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.1745` n `118` status `ready` deltaP `25.9033` edge `0.9509` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.117` n `98` status `ready` deltaP `18.638` edge `0.4408` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.5403` n `118` status `ready` deltaP `41.7402` edge `0.1184` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `0.8756` n `98` status `ready` deltaP `7.7966` edge `0.1039` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.6698` n `118` status `ready` deltaP `17.8948` edge `0.0341` maxDD `-1.4023`
- `market_context_high->metal_1h` score `0.6319` n `118` status `ready` deltaP `14.0592` edge `0.0163` maxDD `-0.3209`
- `market_context_high->equity_1h` score `0.4479` n `118` status `ready` deltaP `5.6835` edge `0.087` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3658` n `118` status `ready` deltaP `8.8729` edge `0.0741` maxDD `-5.2213`
- `market_context_high->equity_4h` score `0.1832` n `118` status `ready` deltaP `3.0849` edge `0.1507` maxDD `-5.1557`
- `market_context_high->commodity_4h` score `0.0141` n `118` status `ready` deltaP `10.9627` edge `0.0506` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.0603` n `118` status `ready` deltaP `4.2855` edge `-0.0009` maxDD `-0.1655`
- `market_context_high->metal_24h` score `-0.0922` n `118` status `ready` deltaP `9.8958` edge `0.1869` maxDD `-10.5088`
- `market_context_high->fx_4h` score `-0.3527` n `118` status `ready` deltaP `2.2556` edge `-0.002` maxDD `-0.3268`
- `market_context_high->commodity_1h` score `-0.4094` n `118` status `ready` deltaP `0.4516` edge `0.0143` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4186` n `118` status `ready` deltaP `2.89` edge `0.0017` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8` n `118` status `ready` deltaP `2.6946` edge `0.057` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
