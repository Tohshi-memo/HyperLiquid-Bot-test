# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T11:37:33.687550+00:00`
- Price records: `672`
- Market context records: `8087`
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

- `market_context_high->equity_24h` score `20.3053` n `87` status `ready` deltaP `36.9051` edge `1.5371` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4094` n `87` status `ready` deltaP `32.4205` edge `0.5326` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2772` n `87` status `ready` deltaP `35.8752` edge `0.4506` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.8619` n `42` status `ready` deltaP `32.0921` edge `0.4517` maxDD `-0.1727`
- `news_risk_high->crypto_major_4h` score `3.6374` n `42` status `ready` deltaP `15.3891` edge `0.2556` maxDD `-2.0729`
- `news_risk_high->equity_1h` score `3.5145` n `43` status `ready` deltaP `28.6311` edge `0.1336` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3183` n `87` status `ready` deltaP `31.7406` edge `0.0837` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0757` n `87` status `ready` deltaP `19.7454` edge `0.1917` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7649` n `43` status `ready` deltaP `4.4562` edge `0.2284` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.5629` n `42` status `ready` deltaP `23.1199` edge `0.0785` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.4294` n `87` status `ready` deltaP `15.0251` edge `0.1456` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2719` n `87` status `ready` deltaP `20.8438` edge `0.1126` maxDD `-0.979`
- `market_context_high->fx_24h` score `2.2582` n `87` status `ready` deltaP `30.3352` edge `0.0563` maxDD `-0.6283`
- `news_risk_high->metal_4h` score `1.3498` n `42` status `ready` deltaP `14.1115` edge `0.0652` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.1877` n `87` status `ready` deltaP `15.5706` edge `0.0219` maxDD `-0.4716`
- `market_context_high->crypto_alt_4h` score `0.8083` n `87` status `ready` deltaP `5.8768` edge `0.1399` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.7859` n `87` status `ready` deltaP `11.0744` edge `0.0295` maxDD `-0.6936`
- `news_risk_high->crypto_major_1h` score `0.7396` n `43` status `ready` deltaP `3.3387` edge `0.0791` maxDD `-1.1783`
- `market_context_high->commodity_24h` score `0.6682` n `87` status `ready` deltaP `25.6658` edge `0.2031` maxDD `-15.7497`
- `market_context_high->crypto_major_1h` score `0.5867` n `87` status `ready` deltaP `9.6204` edge `0.0258` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
