# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T09:52:21.284325+00:00`
- Price records: `672`
- Market context records: `3061`
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

- `market_context_high->crypto_alt_24h` score `16.6695` n `93` status `ready` deltaP `11.4583` edge `2.4524` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.3028` n `93` status `ready` deltaP `45.8053` edge `0.9106` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.44` n `93` status `ready` deltaP `23.5607` edge `1.0094` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.1618` n `93` status `ready` deltaP `28.3938` edge `0.8414` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.2874` n `93` status `ready` deltaP `24.4792` edge `1.4309` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.4567` n `127` status `ready` deltaP `16.7755` edge `0.1576` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.2494` n `130` status `ready` deltaP `0.0415` edge `0.0212` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.2611` n `127` status `ready` deltaP `2.9071` edge `0.0642` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5674` n `130` status `ready` deltaP `2.8858` edge `0.0143` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6339` n `130` status `ready` deltaP `-6.345` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7527` n `130` status `ready` deltaP `3.8047` edge `0.0911` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7847` n `93` status `ready` deltaP `-0.3472` edge `-0.0111` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.0245` n `130` status `ready` deltaP `2.8812` edge `-0.0315` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-1.0587` n `130` status `ready` deltaP `0.79` edge `0.0044` maxDD `-8.6319`
- `market_context_high->crypto_major_1h` score `-1.09` n `130` status `ready` deltaP `2.4827` edge `0.07` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1937` n `127` status `ready` deltaP `-9.486` edge `-0.0056` maxDD `-1.0693`
- `market_context_high->metal_1h` score `-1.2846` n `130` status `ready` deltaP `-3.3717` edge `-0.0054` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.3105` n `127` status `ready` deltaP `9.8689` edge `0.0571` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-2.8978` n `127` status `ready` deltaP `18.7608` edge `0.3079` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.433` n `127` status `ready` deltaP `8.0901` edge `0.0184` maxDD `-35.3306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
