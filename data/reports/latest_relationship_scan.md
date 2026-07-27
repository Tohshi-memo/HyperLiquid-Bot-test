# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T13:07:33.489421+00:00`
- Price records: `672`
- Market context records: `8094`
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

- `market_context_high->equity_24h` score `20.3413` n `87` status `ready` deltaP `36.9051` edge `1.5401` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4` n `87` status `ready` deltaP `32.5729` edge `0.5308` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3096` n `87` status `ready` deltaP `35.8752` edge `0.4533` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8257` n `42` status `ready` deltaP `32.2445` edge `0.4476` maxDD `-0.1672`
- `news_risk_high->crypto_major_4h` score `3.7194` n `42` status `ready` deltaP `15.6939` edge `0.2604` maxDD `-2.0729`
- `news_risk_high->equity_1h` score `3.5675` n `43` status `ready` deltaP `28.9305` edge `0.1353` maxDD `-1.1366`
- `market_context_high->index_4h` score `3.3183` n `87` status `ready` deltaP `31.7406` edge `0.0837` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0853` n `87` status `ready` deltaP `19.7454` edge `0.1925` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.8008` n `43` status `ready` deltaP `4.7556` edge `0.2295` maxDD `-0.8909`
- `news_risk_high->index_4h` score `2.5629` n `42` status `ready` deltaP `23.1199` edge `0.0785` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.4761` n `87` status `ready` deltaP `15.3245` edge `0.1475` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2877` n `87` status `ready` deltaP `20.9963` edge `0.1129` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.1546` n `87` status `ready` deltaP `29.2954` edge `0.0546` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.3656` n `42` status `ready` deltaP `14.264` edge `0.0655` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2153` n `87` status `ready` deltaP `15.87` edge `0.0222` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `0.9293` n `87` status `ready` deltaP `6.639` edge `0.1449` maxDD `-3.9374`
- `news_risk_high->crypto_major_1h` score `0.8151` n `43` status `ready` deltaP `3.7878` edge `0.0824` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `0.8034` n `87` status `ready` deltaP `26.7057` edge `0.2135` maxDD `-15.7497`
- `market_context_high->metal_1h` score `0.7979` n `87` status `ready` deltaP `11.2241` edge `0.0295` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6622` n `87` status `ready` deltaP `10.0695` edge `0.0291` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
