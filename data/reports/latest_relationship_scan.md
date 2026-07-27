# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T11:52:30.642072+00:00`
- Price records: `672`
- Market context records: `8088`
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

- `market_context_high->equity_24h` score `20.3185` n `87` status `ready` deltaP `36.9051` edge `1.5382` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4034` n `87` status `ready` deltaP `32.4205` edge `0.5321` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2832` n `87` status `ready` deltaP `35.8752` edge `0.4511` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8559` n `42` status `ready` deltaP `32.0921` edge `0.4512` maxDD `-0.1727`
- `news_risk_high->crypto_major_4h` score `3.641` n `42` status `ready` deltaP `15.3891` edge `0.2559` maxDD `-2.0729`
- `news_risk_high->equity_1h` score `3.5421` n `43` status `ready` deltaP `28.7808` edge `0.1349` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3183` n `87` status `ready` deltaP `31.7406` edge `0.0837` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0793` n `87` status `ready` deltaP `19.7454` edge `0.192` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7817` n `43` status `ready` deltaP `4.6059` edge `0.2288` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.5629` n `42` status `ready` deltaP `23.1199` edge `0.0785` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.457` n `87` status `ready` deltaP `15.1748` edge `0.1469` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2841` n `87` status `ready` deltaP `20.9963` edge `0.1126` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.2407` n `87` status `ready` deltaP `30.1619` edge `0.056` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.362` n `42` status `ready` deltaP `14.264` edge `0.0652` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.2021` n `87` status `ready` deltaP `15.7203` edge `0.0221` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `0.8265` n `87` status `ready` deltaP `6.0292` edge `0.1404` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.8015` n `87` status `ready` deltaP `11.2241` edge `0.0298` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.7719` n `43` status `ready` deltaP `3.4884` edge `0.0808` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `0.6905` n `87` status `ready` deltaP `25.8391` edge `0.2048` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `0.619` n `87` status `ready` deltaP `9.7701` edge `0.0275` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
