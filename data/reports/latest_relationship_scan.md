# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T15:52:32.660995+00:00`
- Price records: `672`
- Market context records: `6195`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.707` n `32` status `ready` deltaP `42.2194` edge `0.7922` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.8531` n `32` status `ready` deltaP `59.8639` edge `0.172` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0703` n `32` status `ready` deltaP `42.4487` edge `0.0608` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.362` n `32` status `ready` deltaP `28.4431` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.1209` n `32` status `ready` deltaP `15.625` edge `0.2457` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.7878` n `192` status `ready` deltaP `0.7641` edge `0.2447` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.4195` n `32` status `ready` deltaP `14.4274` edge `0.1325` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7749` n `32` status `ready` deltaP `9.6744` edge `0.081` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.2886` n `192` status `ready` deltaP `-2.4332` edge `0.2935` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `0.2433` n `32` status `ready` deltaP `17.0281` edge `-0.0727` maxDD `-0.3101`
- `market_context_high->metal_24h` score `0.0411` n `192` status `ready` deltaP `19.8023` edge `0.1301` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.206` n `32` status `ready` deltaP `9.1412` edge `-0.0002` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2816` n `192` status `ready` deltaP `1.3598` edge `-0.0006` maxDD `-0.5659`
- `market_context_high->equity_4h` score `-0.592` n `192` status `ready` deltaP `1.1683` edge `0.0346` maxDD `-2.671`
- `market_context_high->metal_4h` score `-0.6794` n `192` status `ready` deltaP `3.2311` edge `0.0101` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7093` n `192` status `ready` deltaP `-2.0958` edge `-0.0005` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8135` n `32` status `ready` deltaP `-3.8922` edge `-0.0286` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.8802` n `192` status `ready` deltaP `4.5316` edge `0.0337` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8888` n `192` status `ready` deltaP `3.9452` edge `0.035` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9108` n `192` status `ready` deltaP `1.3161` edge `-0.0048` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
