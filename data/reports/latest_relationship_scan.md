# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T21:52:30.238976+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6549`

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

- `market_context_high->unknown_4h` score `73.0668` n `40` status `ready` deltaP `-4.1463` edge `6.1613` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.938` n `37` status `ready` deltaP `11.2472` edge `0.766` maxDD `-31.3588`
- `market_context_high->fx_4h` score `2.4844` n `40` status `ready` deltaP `27.1341` edge `0.0395` maxDD `-0.0691`
- `market_context_high->index_4h` score `1.6787` n `40` status `ready` deltaP `22.561` edge `0.0365` maxDD `-2.4279`
- `market_context_high->index_24h` score `1.1635` n `37` status `ready` deltaP `14.6913` edge `0.1143` maxDD `-2.7123`
- `market_context_high->equity_1h` score `0.9849` n `52` status `ready` deltaP `5.1935` edge `0.1583` maxDD `-2.6658`
- `market_context_high->fx_24h` score `0.8606` n `37` status `ready` deltaP `10.9422` edge `0.0076` maxDD `-0.0397`
- `market_context_high->commodity_1h` score `0.173` n `52` status `ready` deltaP `10.0184` edge `0.01` maxDD `-1.7019`
- `market_context_high->metal_1h` score `0.0702` n `52` status `ready` deltaP `4.2953` edge `0.01` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `-0.0154` n `37` status `ready` deltaP `2.9139` edge `0.0981` maxDD `-6.5601`
- `market_context_high->index_1h` score `-0.1338` n `52` status `ready` deltaP `-0.4261` edge `0.0239` maxDD `-0.3899`
- `market_context_high->crypto_alt_1h` score `-0.152` n `52` status `ready` deltaP `3.9152` edge `0.0401` maxDD `-3.1881`
- `market_context_high->commodity_4h` score `-0.2029` n `40` status `ready` deltaP `0.9756` edge `0.022` maxDD `-1.633`
- `market_context_high->crypto_major_1h` score `-0.4557` n `52` status `ready` deltaP `1.52` edge `0.0154` maxDD `-3.0501`
- `market_context_high->fx_1h` score `-0.5245` n `52` status `ready` deltaP `-3.6158` edge `0.0075` maxDD `-0.1681`
- `market_context_high->metal_4h` score `-0.8582` n `40` status `ready` deltaP `-4.6037` edge `-0.0343` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-1.1915` n `40` status `ready` deltaP `14.4512` edge `-0.0048` maxDD `-17.5435`
- `market_context_high->equity_4h` score `-1.2088` n `40` status `ready` deltaP `21.0671` edge `0.0868` maxDD `-24.9053`
- `market_context_high->metal_24h` score `-1.6259` n `37` status `ready` deltaP `7.3527` edge `-0.1292` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-4.1258` n `40` status `ready` deltaP `1.5549` edge `-0.1292` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
