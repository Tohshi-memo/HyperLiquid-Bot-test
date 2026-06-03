# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T07:22:21.663947+00:00`
- Price records: `672`
- Market context records: `2742`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->crypto_alt_24h` score `10.5436` n `112` status `ready` deltaP `15.749` edge `1.123` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.1296` n `112` status `ready` deltaP `16.4682` edge `0.6005` maxDD `-1.6255`
- `market_context_high->unknown_4h` score `1.1175` n `143` status `ready` deltaP `7.1636` edge `0.1507` maxDD `-3.7602`
- `market_context_high->crypto_major_24h` score `0.6943` n `112` status `ready` deltaP `6.0268` edge `0.8538` maxDD `-47.7309`
- `market_context_high->index_4h` score `0.1019` n `143` status `ready` deltaP `10.2465` edge `0.0289` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0884` n `143` status `ready` deltaP `3.4976` edge `0.0424` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1955` n `143` status `ready` deltaP `2.6015` edge `0.007` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5087` n `143` status `ready` deltaP `-0.1978` edge `0.0033` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6091` n `143` status `ready` deltaP `0.0524` edge `-0.0031` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.636` n `143` status `ready` deltaP `5.9954` edge `0.0545` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.6901` n `143` status `ready` deltaP `16.2108` edge `0.2685` maxDD `-28.7261`
- `market_context_high->metal_1h` score `-0.7668` n `143` status `ready` deltaP `-1.25` edge `-0.0054` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9627` n `143` status `ready` deltaP `3.4976` edge `0.0402` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.1041` n `143` status `ready` deltaP `-3.3356` edge `0.0081` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2417` n `112` status `ready` deltaP `-0.2232` edge `-0.0148` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.325` n `143` status `ready` deltaP `-5.1337` edge `0.0071` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.552` n `143` status `ready` deltaP `0.1418` edge `-0.0079` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6729` n `112` status `ready` deltaP `2.9265` edge `0.0754` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0435` n `143` status `ready` deltaP `-1.2493` edge `-0.024` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.3022` n `143` status `ready` deltaP `6.9046` edge `0.1494` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
