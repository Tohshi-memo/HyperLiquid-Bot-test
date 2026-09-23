# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T03:52:26.924842+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9762`

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

- `market_context_high->unknown_4h` score `46.1638` n `46` status `ready` deltaP `7.3171` edge `3.7982` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5791` n `46` status `ready` deltaP `13.5341` edge `2.3903` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6549` n `46` status `ready` deltaP `12.1453` edge `1.317` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.7848` n `46` status `ready` deltaP `10.5903` edge `0.9948` maxDD `0.0`
- `market_context_high->index_24h` score `5.6512` n `46` status `ready` deltaP `20.8258` edge `0.3408` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.8855` n `96` status `ready` deltaP `-9.2014` edge `1.1543` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.4994` n `96` status `ready` deltaP `34.8958` edge `0.2602` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.773` n `97` status `ready` deltaP `13.6079` edge `0.1981` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.1888` n `97` status `ready` deltaP `8.7299` edge `0.224` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.0917` n `46` status `ready` deltaP `24.536` edge `0.0241` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.9117` n `103` status `ready` deltaP `11.2115` edge `0.1336` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4881` n `103` status `ready` deltaP `13.4571` edge `0.0778` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3985` n `97` status `ready` deltaP `20.661` edge `0.0424` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.898` n `96` status `ready` deltaP `24.1319` edge `0.1132` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7981` n `46` status `ready` deltaP `6.7626` edge `0.0457` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6806` n `46` status `ready` deltaP `10.6548` edge `0.011` maxDD `-0.0249`
- `market_context_high->equity_4h` score `0.6281` n `46` status `ready` deltaP `4.7853` edge `0.0511` maxDD `-0.4529`
- `news_risk_high->metal_1h` score `0.4577` n `103` status `ready` deltaP `13.2565` edge `0.0091` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.4323` n `97` status `ready` deltaP `13.6928` edge `0.0405` maxDD `-1.9941`
- `market_context_high->metal_24h` score `0.3919` n `46` status `ready` deltaP `17.4064` edge `-0.06` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
