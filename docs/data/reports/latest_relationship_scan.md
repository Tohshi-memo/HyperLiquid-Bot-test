# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T16:37:25.897886+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5915`

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

- `news_risk_high->unknown_24h` score `5190.6942` n `60` status `ready` deltaP `34.2345` edge `432.3717` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.8154` n `53` status `ready` deltaP `54.4979` edge `1.0777` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.447` n `60` status `ready` deltaP `23.3028` edge `0.4416` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.624` n `60` status `ready` deltaP `22.9979` edge `0.0844` maxDD `-0.191`
- `market_context_high->commodity_24h` score `2.1655` n `53` status `ready` deltaP `30.7773` edge `0.2583` maxDD `-10.2019`
- `news_risk_high->crypto_major_4h` score `1.3023` n `60` status `ready` deltaP `7.7439` edge `0.1929` maxDD `-3.5385`
- `news_risk_high->equity_1h` score `1.1051` n `64` status `ready` deltaP `11.1995` edge `0.0806` maxDD `-2.7202`
- `news_risk_high->crypto_alt_4h` score `0.5293` n `60` status `ready` deltaP `11.6768` edge `0.1292` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5148` n `53` status `ready` deltaP `8.2806` edge `0.1065` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.4514` n `64` status `ready` deltaP `8.4113` edge `0.057` maxDD `-2.0834`
- `news_risk_high->fx_4h` score `0.2523` n `60` status `ready` deltaP `13.8415` edge `0.0245` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `0.2239` n `64` status `ready` deltaP `4.9869` edge `0.0502` maxDD `-2.3794`
- `market_context_high->fx_4h` score `0.205` n `53` status `ready` deltaP `13.5585` edge `0.0155` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1448` n `60` status `ready` deltaP `4.6748` edge `0.035` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `0.0124` n `64` status `ready` deltaP `5.1179` edge `0.0078` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.0149` n `53` status `ready` deltaP `7.2026` edge `0.001` maxDD `-0.6874`
- `news_risk_high->fx_1h` score `-0.0245` n `64` status `ready` deltaP `3.7238` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0275` n `64` status `ready` deltaP `2.9566` edge `0.0086` maxDD `-0.5471`
- `market_context_high->commodity_1h` score `-0.0753` n `53` status `ready` deltaP `4.1775` edge `0.0166` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `-0.1846` n `53` status `ready` deltaP `4.7918` edge `0.0319` maxDD `-3.0005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
