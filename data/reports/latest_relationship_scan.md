# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T09:07:33.165534+00:00`
- Price records: `672`
- Market context records: `8077`
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

- `market_context_high->equity_24h` score `20.18` n `85` status `ready` deltaP `36.6887` edge `1.5281` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.8273` n `33` status `ready` deltaP `35.5553` edge `0.5032` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.3854` n `87` status `ready` deltaP `32.4205` edge `0.5306` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2616` n `85` status `ready` deltaP `35.8752` edge `0.4493` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.5248` n `33` status `ready` deltaP `30.1229` edge `0.3695` maxDD `-0.4605`
- `news_risk_high->equity_1h` score `3.4044` n `42` status `ready` deltaP `27.7944` edge `0.13` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2917` n `87` status `ready` deltaP `31.5881` edge `0.0825` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.9969` n `85` status `ready` deltaP `19.0152` edge `0.19` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7548` n `42` status `ready` deltaP `2.8443` edge `0.2383` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.5627` n `33` status `ready` deltaP `21.4523` edge `0.0896` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.397` n `87` status `ready` deltaP `22.0633` edge `0.1149` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.3487` n `85` status `ready` deltaP `31.257` edge `0.0577` maxDD `-0.6283`
- `market_context_high->equity_1h` score `2.3394` n `87` status `ready` deltaP `14.576` edge `0.1411` maxDD `-2.1322`
- `news_risk_high->crypto_alt_4h` score `2.2833` n `33` status `ready` deltaP `21.6417` edge `0.1975` maxDD `-1.924`
- `news_risk_high->fx_4h` score `1.847` n `33` status `ready` deltaP `24.5935` edge `0.0206` maxDD `-0.1179`
- `market_context_high->index_1h` score `1.129` n `87` status `ready` deltaP `14.9718` edge `0.021` maxDD `-0.4716`
- `news_risk_high->metal_4h` score `1.0808` n `33` status `ready` deltaP `10.5691` edge `0.0664` maxDD `-0.7433`
- `market_context_high->commodity_24h` score `0.8997` n `85` status `ready` deltaP `25.6907` edge `0.2074` maxDD `-14.3993`
- `market_context_high->metal_1h` score `0.7859` n `87` status `ready` deltaP `11.0744` edge `0.0295` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.5378` n `87` status `ready` deltaP `4.5048` edge `0.1265` maxDD `-3.9374`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
