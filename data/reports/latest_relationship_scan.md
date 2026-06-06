# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T08:52:21.747233+00:00`
- Price records: `672`
- Market context records: `3057`
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

- `market_context_high->crypto_alt_24h` score `25.7126` n `97` status `ready` deltaP `13.5131` edge `2.4443` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `13.8401` n `97` status `ready` deltaP `45.3769` edge `0.8749` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.4931` n `97` status `ready` deltaP `24.3145` edge `1.0088` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.3708` n `97` status `ready` deltaP `25.3329` edge `1.4359` maxDD `-18.3486`
- `market_context_high->index_24h` score `10.201` n `97` status `ready` deltaP `25.2899` edge `0.7987` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.5086` n `130` status `ready` deltaP `17.1248` edge `0.1596` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1361` n `134` status `ready` deltaP `1.3384` edge `0.022` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.4182` n `130` status `ready` deltaP `2.0379` edge `0.0569` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.5433` n `134` status `ready` deltaP `2.9895` edge `0.0167` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5909` n `134` status `ready` deltaP `-5.5188` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.6615` n `134` status `ready` deltaP `5.0786` edge `0.0943` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7618` n `97` status `ready` deltaP `0.3329` edge `-0.0127` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-0.8228` n `134` status `ready` deltaP `2.2366` edge `0.025` maxDD `-8.6319`
- `market_context_high->crypto_major_1h` score `-1.0025` n `134` status `ready` deltaP `3.7447` edge `0.0728` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-1.0176` n `134` status `ready` deltaP `3.8677` edge `-0.0375` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1384` n `130` status `ready` deltaP `-8.4897` edge `-0.0053` maxDD `-1.0574`
- `market_context_high->metal_1h` score `-1.1844` n `134` status `ready` deltaP `-1.7763` edge `-0.0032` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.2638` n `130` status `ready` deltaP `10.8865` edge `0.0563` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-3.024` n `130` status `ready` deltaP `18.5085` edge `0.2934` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.1942` n `130` status `ready` deltaP `8.9188` edge `0.0435` maxDD `-35.3306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
