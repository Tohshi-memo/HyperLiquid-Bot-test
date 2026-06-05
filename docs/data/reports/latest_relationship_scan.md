# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T02:37:25.291253+00:00`
- Price records: `672`
- Market context records: `2928`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `14.4975` n `142` status `ready` deltaP `14.1604` edge `1.5054` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.1314` n `142` status `ready` deltaP `16.3732` edge `0.6855` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.2235` n `142` status `ready` deltaP `14.2336` edge `0.4702` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.4697` n `142` status `ready` deltaP `12.1479` edge `0.2229` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8475` n `142` status `ready` deltaP `15.7252` edge `0.3585` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.7594` n `142` status `ready` deltaP `8.2124` edge `0.1465` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.6767` n `142` status `ready` deltaP `14.5204` edge `0.0741` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.0221` n `142` status `ready` deltaP `3.7465` edge `0.0822` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `-0.0167` n `142` status `ready` deltaP `15.2525` edge `0.331` maxDD `-28.7261`
- `market_context_high->index_1h` score `-0.0482` n `143` status `ready` deltaP `3.9488` edge `0.0169` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.4639` n `143` status `ready` deltaP `0.3047` edge `0.0426` maxDD `-2.6634`
- `market_context_high->unknown_1h` score `-0.4871` n `143` status `ready` deltaP `3.2987` edge `0.0105` maxDD `-3.1801`
- `market_context_high->crypto_alt_1h` score `-0.5327` n `143` status `ready` deltaP `5.5955` edge `0.0704` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5722` n `143` status `ready` deltaP `-0.9463` edge `0.003` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.652` n `143` status `ready` deltaP `0.247` edge `0.0035` maxDD `-3.4325`
- `market_context_high->crypto_major_1h` score `-0.6928` n `143` status `ready` deltaP `5.4929` edge `0.0615` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.6968` n `143` status `ready` deltaP `-1.8445` edge `-0.0017` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-1.014` n `142` status `ready` deltaP `-1.9237` edge `0.0062` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2836` n `142` status `ready` deltaP `1.8378` edge `0.0152` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.29` n `142` status `ready` deltaP `-1.7116` edge `-0.0089` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
