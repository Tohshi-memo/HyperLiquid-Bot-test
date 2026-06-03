# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T03:22:24.607860+00:00`
- Price records: `672`
- Market context records: `2725`
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

- `market_context_high->crypto_alt_24h` score `11.2795` n `111` status `ready` deltaP `16.3523` edge `1.1803` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7151` n `111` status `ready` deltaP `17.652` edge `0.6414` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.0637` n `111` status `ready` deltaP `6.5175` edge `0.8492` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.0393` n `143` status `ready` deltaP `7.0112` edge `0.1452` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1034` n `143` status `ready` deltaP `10.2465` edge `0.0291` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1472` n `143` status `ready` deltaP `3.35` edge `0.0082` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1651` n `143` status `ready` deltaP `2.8988` edge `0.04` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.4283` n `143` status `ready` deltaP `16.3633` edge `0.2893` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.4955` n `143` status `ready` deltaP `-0.0481` edge `0.0034` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5047` n `143` status `ready` deltaP `1.3997` edge `0.0013` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5416` n `143` status `ready` deltaP `6.1451` edge `0.0656` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7528` n `143` status `ready` deltaP `-1.3997` edge `-0.0026` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.919` n `143` status `ready` deltaP `3.6473` edge `0.0448` maxDD `-9.622`
- `market_context_high->fx_24h` score `-0.9884` n `111` status `ready` deltaP `2.3133` edge `-0.0106` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-1.0165` n `143` status `ready` deltaP `-2.421` edge `0.0093` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.192` n `143` status `ready` deltaP `-3.9361` edge `0.0102` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3228` n `143` status `ready` deltaP `1.8186` edge `0.0103` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.5765` n `111` status `ready` deltaP `2.7544` edge `0.0889` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0295` n `143` status `ready` deltaP `-0.6396` edge `-0.0269` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.2835` n `143` status `ready` deltaP `-1.5767` edge `-0.0272` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
