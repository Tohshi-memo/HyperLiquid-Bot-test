# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T19:37:33.858295+00:00`
- Price records: `672`
- Market context records: `7804`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `8.2314` n `132` status `ready` deltaP `28.5507` edge `0.6298` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.3759` n `133` status `ready` deltaP `12.8445` edge `0.2381` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.1721` n `133` status `ready` deltaP `14.5764` edge `0.1723` maxDD `-6.7444`
- `market_context_high->equity_4h` score `1.135` n `133` status `ready` deltaP `4.036` edge `0.3099` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.0861` n `133` status `ready` deltaP `13.3076` edge `0.0459` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8171` n `132` status `ready` deltaP `25.2187` edge `0.0454` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7946` n `133` status `ready` deltaP `8.3463` edge `0.0965` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.7585` n `133` status `ready` deltaP `7.8186` edge `0.1228` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.5511` n `133` status `ready` deltaP `9.1614` edge `0.0442` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3926` n `133` status `ready` deltaP `8.7946` edge `0.0171` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2755` n `133` status `ready` deltaP `5.0268` edge `0.0327` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0341` n `133` status `ready` deltaP `5.3467` edge `0.0131` maxDD `-0.6722`
- `market_context_high->commodity_24h` score `0.0177` n `132` status `ready` deltaP `13.8182` edge `0.0677` maxDD `-7.0012`
- `market_context_high->index_4h` score `-0.1495` n `133` status `ready` deltaP `11.7075` edge `0.0486` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.321` n `133` status `ready` deltaP `1.7251` edge `0.0005` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8674` n `133` status `ready` deltaP `1.2674` edge `0.0196` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3334` n `133` status `ready` deltaP `-1.5014` edge `0.0019` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.6082` n `133` status `ready` deltaP `-0.309` edge `0.0735` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.6233` n `132` status `ready` deltaP `-9.4875` edge `0.0654` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.3021` n `133` status `ready` deltaP `14.7431` edge `0.1361` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
