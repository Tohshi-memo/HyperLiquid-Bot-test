# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T20:52:28.899410+00:00`
- Price records: `672`
- Market context records: `7810`
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

- `market_context_high->equity_24h` score `8.5146` n `132` status `ready` deltaP `28.5507` edge `0.6534` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4198` n `133` status `ready` deltaP `13.3644` edge `0.2383` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.166` n `133` status `ready` deltaP `3.9571` edge `0.3144` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.1369` n `133` status `ready` deltaP `14.3464` edge `0.1709` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0885` n `133` status `ready` deltaP `13.3076` edge `0.0461` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8195` n `132` status `ready` deltaP `25.2187` edge `0.0457` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.7224` n `133` status `ready` deltaP `7.7423` edge `0.1203` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.719` n `133` status `ready` deltaP `7.7457` edge `0.0942` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.5681` n `133` status `ready` deltaP `9.3743` edge `0.0442` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.365` n `133` status `ready` deltaP `8.4943` edge `0.0168` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2311` n `133` status `ready` deltaP `4.7274` edge `0.031` maxDD `-1.4603`
- `market_context_high->commodity_24h` score `0.1748` n `132` status `ready` deltaP `14.6878` edge `0.075` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.0007` n `133` status `ready` deltaP `5.0464` edge `0.0122` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1482` n `133` status `ready` deltaP `11.6288` edge `0.0493` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.321` n `133` status `ready` deltaP `1.7251` edge `0.0005` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8531` n `133` status `ready` deltaP `1.4171` edge `0.0198` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3381` n `133` status `ready` deltaP `-1.5624` edge `0.0017` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5488` n `133` status `ready` deltaP `0.2235` edge `0.0749` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.5838` n `132` status `ready` deltaP `-9.3136` edge `0.0693` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.2779` n `133` status `ready` deltaP `14.7431` edge `0.1392` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
