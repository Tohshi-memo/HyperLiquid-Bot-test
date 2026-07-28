# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T05:07:24.729777+00:00`
- Price records: `672`
- Market context records: `8164`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `news_risk_high->unknown_24h` score `7935.2134` n `33` status `ready` deltaP `37.1528` edge `661.0201` maxDD `0.0`
- `market_context_high->equity_24h` score `19.4817` n `66` status `ready` deltaP `44.476` edge `1.418` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.5319` n `67` status `ready` deltaP `37.9641` edge `0.5647` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.9603` n `43` status `ready` deltaP `33.7989` edge `0.5419` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.2727` n `66` status `ready` deltaP `40.7986` edge `0.4174` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.4558` n `43` status `ready` deltaP `20.3382` edge `0.3796` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0087` n `67` status `ready` deltaP `36.5604` edge `0.0946` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.5937` n `46` status `ready` deltaP `26.842` edge `0.1514` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.5353` n `67` status `ready` deltaP `21.0341` edge `0.1747` maxDD `-0.6254`
- `market_context_high->index_24h` score `3.1148` n `66` status `ready` deltaP `20.5492` edge `0.1896` maxDD `-1.3621`
- `news_risk_high->index_4h` score `2.8626` n `43` status `ready` deltaP `23.9258` edge `0.0981` maxDD `-0.191`
- `market_context_high->metal_4h` score `1.9992` n `67` status `ready` deltaP `22.4609` edge `0.0791` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.7584` n `66` status `ready` deltaP `24.1636` edge `0.0558` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.7437` n `67` status `ready` deltaP `20.299` edge `0.024` maxDD `-0.1214`
- `news_risk_high->metal_4h` score `1.7388` n `43` status `ready` deltaP `16.1089` edge `0.0843` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.4114` n `46` status `ready` deltaP `7.3418` edge `0.1084` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `1.3212` n `66` status `ready` deltaP `29.6875` edge `0.26` maxDD `-15.7497`
- `news_risk_high->crypto_alt_4h` score `1.1785` n `43` status `ready` deltaP `12.8651` edge `0.2045` maxDD `-5.8012`
- `market_context_high->crypto_major_1h` score `1.0421` n `67` status `ready` deltaP `11.203` edge `0.0532` maxDD `-1.6171`
- `market_context_high->metal_1h` score `0.9001` n `67` status `ready` deltaP `12.6821` edge `0.0283` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
