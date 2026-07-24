# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T22:07:27.114999+00:00`
- Price records: `672`
- Market context records: `7816`
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

- `market_context_high->equity_24h` score `8.8314` n `132` status `ready` deltaP `28.5507` edge `0.6798` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4512` n `133` status `ready` deltaP `13.7111` edge `0.2386` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.247` n `133` status `ready` deltaP `4.5688` edge `0.3207` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.184` n `133` status `ready` deltaP `14.6513` edge `0.1728` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1628` n `133` status `ready` deltaP `13.9064` edge `0.0483` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8226` n `132` status `ready` deltaP `25.2187` edge `0.0461` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.812` n `133` status `ready` deltaP `8.352` edge `0.1237` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.7274` n `133` status `ready` deltaP `7.8958` edge `0.0939` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.5417` n `133` status `ready` deltaP `9.3743` edge `0.042` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3518` n `133` status `ready` deltaP `8.3441` edge `0.0167` maxDD `-0.7743`
- `market_context_high->commodity_24h` score `0.314` n `132` status `ready` deltaP `15.5573` edge `0.0808` maxDD `-7.0012`
- `market_context_high->crypto_alt_1h` score `0.2803` n `133` status `ready` deltaP `5.1765` edge `0.0321` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0113` n `133` status `ready` deltaP `5.1966` edge `0.0122` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1165` n `133` status `ready` deltaP `12.0876` edge `0.0503` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3474` n `133` status `ready` deltaP `1.4248` edge `0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8902` n `133` status `ready` deltaP `0.968` edge `0.0197` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3389` n `133` status `ready` deltaP `-1.5624` edge `0.0016` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4711` n `133` status `ready` deltaP `0.9857` edge `0.0763` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.5141` n `132` status `ready` deltaP `-8.6179` edge `0.0736` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.2218` n `133` status `ready` deltaP `14.7431` edge `0.1464` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
