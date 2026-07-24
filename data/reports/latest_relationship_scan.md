# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T22:22:25.292400+00:00`
- Price records: `672`
- Market context records: `7817`
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

- `market_context_high->equity_24h` score `8.8938` n `132` status `ready` deltaP `28.5507` edge `0.685` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4373` n `133` status `ready` deltaP `13.5378` edge `0.2386` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.2619` n `133` status `ready` deltaP `4.7217` edge `0.3216` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.1864` n `133` status `ready` deltaP `14.6513` edge `0.173` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1604` n `133` status `ready` deltaP `13.9064` edge `0.0481` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8234` n `132` status `ready` deltaP `25.2187` edge `0.0462` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.8192` n `133` status `ready` deltaP `8.352` edge `0.1243` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.7274` n `133` status `ready` deltaP `7.8958` edge `0.0939` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.5247` n `133` status `ready` deltaP `9.2214` edge `0.0416` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3518` n `133` status `ready` deltaP `8.3441` edge `0.0167` maxDD `-0.7743`
- `market_context_high->commodity_24h` score `0.3411` n `132` status `ready` deltaP `15.7312` edge `0.0819` maxDD `-7.0012`
- `market_context_high->crypto_alt_1h` score `0.2815` n `133` status `ready` deltaP `5.1765` edge `0.0322` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0113` n `133` status `ready` deltaP `5.1966` edge `0.0122` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.107` n `133` status `ready` deltaP `12.2405` edge `0.0505` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3594` n `133` status `ready` deltaP `1.2746` edge `0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.9022` n `133` status `ready` deltaP `0.8183` edge `0.0197` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3309` n `133` status `ready` deltaP `-1.4095` edge `0.0016` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4565` n `133` status `ready` deltaP `1.1381` edge `0.0765` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.498` n `132` status `ready` deltaP `-8.444` edge `0.0745` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.2108` n `133` status `ready` deltaP `14.7431` edge `0.1478` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
