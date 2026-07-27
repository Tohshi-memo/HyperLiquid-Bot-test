# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T22:52:28.729983+00:00`
- Price records: `672`
- Market context records: `8138`
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

- `market_context_high->equity_24h` score `23.5963` n `84` status `ready` deltaP `42.7331` edge `1.7725` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.9571` n `85` status `ready` deltaP `35.7335` edge `0.615` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.7062` n `84` status `ready` deltaP `36.6319` edge `0.4813` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.6834` n `43` status `ready` deltaP `29.988` edge `0.4609` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.2871` n `43` status `ready` deltaP `16.6797` edge `0.3066` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.0281` n `84` status `ready` deltaP `24.9752` edge `0.2362` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.8565` n `85` status `ready` deltaP `34.0136` edge `0.0989` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.5593` n `43` status `ready` deltaP `28.0323` edge `0.1406` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.0553` n `85` status `ready` deltaP `16.0761` edge `0.1777` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.5885` n `85` status `ready` deltaP `23.707` edge `0.1199` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.3681` n `43` status `ready` deltaP `20.1148` edge `0.0823` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.2321` n `85` status `ready` deltaP `12.2436` edge `0.2161` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.2062` n `84` status `ready` deltaP `29.9107` edge `0.0548` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.9662` n `85` status `ready` deltaP `13.9437` edge `0.2427` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.7009` n `84` status `ready` deltaP `32.4901` edge `0.29` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.4857` n `85` status `ready` deltaP `17.4657` edge `0.027` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.1783` n `43` status `ready` deltaP `12.2979` edge `0.063` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.0597` n `43` status `ready` deltaP `4.686` edge `0.0968` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.012` n `85` status `ready` deltaP `13.466` edge `0.0324` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.757` n `85` status `ready` deltaP `12.3741` edge `0.0556` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
