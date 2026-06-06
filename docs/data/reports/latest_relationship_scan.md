# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T05:22:20.901748+00:00`
- Price records: `672`
- Market context records: `3041`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->crypto_alt_24h` score `24.527` n `99` status `ready` deltaP `12.3737` edge `2.3531` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.4066` n `99` status `ready` deltaP `24.1477` edge `1.0027` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.0689` n `99` status `ready` deltaP `43.0713` edge `0.826` maxDD `-1.2589`
- `market_context_high->equity_24h` score `9.0066` n `99` status `ready` deltaP `23.548` edge `1.2729` maxDD `-18.3486`
- `market_context_high->index_24h` score `8.6497` n `99` status `ready` deltaP `23.1377` edge `0.6921` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6397` n `129` status `ready` deltaP `17.8637` edge `0.1656` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1272` n `132` status `ready` deltaP `1.3745` edge `0.0225` maxDD `-1.7142`
- `market_context_high->unknown_1h` score `-0.4385` n `132` status `ready` deltaP `4.7315` edge `0.005` maxDD `-3.1801`
- `market_context_high->unknown_4h` score `-0.4802` n `129` status `ready` deltaP `1.6981` edge `0.054` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5097` n `132` status `ready` deltaP `3.62` edge `0.0168` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5406` n `132` status `ready` deltaP `-4.8539` edge `0.0` maxDD `-0.289`
- `market_context_high->crypto_alt_1h` score `-0.6402` n `132` status `ready` deltaP `6.4916` edge `0.0876` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.7153` n `132` status `ready` deltaP `3.0485` edge `0.0293` maxDD `-8.3065`
- `market_context_high->index_4h` score `-0.9754` n `129` status `ready` deltaP `12.5602` edge `0.0605` maxDD `-16.8761`
- `market_context_high->crypto_major_1h` score `-1.0011` n `132` status `ready` deltaP `4.491` edge `0.068` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1624` n `129` status `ready` deltaP `-9.2456` edge `-0.0039` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.2011` n `132` status `ready` deltaP `-2.0369` edge `-0.0036` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.3652` n `99` status `ready` deltaP `-1.452` edge `-0.0169` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9716` n `129` status `ready` deltaP `9.385` edge `0.0492` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.3147` n `129` status `ready` deltaP `17.7171` edge `0.2614` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
