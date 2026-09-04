# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T08:37:25.411949+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11484`

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

- `risk_on_high->unknown_4h` score `20.5849` n `133` status `ready` deltaP `8.5412` edge `1.7203` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.5849` n `133` status `ready` deltaP `8.5412` edge `1.7203` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `14.0168` n `181` status `ready` deltaP `11.7606` edge `1.1592` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.2444` n `133` status `ready` deltaP `-1.0536` edge `1.0851` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.2444` n `133` status `ready` deltaP `-1.0536` edge `1.0851` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.3548` n `191` status `ready` deltaP `0.5486` edge `0.9223` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.6896` n `162` status `ready` deltaP `16.8403` edge `0.4631` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `0.8748` n `133` status `ready` deltaP `12.2873` edge `0.4055` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.8748` n `133` status `ready` deltaP `12.2873` edge `0.4055` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.4825` n `65` status `ready` deltaP `7.1599` edge `0.0404` maxDD `-0.7681`
- `risk_on_high->metal_1h` score `0.1085` n `133` status `ready` deltaP `12.2631` edge `0.0034` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1085` n `133` status `ready` deltaP `12.2631` edge `0.0034` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0504` n `65` status `ready` deltaP `4.8273` edge `-0.0033` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.119` n `65` status `ready` deltaP `4.9517` edge `0.0017` maxDD `-0.9036`
- `news_risk_high->commodity_24h` score `-0.1503` n `65` status `ready` deltaP `3.6351` edge `-0.0175` maxDD `-0.2074`
- `risk_on_high->index_1h` score `-0.1785` n `133` status `ready` deltaP `3.5433` edge `-0.002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1785` n `133` status `ready` deltaP `3.5433` edge `-0.002` maxDD `-0.5605`
- `market_context_high->metal_1h` score `-0.2858` n `191` status `ready` deltaP `6.992` edge `0.0024` maxDD `-2.1858`
- `risk_on_high->crypto_alt_1h` score `-0.3049` n `133` status `ready` deltaP `4.3019` edge `0.0476` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.3049` n `133` status `ready` deltaP `4.3019` edge `0.0476` maxDD `-5.4685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
