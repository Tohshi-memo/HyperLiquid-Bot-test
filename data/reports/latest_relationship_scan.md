# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T12:37:23.394205+00:00`
- Price records: `672`
- Market context records: `2457`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `20.8854` n `38` status `ready` deltaP `45.6323` edge `1.4951` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `20.3708` n `38` status `ready` deltaP `55.3545` edge `1.3725` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `16.5639` n `38` status `ready` deltaP `29.4865` edge `1.2152` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.1181` n `38` status `ready` deltaP `22.4964` edge `0.8346` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.4325` n `38` status `ready` deltaP `24.6253` edge `0.4778` maxDD `-1.4744`
- `news_risk_high->index_24h` score `7.057` n `38` status `ready` deltaP `19.3348` edge `0.4844` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.8083` n `110` status `ready` deltaP `21.8024` edge `0.3715` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.1916` n `133` status `ready` deltaP `19.3047` edge `0.4016` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.1268` n `133` status `ready` deltaP `20.5346` edge `0.4749` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6668` n `38` status `ready` deltaP `38.0299` edge `0.0705` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.101` n `38` status `ready` deltaP `26.2035` edge `0.29` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.436` n `110` status `ready` deltaP `11.6351` edge `0.624` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `1.9944` n `38` status `ready` deltaP `25.2889` edge `0.016` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `1.8305` n `38` status `ready` deltaP `22.1872` edge `0.0478` maxDD `-1.4536`
- `market_context_high->unknown_4h` score `1.6673` n `133` status `ready` deltaP `10.1917` edge `0.1632` maxDD `-2.7098`
- `news_risk_high->unknown_4h` score `1.2586` n `38` status `ready` deltaP `13.5751` edge `0.0867` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.2353` n `110` status `ready` deltaP `6.2247` edge `0.1079` maxDD `-0.7163`
- `news_risk_high->metal_4h` score `0.9773` n `38` status `ready` deltaP `5.4878` edge `0.2376` maxDD `-6.9109`
- `market_context_high->crypto_major_1h` score `0.8429` n `136` status `ready` deltaP `9.0833` edge `0.1291` maxDD `-4.2199`
- `news_risk_high->fx_1h` score `0.8037` n `38` status `ready` deltaP `12.11` edge `0.0119` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
