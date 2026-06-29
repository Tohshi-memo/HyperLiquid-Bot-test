# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T22:18:31.052100+00:00`
- Price records: `672`
- Market context records: `5187`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5644`

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

- `market_context_high->unknown_24h` score `21.2135` n `84` status `ready` deltaP `33.0853` edge `1.5662` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.9757` n `84` status `ready` deltaP `26.7113` edge `1.2694` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.2464` n `84` status `ready` deltaP `27.5049` edge `1.0092` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.4839` n `155` status `ready` deltaP `19.7266` edge `0.4277` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `4.3018` n `155` status `ready` deltaP `13.4599` edge `0.498` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `4.3002` n `155` status `ready` deltaP `12.4745` edge `0.4351` maxDD `-9.46`
- `market_context_high->unknown_1h` score `2.5508` n `155` status `ready` deltaP `9.1375` edge `0.2158` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.2366` n `155` status `ready` deltaP `9.2269` edge `0.2054` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.4737` n `155` status `ready` deltaP `4.0545` edge `0.1086` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4518` n `155` status `ready` deltaP `5.9542` edge `0.1225` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.2537` n `155` status `ready` deltaP `7.6154` edge `0.0669` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.207` n `84` status `ready` deltaP `11.5328` edge `0.0299` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0238` n `155` status `ready` deltaP `5.7833` edge `0.0138` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0701` n `155` status `ready` deltaP `4.8599` edge `0.0178` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2736` n `155` status `ready` deltaP `1.5096` edge `0.0001` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.402` n `155` status `ready` deltaP `6.5155` edge `0.0348` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.4831` n `155` status `ready` deltaP `5.1682` edge `0.007` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5884` n `155` status `ready` deltaP `0.875` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->index_24h` score `-1.01` n `84` status `ready` deltaP `7.3661` edge `-0.0151` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2524` n `155` status `ready` deltaP `0.5074` edge `0.0364` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
