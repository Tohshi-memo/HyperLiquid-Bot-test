# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T11:37:23.440140+00:00`
- Price records: `672`
- Market context records: `3069`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `17.0725` n `90` status `ready` deltaP `11.9791` edge `2.5006` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.8496` n `90` status `ready` deltaP `46.8055` edge `0.9495` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.5785` n `90` status `ready` deltaP `22.9514` edge `1.025` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.2697` n `90` status `ready` deltaP `30.9028` edge `0.9045` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.817` n `90` status `ready` deltaP `24.5834` edge `1.4981` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.3701` n `127` status `ready` deltaP `16.2929` edge `0.1536` maxDD `-2.8438`
- `market_context_high->unknown_4h` score `-0.1641` n `127` status `ready` deltaP `2.7547` edge `0.0733` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.3111` n `127` status `ready` deltaP `-0.6542` edge `0.0207` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.588` n `127` status `ready` deltaP `2.3398` edge `0.0153` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.6646` n `127` status `ready` deltaP `4.2529` edge `0.0994` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.77` n `90` status `ready` deltaP `-0.5902` edge `-0.0076` maxDD `-0.6418`
- `market_context_high->fx_1h` score `-0.9726` n `127` status `ready` deltaP `-6.2827` edge `-0.0019` maxDD `-0.3147`
- `market_context_high->unknown_1h` score `-0.9793` n `127` status `ready` deltaP `2.651` edge `-0.0262` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0841` n `127` status `ready` deltaP `1.6962` edge `0.076` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.0972` n `127` status `ready` deltaP `-0.0554` edge `0.0051` maxDD `-8.6319`
- `market_context_high->fx_4h` score `-1.2555` n `127` status `ready` deltaP `-10.6035` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->metal_1h` score `-1.3263` n `127` status `ready` deltaP `-4.115` edge `-0.0058` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.3976` n `127` status `ready` deltaP `8.599` edge `0.0544` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-3.0516` n `127` status `ready` deltaP `17.9482` edge `0.2936` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7213` n `127` status `ready` deltaP `6.4901` edge `0.0035` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
