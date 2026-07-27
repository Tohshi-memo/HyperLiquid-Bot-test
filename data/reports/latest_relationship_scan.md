# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T10:37:31.225809+00:00`
- Price records: `672`
- Market context records: `8083`
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

- `market_context_high->equity_24h` score `20.2585` n `87` status `ready` deltaP `36.9051` edge `1.5332` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.7087` n `39` status `ready` deltaP `36.4877` edge `0.4871` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.4214` n `87` status `ready` deltaP `32.4205` edge `0.5336` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2568` n `87` status `ready` deltaP `35.8752` edge `0.4489` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `4.5193` n `39` status `ready` deltaP `20.3956` edge `0.2864` maxDD `-1.6613`
- `news_risk_high->equity_1h` score `3.4294` n `43` status `ready` deltaP `28.0323` edge `0.1305` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3037` n `87` status `ready` deltaP `31.5881` edge `0.0835` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0649` n `87` status `ready` deltaP `19.7454` edge `0.1908` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.735` n `43` status `ready` deltaP `4.1568` edge `0.2279` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.7085` n `39` status `ready` deltaP `24.2495` edge `0.0831` maxDD `-0.191`
- `market_context_high->equity_1h` score `2.3443` n `87` status `ready` deltaP `14.4263` edge `0.1425` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.328` n `87` status `ready` deltaP `31.0285` edge `0.0575` maxDD `-0.6283`
- `market_context_high->metal_4h` score `2.3022` n `87` status `ready` deltaP `21.1487` edge `0.1131` maxDD `-0.979`
- `news_risk_high->metal_4h` score `1.4707` n `39` status `ready` deltaP `14.7827` edge `0.0708` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.1446` n `87` status `ready` deltaP `15.1215` edge `0.0213` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.7847` n `87` status `ready` deltaP `11.0744` edge `0.0294` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.7466` n `87` status `ready` deltaP `5.4195` edge `0.1378` maxDD `-3.9374`
- `news_risk_high->crypto_major_1h` score `0.6952` n `43` status `ready` deltaP `3.0393` edge `0.0774` maxDD `-1.1783`
- `news_risk_high->fx_4h` score `0.6153` n `39` status `ready` deltaP `14.3371` edge `0.0143` maxDD `-0.1464`
- `market_context_high->commodity_24h` score `0.5776` n `87` status `ready` deltaP `24.9726` edge `0.1961` maxDD `-15.7497`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
