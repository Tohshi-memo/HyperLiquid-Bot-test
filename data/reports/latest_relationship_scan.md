# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T07:37:23.190115+00:00`
- Price records: `672`
- Market context records: `2743`
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

- `market_context_high->crypto_alt_24h` score `10.225` n `113` status `ready` deltaP `15.1564` edge `1.1004` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `7.8899` n `113` status `ready` deltaP `15.6465` edge `0.586` maxDD `-1.6255`
- `market_context_high->unknown_4h` score `1.0945` n `143` status `ready` deltaP `7.0112` edge `0.1498` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1145` n `143` status `ready` deltaP `10.3989` edge `0.0295` maxDD `-2.3986`
- `market_context_high->crypto_major_24h` score `0.0033` n `113` status `ready` deltaP `5.5448` edge `0.817` maxDD `-51.2836`
- `market_context_high->unknown_1h` score `-0.0764` n `143` status `ready` deltaP `3.6473` edge `0.0424` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1877` n `143` status `ready` deltaP `2.7512` edge `0.007` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5207` n `143` status `ready` deltaP `-0.3475` edge `0.0033` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6239` n `143` status `ready` deltaP `-0.0973` edge `-0.004` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6344` n `143` status `ready` deltaP `5.9954` edge `0.0547` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.7598` n `143` status `ready` deltaP `16.0584` edge `0.2637` maxDD `-28.7261`
- `market_context_high->metal_1h` score `-0.7661` n `143` status `ready` deltaP `-1.25` edge `-0.0053` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9619` n `143` status `ready` deltaP `3.4976` edge `0.0403` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.1187` n `143` status `ready` deltaP `-3.488` edge `0.0079` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2391` n `113` status `ready` deltaP `-0.1598` edge `-0.015` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.3082` n `143` status `ready` deltaP `-4.984` edge `0.0075` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.5669` n `143` status `ready` deltaP `-0.0106` edge `-0.0088` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6022` n `113` status `ready` deltaP `3.2663` edge `0.0822` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0363` n `143` status `ready` deltaP `-1.2493` edge `-0.0234` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.3256` n `143` status `ready` deltaP `6.9046` edge `0.1464` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
