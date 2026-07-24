# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T04:22:24.339174+00:00`
- Price records: `672`
- Market context records: `7740`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `4.3742` n `132` status `ready` deltaP `20.7897` edge `0.3601` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.9806` n `133` status `ready` deltaP `12.8585` edge `0.0401` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.7497` n `133` status `ready` deltaP `13.7367` edge `0.1427` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.5955` n `133` status `ready` deltaP `8.7968` edge `0.0769` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.5298` n `133` status `ready` deltaP `8.1996` edge `0.1012` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.4142` n `133` status `ready` deltaP `1.6636` edge `0.2333` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3986` n `133` status `ready` deltaP `9.0949` edge `0.0156` maxDD `-0.7743`
- `market_context_high->metal_24h` score `0.3021` n `133` status `ready` deltaP `6.8479` edge `0.1886` maxDD `-2.3927`
- `market_context_high->fx_24h` score `0.2946` n `132` status `ready` deltaP `17.3451` edge `0.0309` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `0.0969` n `133` status `ready` deltaP `3.8292` edge `0.0258` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.2301` n `133` status `ready` deltaP `3.0945` edge `0.0061` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2569` n `133` status `ready` deltaP `10.5585` edge `0.0425` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.3114` n `133` status `ready` deltaP `3.1052` edge `0.0127` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4387` n `133` status `ready` deltaP `0.3737` edge `-0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7632` n `133` status `ready` deltaP `2.465` edge `0.0203` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4697` n `133` status `ready` deltaP `1.1381` edge `0.0754` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5118` n `133` status `ready` deltaP `-4.4676` edge `-0.0012` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.6937` n `132` status `ready` deltaP `5.6858` edge `-0.0207` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.2093` n `133` status `ready` deltaP `-0.9747` edge `-0.1186` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.4765` n `132` status `ready` deltaP `-17.9311` edge `0.0123` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
