# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T08:52:28.335783+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8646`

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

- `market_context_high->commodity_24h` score `1.6687` n `76` status `ready` deltaP `16.1716` edge `0.1164` maxDD `-1.8119`
- `risk_on_high->equity_24h` score `1.6588` n `43` status `ready` deltaP `-18.7624` edge `0.7742` maxDD `-28.5375`
- `risk_on_and_context->equity_24h` score `1.6588` n `43` status `ready` deltaP `-18.7624` edge `0.7742` maxDD `-28.5375`
- `market_context_high->crypto_major_24h` score `0.8984` n `76` status `ready` deltaP `2.4397` edge `0.7086` maxDD `-35.1086`
- `market_context_high->equity_24h` score `0.8145` n `76` status `ready` deltaP `0.5767` edge `0.9829` maxDD `-55.843`
- `risk_on_high->equity_1h` score `0.7284` n `43` status `ready` deltaP `14.9732` edge `0.0187` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.7284` n `43` status `ready` deltaP `14.9732` edge `0.0187` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.5407` n `43` status `ready` deltaP `11.2194` edge `0.0006` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.5407` n `43` status `ready` deltaP `11.2194` edge `0.0006` maxDD `-0.4273`
- `market_context_high->crypto_major_4h` score `0.3549` n `77` status `ready` deltaP `3.997` edge `0.3593` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.2546` n `77` status `ready` deltaP `4.0478` edge `0.0938` maxDD `-3.7178`
- `risk_on_high->fx_4h` score `0.0129` n `43` status `ready` deltaP `2.9977` edge `0.0075` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0129` n `43` status `ready` deltaP `2.9977` edge `0.0075` maxDD `-0.1126`
- `risk_on_high->equity_4h` score `-0.0566` n `43` status `ready` deltaP `5.533` edge `0.0937` maxDD `-4.824`
- `risk_on_and_context->equity_4h` score `-0.0566` n `43` status `ready` deltaP `5.533` edge `0.0937` maxDD `-4.824`
- `risk_on_high->commodity_24h` score `-0.182` n `43` status `ready` deltaP `11.5511` edge `-0.0124` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.182` n `43` status `ready` deltaP `11.5511` edge `-0.0124` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `-0.2294` n `43` status `ready` deltaP `0.8625` edge `-0.0005` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2294` n `43` status `ready` deltaP `0.8625` edge `-0.0005` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3374` n `77` status `ready` deltaP `-0.1031` edge `0.0076` maxDD `-0.4687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
