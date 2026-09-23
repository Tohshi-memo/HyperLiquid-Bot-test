# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T08:22:28.546604+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_4h` score `47.038` n `46` status `ready` deltaP `7.7744` edge `3.868` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.2707` n `46` status `ready` deltaP `13.5341` edge `2.3646` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.5973` n `46` status `ready` deltaP `12.1453` edge `1.3122` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.2664` n `46` status `ready` deltaP `10.5903` edge `0.9516` maxDD `0.0`
- `market_context_high->index_24h` score `5.632` n `46` status `ready` deltaP `20.8258` edge `0.3392` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.5771` n `96` status `ready` deltaP `-9.2014` edge `1.1286` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.3305` n `96` status `ready` deltaP `34.375` edge `0.2496` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.7649` n `103` status `ready` deltaP `13.9267` edge `0.1953` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.2015` n `103` status `ready` deltaP `8.4389` edge `0.227` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.1879` n `46` status `ready` deltaP `25.6031` edge `0.025` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.823` n `103` status `ready` deltaP `10.6127` edge `0.1302` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4749` n `103` status `ready` deltaP `13.3074` edge `0.0777` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3565` n `103` status `ready` deltaP `20.4801` edge `0.0401` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.0952` n `96` status `ready` deltaP `27.0833` edge `0.1188` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.8496` n `46` status `ready` deltaP `7.3614` edge `0.046` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.799` n `46` status `ready` deltaP `6.1572` edge `0.0562` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6818` n `46` status `ready` deltaP `10.6548` edge `0.0111` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.4781` n `103` status `ready` deltaP `13.4062` edge `0.0098` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2244` n `103` status `ready` deltaP `7.9574` edge `0.01` maxDD `-0.2147`
- `news_risk_high->metal_4h` score `0.1198` n `103` status `ready` deltaP `11.3737` edge `0.0353` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
