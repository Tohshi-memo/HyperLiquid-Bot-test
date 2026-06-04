# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T16:52:34.310006+00:00`
- Price records: `672`
- Market context records: `2884`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `8.9085` n `142` status `ready` deltaP `8.2576` edge `1.079` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `5.0304` n `142` status `ready` deltaP `10.2406` edge `0.3974` maxDD `-1.7175`
- `market_context_high->equity_24h` score `4.9421` n `142` status `ready` deltaP `9.6024` edge `0.5482` maxDD `-12.6963`
- `market_context_high->index_24h` score `2.2736` n `142` status `ready` deltaP `11.1062` edge `0.2135` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7184` n `142` status `ready` deltaP `15.5516` edge `0.3489` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.7462` n `142` status `ready` deltaP `6.0331` edge `0.1273` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6763` n `142` status `ready` deltaP `14.9777` edge `0.071` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0189` n `142` status `ready` deltaP `4.4974` edge `0.017` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.0434` n `142` status `ready` deltaP `4.3308` edge `0.0406` maxDD `-3.1801`
- `market_context_high->equity_4h` score `-0.1526` n `142` status `ready` deltaP `4.4014` edge `0.0959` maxDD `-5.7037`
- `market_context_high->commodity_1h` score `-0.5984` n `142` status `ready` deltaP `-0.5819` edge `0.0025` maxDD `-4.3601`
- `market_context_high->crypto_alt_4h` score `-0.6201` n `142` status `ready` deltaP `14.4903` edge `0.2858` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.657` n `142` status `ready` deltaP `4.9465` edge `0.0588` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.6772` n `142` status `ready` deltaP `-2.1843` edge `0.0025` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6816` n `142` status `ready` deltaP `-0.466` edge `0.0003` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.7348` n `142` status `ready` deltaP `-1.7015` edge `0.0334` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.7588` n `142` status `ready` deltaP `4.9739` edge `0.0565` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1088` n `142` status `ready` deltaP `3.8195` edge `0.0244` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2649` n `142` status `ready` deltaP `-4.8201` edge `0.0046` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3699` n `142` status `ready` deltaP `-1.8852` edge `-0.0144` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
