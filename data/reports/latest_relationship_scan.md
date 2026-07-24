# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T22:39:56.879643+00:00`
- Price records: `672`
- Market context records: `7819`
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

- `market_context_high->equity_24h` score `8.955` n `132` status `ready` deltaP `28.5507` edge `0.6901` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4512` n `133` status `ready` deltaP `13.7111` edge `0.2386` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.2738` n `133` status `ready` deltaP `4.8746` edge `0.3221` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.1816` n `133` status `ready` deltaP `14.6513` edge `0.1726` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1424` n `133` status `ready` deltaP `13.7567` edge `0.0476` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8249` n `132` status `ready` deltaP `25.2187` edge `0.0464` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.8192` n `133` status `ready` deltaP `8.352` edge `0.1243` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.7274` n `133` status `ready` deltaP `7.8958` edge `0.0939` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.5064` n `133` status `ready` deltaP `9.0685` edge `0.0411` maxDD `-1.0817`
- `market_context_high->commodity_24h` score `0.3682` n `132` status `ready` deltaP `15.9052` edge `0.083` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.3518` n `133` status `ready` deltaP `8.3441` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2779` n `133` status `ready` deltaP `5.1765` edge `0.0319` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0257` n `133` status `ready` deltaP `5.3467` edge `0.0124` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0983` n `133` status `ready` deltaP `12.3934` edge `0.0506` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3714` n `133` status `ready` deltaP `1.1245` edge `0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9022` n `133` status `ready` deltaP `0.8183` edge `0.0197` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.323` n `133` status `ready` deltaP `-1.2565` edge `0.0016` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4431` n `133` status `ready` deltaP `1.2905` edge `0.0766` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.4828` n `132` status `ready` deltaP `-8.2701` edge `0.0753` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.2007` n `133` status `ready` deltaP `14.7431` edge `0.1491` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
