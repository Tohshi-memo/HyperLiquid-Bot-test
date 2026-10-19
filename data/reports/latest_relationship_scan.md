# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T04:52:28.438082+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8763`

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

- `risk_on_high->equity_24h` score `3.9622` n `43` status `ready` deltaP `-15.9798` edge `0.9476` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `3.9622` n `43` status `ready` deltaP `-15.9798` edge `0.9476` maxDD `-28.5375`
- `market_context_high->equity_24h` score `3.1179` n `76` status `ready` deltaP `3.3593` edge `1.1563` maxDD `-55.843`
- `market_context_high->crypto_major_24h` score `1.7807` n `76` status `ready` deltaP `5.2174` edge `0.8032` maxDD `-35.1086`
- `market_context_high->commodity_24h` score `1.1629` n `76` status `ready` deltaP `13.389` edge `0.0928` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.7992` n `43` status `ready` deltaP `15.1233` edge `0.0236` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7992` n `43` status `ready` deltaP `15.1233` edge `0.0236` maxDD `-1.9591`
- `market_context_high->crypto_major_4h` score `0.6247` n `76` status `ready` deltaP `5.6001` edge `0.3832` maxDD `-15.2359`
- `risk_on_high->index_1h` score `0.5731` n `43` status `ready` deltaP `11.5197` edge `0.0013` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5731` n `43` status `ready` deltaP `11.5197` edge `0.0013` maxDD `-0.4273`
- `risk_on_high->equity_4h` score `0.3931` n `43` status `ready` deltaP `7.6737` edge `0.1169` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `0.3931` n `43` status `ready` deltaP `7.6737` edge `0.1169` maxDD `-4.824`
- `market_context_high->crypto_major_1h` score `0.3357` n `77` status `ready` deltaP `4.946` edge `0.0982` maxDD `-3.7178`
- `risk_on_high->fx_4h` score `0.0386` n `43` status `ready` deltaP `3.3035` edge `0.0076` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0386` n `43` status `ready` deltaP `3.3035` edge `0.0076` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2372` n `43` status `ready` deltaP `0.7123` edge `-0.0005` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2372` n `43` status `ready` deltaP `0.7123` edge `-0.0005` maxDD `-0.1065`
- `risk_on_high->index_4h` score `-0.2636` n `43` status `ready` deltaP `8.1644` edge `0.0103` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.2636` n `43` status `ready` deltaP `8.1644` edge `0.0103` maxDD `-0.9359`
- `market_context_high->metal_1h` score `-0.3505` n `77` status `ready` deltaP `-0.2528` edge `0.0075` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
