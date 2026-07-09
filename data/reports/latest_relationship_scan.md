# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T23:22:27.096127+00:00`
- Price records: `672`
- Market context records: `6227`
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

- `news_risk_high->crypto_alt_24h` score `13.469` n `32` status `ready` deltaP `42.2194` edge `0.8557` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3778` n `32` status `ready` deltaP `54.7619` edge `0.1664` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1671` n `32` status `ready` deltaP `43.6738` edge `0.0607` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.7043` n `32` status `ready` deltaP `15.625` edge `0.3205` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3452` n `32` status `ready` deltaP `28.2934` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.0971` n `192` status `ready` deltaP `2.5605` edge `0.2585` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `1.5347` n `32` status `ready` deltaP `22.1301` edge `0.0009` maxDD `-0.3101`
- `news_risk_high->crypto_major_1h` score `1.3875` n `32` status `ready` deltaP `14.2777` edge `0.1294` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.0079` n `192` status `ready` deltaP `-0.9274` edge `0.3434` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7647` n `32` status `ready` deltaP `10.1235` edge `0.0767` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0501` n `192` status `ready` deltaP `19.8023` edge `0.1184` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2058` n `32` status `ready` deltaP `8.801` edge `0.0021` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2926` n `192` status `ready` deltaP `1.2101` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5679` n `192` status `ready` deltaP `-0.7485` edge `0.0023` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.5992` n `192` status `ready` deltaP `4.1286` edge `0.0144` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8135` n `32` status `ready` deltaP `-4.0419` edge `-0.0276` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.899` n `192` status `ready` deltaP `4.3943` edge `0.0307` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9107` n `192` status `ready` deltaP `1.1664` edge `-0.0038` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9121` n `192` status `ready` deltaP `4.3819` edge `0.0306` maxDD `-9.807`
- `market_context_high->equity_4h` score `-0.9182` n `192` status `ready` deltaP `1.9055` edge `0.0025` maxDD `-2.671`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
