# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T01:22:23.749081+00:00`
- Price records: `672`
- Market context records: `2717`
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

- `market_context_high->crypto_alt_24h` score `11.0947` n `111` status `ready` deltaP `16.3523` edge `1.1649` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5863` n `111` status `ready` deltaP `16.9576` edge `0.6353` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8588` n `143` status `ready` deltaP `6.0965` edge `0.1359` maxDD `-3.7312`
- `market_context_high->crypto_major_24h` score `0.6573` n `111` status `ready` deltaP `6.5175` edge `0.7971` maxDD `-44.169`
- `market_context_high->index_4h` score `0.2113` n `143` status `ready` deltaP `11.466` edge `0.0348` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1487` n `143` status `ready` deltaP `3.35` edge `0.008` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2398` n `143` status `ready` deltaP `2.4497` edge `0.0365` maxDD `-3.1587`
- `market_context_high->crypto_alt_4h` score `-0.4309` n `143` status `ready` deltaP `16.2108` edge `0.2901` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.444` n `143` status `ready` deltaP `0.5507` edge `0.0037` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.4899` n `143` status `ready` deltaP `1.5494` edge `0.0022` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5042` n `143` status `ready` deltaP `6.4445` edge `0.0684` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7169` n `143` status `ready` deltaP `-0.9506` edge `-0.001` maxDD `-3.0996`
- `market_context_high->fx_24h` score `-0.8617` n `111` status `ready` deltaP `3.7022` edge `-0.0093` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-0.9374` n `143` status `ready` deltaP `-1.5063` edge `0.0098` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.9417` n `143` status `ready` deltaP `3.6473` edge `0.0419` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.2068` n `143` status `ready` deltaP `-4.336` edge `0.0122` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.2395` n `143` status `ready` deltaP `2.5808` edge `0.0159` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.3694` n `111` status `ready` deltaP `4.1432` edge `0.1062` maxDD `-12.4171`
- `market_context_high->index_24h` score `-1.823` n `111` status `ready` deltaP `0.0235` edge `-0.054` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-1.9693` n `143` status `ready` deltaP `-0.7291` edge `-0.0188` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
