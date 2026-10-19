# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T05:22:28.245019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8894`

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

- `risk_on_high->equity_24h` score `3.6596` n `43` status `ready` deltaP `-16.3276` edge `0.9247` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `3.6596` n `43` status `ready` deltaP `-16.3276` edge `0.9247` maxDD `-28.5375`
- `market_context_high->equity_24h` score `2.8153` n `76` status `ready` deltaP `3.0115` edge `1.1334` maxDD `-55.843`
- `market_context_high->crypto_major_24h` score `1.6682` n `76` status `ready` deltaP `4.8702` edge `0.7911` maxDD `-35.1086`
- `market_context_high->commodity_24h` score `1.2292` n `76` status `ready` deltaP `13.7368` edge `0.096` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.792` n `43` status `ready` deltaP `15.1233` edge `0.023` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.792` n `43` status `ready` deltaP `15.1233` edge `0.023` maxDD `-1.9591`
- `market_context_high->crypto_major_4h` score `0.621` n `77` status `ready` deltaP `5.9787` edge `0.3802` maxDD `-15.2359`
- `risk_on_high->index_1h` score `0.5587` n `43` status `ready` deltaP `11.3696` edge `0.0011` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5587` n `43` status `ready` deltaP `11.3696` edge `0.0011` maxDD `-0.4273`
- `risk_on_high->equity_4h` score `0.3134` n `43` status `ready` deltaP `7.3679` edge `0.1123` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `0.3134` n `43` status `ready` deltaP `7.3679` edge `0.1123` maxDD `-4.824`
- `market_context_high->crypto_major_1h` score `0.3123` n `77` status `ready` deltaP `4.6466` edge `0.0972` maxDD `-3.7178`
- `risk_on_high->fx_4h` score `0.0386` n `43` status `ready` deltaP `3.3035` edge `0.0076` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0386` n `43` status `ready` deltaP `3.3035` edge `0.0076` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2287` n `43` status `ready` deltaP `0.8625` edge `-0.0004` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2287` n `43` status `ready` deltaP `0.8625` edge `-0.0004` maxDD `-0.1065`
- `risk_on_high->index_4h` score `-0.2977` n `43` status `ready` deltaP `7.8586` edge `0.0095` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.2977` n `43` status `ready` deltaP `7.8586` edge `0.0095` maxDD `-0.9359`
- `market_context_high->metal_1h` score `-0.3505` n `77` status `ready` deltaP `-0.2528` edge `0.0075` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
