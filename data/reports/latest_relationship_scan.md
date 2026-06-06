# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T06:07:25.011767+00:00`
- Price records: `672`
- Market context records: `3045`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6968`

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

- `market_context_high->crypto_alt_24h` score `24.9863` n `99` status `ready` deltaP `12.8945` edge `2.3879` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.5311` n `99` status `ready` deltaP `24.6686` edge `1.0096` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.2053` n `99` status `ready` deltaP `43.5922` edge `0.8339` maxDD `-1.2589`
- `market_context_high->equity_24h` score `9.3441` n `99` status `ready` deltaP `24.0688` edge `1.3127` maxDD `-18.3486`
- `market_context_high->index_24h` score `8.9565` n `99` status `ready` deltaP `23.6585` edge `0.7142` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6481` n `129` status `ready` deltaP `17.8637` edge `0.1663` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1236` n `133` status `ready` deltaP `1.434` edge `0.0224` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4747` n `133` status `ready` deltaP `3.9789` edge `0.0189` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.4754` n `129` status `ready` deltaP `1.6981` edge `0.0544` maxDD `-3.7602`
- `market_context_high->crypto_alt_1h` score `-0.5296` n `133` status `ready` deltaP `6.5339` edge `0.1015` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.5428` n `133` status `ready` deltaP `-4.8906` edge `0.0` maxDD `-0.2921`
- `market_context_high->equity_1h` score `-0.6734` n `133` status `ready` deltaP `3.2405` edge `0.0334` maxDD `-8.3065`
- `market_context_high->crypto_major_1h` score `-0.8926` n `133` status `ready` deltaP `4.7172` edge `0.0804` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-0.9337` n `133` status `ready` deltaP `4.751` edge `-0.0364` maxDD `-3.1801`
- `market_context_high->index_4h` score `-0.9526` n `129` status `ready` deltaP `12.7127` edge `0.0624` maxDD `-16.8761`
- `market_context_high->fx_4h` score `-1.1379` n `129` status `ready` deltaP `-8.7883` edge `-0.0038` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.1723` n `133` status `ready` deltaP `-1.7537` edge `-0.0018` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.3092` n `99` status `ready` deltaP `-0.9312` edge `-0.0157` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9236` n `129` status `ready` deltaP `9.8423` edge `0.0523` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.2422` n `129` status `ready` deltaP `17.7171` edge `0.2707` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
