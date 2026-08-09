# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T22:14:45.084728+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10858`

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

- `market_context_high->metal_24h` score `1.0844` n `122` status `ready` deltaP `6.4748` edge `0.1048` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.0675` n `143` status `ready` deltaP `14.1374` edge `0.062` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.828` n `155` status `ready` deltaP `10.9803` edge `0.0301` maxDD `-0.7439`
- `market_context_high->equity_24h` score `0.7877` n `122` status `ready` deltaP `3.6487` edge `0.3473` maxDD `-21.1456`
- `market_context_high->fx_24h` score `0.5048` n `122` status `ready` deltaP `19.1228` edge `0.0239` maxDD `-1.9329`
- `market_context_high->index_24h` score `-0.022` n `122` status `ready` deltaP `5.2226` edge `0.1155` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5697` n `155` status `ready` deltaP `0.9108` edge `-0.004` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.6181` n `155` status `ready` deltaP `-3.9724` edge `-0.0055` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6604` n `155` status `ready` deltaP `-3.8333` edge `-0.0077` maxDD `-1.1132`
- `market_context_high->fx_4h` score `-0.71` n `143` status `ready` deltaP `3.084` edge `-0.0044` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.9404` n `143` status `ready` deltaP `-1.373` edge `-0.0087` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9782` n `155` status `ready` deltaP `-0.4434` edge `0.0043` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9822` n `143` status `ready` deltaP `-1.3559` edge `-0.016` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.1632` n `155` status `ready` deltaP `-8.7521` edge `-0.0266` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5372` n `143` status `ready` deltaP `-1.8761` edge `-0.0652` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.162` n `155` status `ready` deltaP `-11.2546` edge `-0.0551` maxDD `-7.3365`
- `market_context_high->crypto_major_24h` score `-4.0859` n `122` status `ready` deltaP `2.8404` edge `-0.11` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.1364` n `143` status `ready` deltaP `-9.0387` edge `-0.1188` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-5.1309` n `122` status `ready` deltaP `-14.905` edge `-0.1839` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8993` n `155` status `ready` deltaP `-7.12` edge `-0.5651` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
