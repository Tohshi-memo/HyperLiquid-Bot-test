# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T15:22:31.144617+00:00`
- Price records: `672`
- Market context records: `7786`
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

- `market_context_high->equity_24h` score `7.5455` n `132` status `ready` deltaP `28.1068` edge `0.5756` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.5209` n `133` status `ready` deltaP `14.3131` edge `0.2404` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.019` n `133` status `ready` deltaP `13.0082` edge `0.0423` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.9635` n `133` status `ready` deltaP `13.8891` edge `0.1595` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.9305` n `133` status `ready` deltaP `3.1926` edge `0.2893` maxDD `-6.9701`
- `market_context_high->fx_24h` score `0.7824` n `132` status `ready` deltaP `24.8364` edge `0.0435` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.7675` n `133` status `ready` deltaP `8.352` edge `0.12` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.6662` n `133` status `ready` deltaP `7.8958` edge `0.0888` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3314` n `133` status `ready` deltaP `8.194` edge `0.016` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.2377` n `133` status `ready` deltaP `6.775` edge `0.034` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.1952` n `133` status `ready` deltaP `4.428` edge `0.03` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0475` n `133` status `ready` deltaP `4.7461` edge `0.0103` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1727` n `133` status `ready` deltaP `11.323` edge `0.0482` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3618` n `133` status `ready` deltaP `1.2746` edge `0.0001` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.5724` n `132` status `ready` deltaP `10.9123` edge `0.0379` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9369` n `133` status `ready` deltaP `0.5189` edge `0.0188` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.335` n `133` status `ready` deltaP `-1.5624` edge `0.0021` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5293` n `133` status `ready` deltaP `0.5283` edge `0.0745` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.7266` n `132` status `ready` deltaP `-10.4398` edge `0.0585` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.4341` n `133` status `ready` deltaP `14.6643` edge `0.1197` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
