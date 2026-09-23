# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T08:07:32.195035+00:00`
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

- `market_context_high->unknown_4h` score `47.0404` n `46` status `ready` deltaP `7.7744` edge `3.8682` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.2635` n `46` status `ready` deltaP `13.5341` edge `2.364` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6081` n `46` status `ready` deltaP `12.1453` edge `1.3131` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.2688` n `46` status `ready` deltaP `10.5903` edge `0.9518` maxDD `0.0`
- `market_context_high->index_24h` score `5.6344` n `46` status `ready` deltaP `20.8258` edge `0.3394` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.5699` n `96` status `ready` deltaP `-9.2014` edge `1.128` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.354` n `96` status `ready` deltaP `34.5486` edge `0.2504` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.7179` n `103` status `ready` deltaP `13.7743` edge `0.1924` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.1919` n `103` status `ready` deltaP `8.4389` edge `0.2262` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.1745` n `46` status `ready` deltaP `25.4506` edge `0.0249` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.8026` n `103` status `ready` deltaP `10.463` edge `0.1295` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4497` n `103` status `ready` deltaP `13.1577` edge `0.0766` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3723` n `103` status `ready` deltaP `20.6326` edge `0.0404` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.0838` n `96` status `ready` deltaP `26.9097` edge `0.1185` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.8496` n `46` status `ready` deltaP `7.3614` edge `0.046` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7784` n `46` status `ready` deltaP `6.0048` edge `0.0555` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6699` n `46` status `ready` deltaP `10.5051` edge `0.0111` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.4781` n `103` status `ready` deltaP `13.4062` edge `0.0098` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2232` n `103` status `ready` deltaP `7.9574` edge `0.0099` maxDD `-0.2147`
- `news_risk_high->metal_4h` score `0.1088` n `103` status `ready` deltaP `11.2213` edge `0.0349` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
