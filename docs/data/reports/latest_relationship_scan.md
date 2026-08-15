# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T12:22:31.844207+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.4799` n `128` status `ready` deltaP `-24.8091` edge `11.9133` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.6409` n `32` status `ready` deltaP `-38.0903` edge `4.6419` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6409` n `32` status `ready` deltaP `-38.0903` edge `4.6419` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.6346` n `36` status `ready` deltaP `24.7544` edge `0.9258` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.7003` n `36` status `ready` deltaP `40.2439` edge `0.3734` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.4033` n `128` status `ready` deltaP `31.2784` edge `0.2475` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.9794` n `32` status `ready` deltaP `33.6222` edge `0.1908` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.9794` n `32` status `ready` deltaP `33.6222` edge `0.1908` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2503` n `32` status `ready` deltaP `28.2008` edge `0.4725` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2503` n `32` status `ready` deltaP `28.2008` edge `0.4725` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.5094` n `36` status `ready` deltaP `28.9428` edge `0.0995` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9829` n `32` status `ready` deltaP `21.7226` edge `0.122` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9829` n `32` status `ready` deltaP `21.7226` edge `0.122` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0351` n `128` status `ready` deltaP `20.1601` edge `0.0823` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9376` n `36` status `ready` deltaP `22.3577` edge `0.0256` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7394` n `36` status `ready` deltaP `8.4332` edge `0.1206` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2958` n `32` status `ready` deltaP `13.8099` edge `0.0392` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2958` n `32` status `ready` deltaP `13.8099` edge `0.0392` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6593` n `128` status `ready` deltaP `9.1224` edge `0.0238` maxDD `-0.3742`
- `risk_on_high->equity_24h` score `0.5663` n `32` status `ready` deltaP `13.2961` edge `0.1619` maxDD `-11.2348`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
