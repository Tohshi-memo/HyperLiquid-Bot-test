# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T11:07:24.340062+00:00`
- Price records: `672`
- Market context records: `8085`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.2765` n `87` status `ready` deltaP `36.9051` edge `1.5347` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4202` n `87` status `ready` deltaP `32.4205` edge `0.5335` maxDD `-2.5032`
- `news_risk_high->equity_4h` score `8.2865` n `41` status `ready` deltaP `34.2988` edge `0.4666` maxDD `-0.044`
- `market_context_high->metal_24h` score `8.2652` n `87` status `ready` deltaP `35.8752` edge `0.4496` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.9778` n `41` status `ready` deltaP `17.0732` edge `0.2665` maxDD `-1.907`
- `news_risk_high->equity_1h` score `3.4654` n `43` status `ready` deltaP `28.3317` edge `0.1315` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3061` n `87` status `ready` deltaP `31.5881` edge `0.0837` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0685` n `87` status `ready` deltaP `19.7454` edge `0.1911` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7625` n `43` status `ready` deltaP `4.4562` edge `0.2282` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.7374` n `41` status `ready` deltaP `25.0` edge `0.0805` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.3802` n `87` status `ready` deltaP `14.7257` edge `0.1435` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.2931` n `87` status `ready` deltaP `30.6818` edge `0.0569` maxDD `-0.6283`
- `market_context_high->metal_4h` score `2.2731` n `87` status `ready` deltaP `20.8438` edge `0.1127` maxDD `-0.979`
- `news_risk_high->metal_4h` score `1.5348` n `41` status `ready` deltaP `15.8536` edge `0.069` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.1578` n `87` status `ready` deltaP `15.2712` edge `0.0214` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `0.7865` n `87` status `ready` deltaP `5.7244` edge `0.1391` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.7835` n `87` status `ready` deltaP `11.0744` edge `0.0293` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.6964` n `43` status `ready` deltaP `3.0393` edge `0.0775` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `0.6244` n `87` status `ready` deltaP `25.3192` edge `0.1998` maxDD `-15.7497`
- `market_context_high->crypto_major_4h` score `0.566` n `87` status `ready` deltaP `8.4105` edge `0.1629` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
