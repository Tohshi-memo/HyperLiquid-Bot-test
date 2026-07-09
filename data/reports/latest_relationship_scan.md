# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T00:22:31.217433+00:00`
- Price records: `672`
- Market context records: `6140`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `11.1632` n `30` status `ready` deltaP `40.3819` edge `0.6758` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7493` n `30` status `ready` deltaP `68.5764` edge `0.1886` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3457` n `32` status `ready` deltaP `45.3506` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4554` n `32` status `ready` deltaP `29.491` edge `0.0219` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4886` n `195` status `ready` deltaP `0.9543` edge `0.2185` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.163` n `32` status `ready` deltaP `12.7807` edge `0.1106` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5816` n `32` status `ready` deltaP `8.0277` edge `0.0672` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.3815` n `195` status `ready` deltaP `3.9024` edge `0.0975` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2009` n `30` status `ready` deltaP `7.5` edge `0.0114` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2341` n `195` status `ready` deltaP `2.1833` edge `0.0` maxDD `-0.5659`
- `news_risk_high->crypto_major_24h` score `-0.2452` n `30` status `ready` deltaP `10.7291` edge `-0.025` maxDD `-4.2368`
- `market_context_high->unknown_4h` score `-0.3605` n `195` status `ready` deltaP `-2.6118` edge `0.2406` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `-0.5875` n `30` status `ready` deltaP `14.0973` edge `-0.1224` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6148` n `195` status `ready` deltaP `3.6945` edge `0.0153` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7727` n `195` status `ready` deltaP `-2.2885` edge `-0.0045` maxDD `-0.5708`
- `market_context_high->metal_24h` score `-0.7869` n `195` status `ready` deltaP `16.2099` edge `0.0479` maxDD `-11.8809`
- `news_risk_high->metal_1h` score `-0.7979` n `32` status `ready` deltaP `-3.4431` edge `-0.0296` maxDD `-1.6464`
- `market_context_high->equity_1h` score `-0.8531` n `195` status `ready` deltaP `-1.1577` edge `0.0099` maxDD `-4.2573`
- `market_context_high->metal_1h` score `-0.8619` n `195` status `ready` deltaP `1.9415` edge `-0.0049` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9943` n `195` status `ready` deltaP `3.0117` edge `0.0277` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
