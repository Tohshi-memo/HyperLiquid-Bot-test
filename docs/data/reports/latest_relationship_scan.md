# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T14:22:30.481716+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8252`

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

- `market_context_high->commodity_24h` score `1.9478` n `76` status `ready` deltaP `18.0846` edge `0.1269` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5449` n `43` status `ready` deltaP `14.1348` edge `0.009` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5449` n `43` status `ready` deltaP `14.1348` edge `0.009` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4393` n `43` status `ready` deltaP `10.0869` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4393` n `43` status `ready` deltaP `10.0869` edge `-0.0003` maxDD `-0.4273`
- `market_context_high->crypto_major_4h` score `0.1407` n `77` status `ready` deltaP `3.3873` edge `0.3359` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `0.097` n `43` status `ready` deltaP `13.4641` edge `-0.0019` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.097` n `43` status `ready` deltaP `13.4641` edge `-0.0019` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.0799` n `43` status `ready` deltaP `2.0025` edge `0.0064` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0799` n `43` status `ready` deltaP `2.0025` edge `0.0064` maxDD `-0.1126`
- `market_context_high->crypto_major_24h` score `-0.0911` n `76` status `ready` deltaP `-1.0326` edge `0.6049` maxDD `-35.1086`
- `market_context_high->crypto_major_1h` score `-0.1276` n `82` status `ready` deltaP `1.884` edge `0.0643` maxDD `-4.1242`
- `risk_on_high->fx_1h` score `-0.2427` n `43` status `ready` deltaP `0.6381` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2427` n `43` status `ready` deltaP `0.6381` edge `-0.0007` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.4292` n `82` status `ready` deltaP `-3.2533` edge `0.0021` maxDD `-0.5013`
- `market_context_high->fx_4h` score `-0.5226` n `77` status `ready` deltaP `-1.1084` edge `0.0041` maxDD `-0.7635`
- `risk_on_high->index_4h` score `-0.5833` n `43` status `ready` deltaP `5.1731` edge `0.0036` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.5833` n `43` status `ready` deltaP `5.1731` edge `0.0036` maxDD `-0.9359`
- `market_context_high->metal_4h` score `-0.5951` n `77` status `ready` deltaP `-0.5029` edge `0.0493` maxDD `-0.7797`
- `market_context_high->fx_1h` score `-0.6406` n `82` status `ready` deltaP `-4.1832` edge `-0.0017` maxDD `-0.537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
