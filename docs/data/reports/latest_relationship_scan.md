# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T20:37:28.203309+00:00`
- Price records: `672`
- Market context records: `6122`
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

- `news_risk_high->crypto_alt_24h` score `9.8701` n `30` status `ready` deltaP `37.7777` edge `0.5854` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.8952` n `30` status `ready` deltaP `69.9653` edge `0.1915` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2811` n `32` status `ready` deltaP `44.5884` edge `0.0641` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3919` n `32` status `ready` deltaP `28.7425` edge `0.0216` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2581` n `32` status `ready` deltaP `13.6789` edge `0.1168` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6607` n `195` status `ready` deltaP `5.4268` edge `0.1106` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.6564` n `32` status `ready` deltaP `8.7762` edge `0.0718` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0535` n `30` status `ready` deltaP `8.7152` edge `0.0222` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2754` n `195` status `ready` deltaP `1.4348` edge `-0.0003` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.5083` n `30` status `ready` deltaP `14.0973` edge `-0.1158` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.7232` n `195` status `ready` deltaP `2.7799` edge `0.0075` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7332` n `195` status `ready` deltaP `-1.8394` edge `-0.0042` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.7627` n `195` status `ready` deltaP `-0.1098` edge `0.0145` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.8057` n `32` status `ready` deltaP `-3.4431` edge `-0.0306` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8739` n `195` status `ready` deltaP `1.9415` edge `-0.0059` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9195` n `195` status `ready` deltaP `3.7602` edge `0.0323` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9398` n `195` status `ready` deltaP `4.4642` edge `0.0265` maxDD `-9.807`
- `market_context_high->index_4h` score `-0.9933` n `195` status `ready` deltaP `0.3267` edge `0.0169` maxDD `-1.381`
- `news_risk_high->index_1h` score `-1.1537` n `32` status `ready` deltaP `-10.5726` edge `-0.0211` maxDD `-1.1725`
- `market_context_high->metal_24h` score `-1.2694` n `195` status `ready` deltaP `13.6058` edge `0.0034` maxDD `-11.8809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
