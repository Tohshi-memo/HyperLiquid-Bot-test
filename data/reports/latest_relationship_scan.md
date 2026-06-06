# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T08:37:21.462499+00:00`
- Price records: `672`
- Market context records: `3056`
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

- `market_context_high->crypto_alt_24h` score `25.7352` n `98` status `ready` deltaP `13.9916` edge `2.443` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `13.7257` n `98` status `ready` deltaP `45.2665` edge `0.8661` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.5146` n `98` status `ready` deltaP `24.4934` edge `1.0094` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.3523` n `98` status `ready` deltaP `25.4854` edge `1.4325` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.9589` n `98` status `ready` deltaP `24.5536` edge `0.7876` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.5145` n `131` status `ready` deltaP `17.1837` edge `0.1597` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1555` n `135` status `ready` deltaP `1.0956` edge `0.022` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3974` n `131` status `ready` deltaP `2.3726` edge `0.0564` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5545` n `135` status `ready` deltaP `2.7578` edge `0.0168` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5753` n `135` status `ready` deltaP `-5.2484` edge `-0.0015` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.6296` n `135` status `ready` deltaP `5.4214` edge `0.0961` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7555` n `98` status `ready` deltaP `0.4854` edge `-0.0129` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-0.7985` n `135` status `ready` deltaP `2.5848` edge `0.0258` maxDD `-8.6319`
- `market_context_high->crypto_major_1h` score `-0.9681` n `135` status `ready` deltaP `4.1206` edge `0.0747` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-0.994` n `135` status `ready` deltaP `4.1772` edge `-0.0376` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1203` n `131` status `ready` deltaP `-8.1724` edge `-0.0051` maxDD `-1.0574`
- `market_context_high->metal_1h` score `-1.1571` n `135` status `ready` deltaP `-1.3562` edge `-0.0025` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.2707` n `131` status `ready` deltaP `10.6044` edge `0.0573` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-2.9531` n `131` status `ready` deltaP `18.8373` edge `0.3003` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.1488` n `131` status `ready` deltaP `9.2359` edge `0.0472` maxDD `-35.3306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
