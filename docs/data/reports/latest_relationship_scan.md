# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T18:07:43.399377+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8092`

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

- `market_context_high->unknown_4h` score `95.8537` n `152` status `ready` deltaP `0.5948` edge `8.0174` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `28.2481` n `153` status `ready` deltaP `1.3248` edge `2.3941` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.4169` n `112` status `ready` deltaP `25.8418` edge `0.1438` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.2171` n `153` status `ready` deltaP `7.666` edge `0.0028` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1393` n `152` status `ready` deltaP `9.4879` edge `0.0082` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0051` n `112` status `ready` deltaP `16.3051` edge `0.0145` maxDD `-4.5747`
- `market_context_high->fx_24h` score `-0.1348` n `112` status `ready` deltaP `16.972` edge `0.0268` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1501` n `153` status `ready` deltaP `8.031` edge `0.0064` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.2774` n `153` status `ready` deltaP `2.1526` edge `0.0126` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5852` n `153` status `ready` deltaP `0.0127` edge `-0.0014` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.6914` n `152` status `ready` deltaP `4.3619` edge `0.0362` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9293` n `153` status `ready` deltaP `3.7846` edge `0.0137` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9726` n `152` status `ready` deltaP `7.0826` edge `-0.0009` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8066` n `153` status `ready` deltaP `1.6046` edge `-0.0147` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0279` n `153` status `ready` deltaP `-0.8747` edge `-0.0057` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4283` n `152` status `ready` deltaP `-6.5469` edge `-0.0244` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.3926` n `112` status `ready` deltaP `-2.2716` edge `-0.0623` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.7034` n `152` status `ready` deltaP `-1.3378` edge `-0.0901` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.0668` n `112` status `ready` deltaP `-3.3904` edge `-0.2119` maxDD `-35.4638`
- `market_context_high->commodity_24h` score `-6.3342` n `112` status `ready` deltaP `-17.0772` edge `-0.1393` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
