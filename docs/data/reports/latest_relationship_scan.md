# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T17:22:25.671593+00:00`
- Price records: `672`
- Market context records: `5685`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8784`

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

- `market_context_high->equity_24h` score `1.7896` n `206` status `ready` deltaP `16.0987` edge `0.5497` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9795` n `256` status `ready` deltaP `11.8807` edge `0.2169` maxDD `-12.8252`
- `market_context_high->crypto_alt_4h` score `0.5226` n `256` status `ready` deltaP `8.9653` edge `0.1589` maxDD `-8.6763`
- `market_context_high->equity_4h` score `0.1515` n `256` status `ready` deltaP `5.6689` edge `0.1387` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2729` n `268` status `ready` deltaP `1.716` edge `0.0012` maxDD `-0.4764`
- `market_context_high->crypto_alt_1h` score `-0.4231` n `268` status `ready` deltaP `2.6767` edge `0.0398` maxDD `-4.7655`
- `market_context_high->metal_1h` score `-0.509` n `268` status `ready` deltaP `0.4446` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5871` n `268` status `ready` deltaP `3.4901` edge `0.0285` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6309` n `268` status `ready` deltaP `0.219` edge `0.0045` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6355` n `268` status `ready` deltaP `4.1022` edge `0.0399` maxDD `-6.6163`
- `market_context_high->commodity_1h` score `-0.9449` n `268` status `ready` deltaP `0.2257` edge `-0.0037` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1483` n `256` status `ready` deltaP `4.3826` edge `0.007` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.288` n `256` status `ready` deltaP `-0.8194` edge `0.0075` maxDD `-3.04`
- `market_context_high->fx_24h` score `-1.3266` n `206` status `ready` deltaP `13.4928` edge `0.0465` maxDD `-3.0935`
- `market_context_high->index_24h` score `-2.5611` n `206` status `ready` deltaP `5.6449` edge `0.0371` maxDD `-17.246`
- `market_context_high->metal_4h` score `-2.8575` n `256` status `ready` deltaP `-11.3377` edge `-0.0532` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.814` n `256` status `ready` deltaP `-2.7725` edge `-0.0318` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.8124` n `206` status `ready` deltaP `4.0588` edge `0.0176` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.2684` n `206` status `ready` deltaP `-11.7955` edge `-0.2474` maxDD `-32.7213`
- `market_context_high->commodity_24h` score `-12.0152` n `206` status `ready` deltaP `-9.911` edge `-0.0743` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
