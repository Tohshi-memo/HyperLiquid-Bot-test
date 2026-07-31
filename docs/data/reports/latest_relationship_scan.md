# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T18:38:31.153470+00:00`
- Price records: `672`
- Market context records: `8539`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5925`

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

- `news_risk_high->unknown_24h` score `5977.8267` n `54` status `ready` deltaP `42.7662` edge `497.9092` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.67` n `64` status `ready` deltaP `20.6555` edge `0.3945` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9767` n `64` status `ready` deltaP `16.1966` edge `0.0758` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6234` n `64` status `ready` deltaP `15.5034` edge `0.0796` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0022` n `64` status `ready` deltaP `6.593` edge `0.1621` maxDD `-3.5385`
- `market_context_high->crypto_alt_4h` score `0.983` n `55` status `ready` deltaP `9.8586` edge `0.156` maxDD `-5.323`
- `news_risk_high->crypto_alt_4h` score `0.735` n `64` status `ready` deltaP `14.1768` edge `0.1389` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4461` n `64` status `ready` deltaP `8.1119` edge `0.0558` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3181` n `64` status `ready` deltaP `6.4652` edge `0.0489` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0792` n `64` status `ready` deltaP `5.1366` edge `0.004` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0034` n `64` status `ready` deltaP `3.4712` edge `0.0081` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0151` n `64` status `ready` deltaP `2.0198` edge `0.0322` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `-0.0501` n `64` status `ready` deltaP `10.5564` edge `0.0212` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1611` n `64` status `ready` deltaP `2.9566` edge `0.0072` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2856` n `62` status `ready` deltaP `2.062` edge `-0.0001` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.327` n `62` status `ready` deltaP `3.559` edge `-0.0031` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5306` n `62` status `ready` deltaP `-2.9264` edge `0.0142` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7884` n `62` status `ready` deltaP `0.4974` edge `-0.0161` maxDD `-1.5667`
- `market_context_high->fx_4h` score `-0.8675` n `55` status `ready` deltaP `0.8121` edge `0.0019` maxDD `-1.3685`
- `market_context_high->metal_1h` score `-1.002` n `62` status `ready` deltaP `-3.2934` edge `-0.0121` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
