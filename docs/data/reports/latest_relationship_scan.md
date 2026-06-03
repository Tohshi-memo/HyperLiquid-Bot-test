# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T00:52:21.998185+00:00`
- Price records: `672`
- Market context records: `2715`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `11.0407` n `111` status `ready` deltaP `16.3523` edge `1.1604` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6067` n `111` status `ready` deltaP `16.9576` edge `0.637` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8226` n `143` status `ready` deltaP `5.9441` edge `0.1339` maxDD `-3.7312`
- `market_context_high->crypto_major_24h` score `0.5567` n `111` status `ready` deltaP `6.5175` edge `0.7842` maxDD `-44.169`
- `market_context_high->index_4h` score `0.2381` n `143` status `ready` deltaP `11.7709` edge `0.0362` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1355` n `143` status `ready` deltaP `3.4997` edge `0.0087` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2434` n `143` status `ready` deltaP `2.4497` edge `0.0362` maxDD `-3.1587`
- `market_context_high->crypto_alt_4h` score `-0.4141` n `143` status `ready` deltaP `16.2108` edge `0.2915` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.4177` n `143` status `ready` deltaP `0.8501` edge `0.0039` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.465` n `143` status `ready` deltaP `1.8488` edge `0.0034` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.4691` n `143` status `ready` deltaP `6.7439` edge `0.0709` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7154` n `143` status `ready` deltaP `-0.9506` edge `-0.0008` maxDD `-3.0996`
- `market_context_high->fx_24h` score `-0.8267` n `111` status `ready` deltaP `4.0494` edge `-0.0087` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-0.9106` n `143` status `ready` deltaP `-1.2014` edge `0.01` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.9308` n `143` status `ready` deltaP `3.797` edge `0.0423` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.2092` n `143` status `ready` deltaP `-4.336` edge `0.012` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.2261` n `143` status `ready` deltaP `2.7333` edge `0.0166` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.31` n `111` status `ready` deltaP `4.4905` edge `0.1115` maxDD `-12.4171`
- `market_context_high->index_24h` score `-1.6992` n `111` status `ready` deltaP `0.3707` edge `-0.046` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-1.9705` n `143` status `ready` deltaP `-0.7291` edge `-0.0189` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
