# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T19:07:28.023055+00:00`
- Price records: `672`
- Market context records: `8120`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11841`

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

- `market_context_high->equity_24h` score `22.0373` n `85` status `ready` deltaP `40.241` edge `1.6592` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.9055` n `86` status `ready` deltaP `35.5538` edge `0.616` maxDD `-0.872`
- `market_context_high->metal_24h` score `8.485` n `85` status `ready` deltaP `35.9375` edge `0.4675` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.9714` n `43` status `ready` deltaP `30.9026` edge `0.4788` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.2021` n `43` status `ready` deltaP `15.9175` edge `0.3046` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.8406` n `86` status `ready` deltaP `34.125` edge `0.099` maxDD `-0.1824`
- `news_risk_high->equity_1h` score `3.7151` n `43` status `ready` deltaP `29.0802` edge `0.1466` maxDD `-1.1366`
- `market_context_high->index_24h` score `3.5908` n `85` status `ready` deltaP `22.7492` edge `0.2146` maxDD `-1.3621`
- `market_context_high->equity_1h` score `3.0076` n `86` status `ready` deltaP `16.2895` edge `0.1723` maxDD `-1.088`
- `news_risk_high->unknown_1h` score `2.9135` n `43` status `ready` deltaP `5.6538` edge `0.2329` maxDD `-0.8909`
- `market_context_high->metal_4h` score `2.5282` n `86` status `ready` deltaP `23.3728` edge `0.1171` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.5053` n `43` status `ready` deltaP `21.3343` edge `0.0856` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.0922` n `86` status `ready` deltaP `11.3797` edge `0.2102` maxDD `-3.9374`
- `market_context_high->fx_24h` score `2.0039` n `85` status `ready` deltaP `27.7267` edge `0.0525` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `1.7275` n `86` status `ready` deltaP `12.4291` edge `0.2329` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.4548` n `86` status `ready` deltaP `17.2574` edge `0.0262` maxDD `-0.268`
- `market_context_high->commodity_24h` score `1.3155` n `85` status `ready` deltaP `30.194` edge `0.2559` maxDD `-15.7497`
- `news_risk_high->metal_4h` score `1.2259` n `43` status `ready` deltaP `12.9076` edge `0.0629` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.0322` n `43` status `ready` deltaP `4.5363` edge `0.0955` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.994` n `86` status `ready` deltaP `13.2851` edge `0.0321` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
