# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T01:22:25.634876+00:00`
- Price records: `672`
- Market context records: `7830`
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

- `market_context_high->equity_24h` score `9.6222` n `132` status `ready` deltaP `28.5507` edge `0.7457` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3701` n `133` status `ready` deltaP `6.0978` edge `0.3263` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.312` n `133` status `ready` deltaP `12.1513` edge `0.2374` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.241` n `133` status `ready` deltaP `15.1086` edge `0.1745` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0777` n `133` status `ready` deltaP `13.1579` edge `0.0462` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8653` n `133` status `ready` deltaP `8.8093` edge `0.1251` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8296` n `132` status `ready` deltaP `25.2187` edge `0.047` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7598` n `133` status `ready` deltaP `8.1961` edge `0.0946` maxDD `-4.2072`
- `market_context_high->commodity_24h` score `0.6653` n `132` status `ready` deltaP `17.8182` edge `0.095` maxDD `-7.0012`
- `market_context_high->commodity_4h` score `0.4371` n `133` status `ready` deltaP `8.4569` edge `0.0394` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3386` n `133` status `ready` deltaP `8.194` edge `0.0166` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2743` n `133` status `ready` deltaP `5.1765` edge `0.0316` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0401` n `133` status `ready` deltaP `5.4969` edge `0.0126` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.069` n `133` status `ready` deltaP `12.8521` edge `0.0513` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3738` n `133` status `ready` deltaP `1.1245` edge `0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8495` n `133` status `ready` deltaP `1.4171` edge `0.0201` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.3162` n `132` status `ready` deltaP `-6.3571` edge `0.0839` maxDD `-2.1544`
- `market_context_high->fx_4h` score `-1.3825` n `133` status `ready` deltaP `-2.3269` edge `0.0011` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4249` n `133` status `ready` deltaP `1.443` edge `0.0771` maxDD `-1.4368`
- `market_context_high->crypto_alt_24h` score `-2.1141` n `133` status `ready` deltaP `14.7431` edge `0.1602` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
