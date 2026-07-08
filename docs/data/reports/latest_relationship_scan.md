# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T20:17:55.100746+00:00`
- Price records: `672`
- Market context records: `6120`
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

- `news_risk_high->crypto_alt_24h` score `9.7614` n `30` status `ready` deltaP `37.6041` edge `0.5775` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.8964` n `30` status `ready` deltaP `69.9653` edge `0.1916` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2665` n `32` status `ready` deltaP `44.436` edge `0.0639` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3787` n `32` status `ready` deltaP `28.5928` edge `0.0215` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2371` n `32` status `ready` deltaP `13.5292` edge `0.1151` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6933` n `195` status `ready` deltaP `5.5793` edge `0.1123` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.6346` n `32` status `ready` deltaP `8.6265` edge `0.07` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0488` n `30` status `ready` deltaP `8.7152` edge `0.0228` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.284` n `195` status `ready` deltaP `1.2851` edge `-0.0004` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.4999` n `30` status `ready` deltaP `14.0973` edge `-0.1151` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.7208` n `195` status `ready` deltaP `2.7799` edge `0.0078` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7296` n `195` status `ready` deltaP `-1.8394` edge `-0.0039` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.7752` n `195` status `ready` deltaP `-0.2595` edge `0.0139` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.8081` n `32` status `ready` deltaP `-3.4431` edge `-0.0309` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8775` n `195` status `ready` deltaP `1.9415` edge `-0.0062` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9413` n `195` status `ready` deltaP `3.6105` edge `0.0305` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9609` n `195` status `ready` deltaP `4.3145` edge `0.0248` maxDD `-9.807`
- `market_context_high->index_4h` score `-0.9823` n `195` status `ready` deltaP `0.4792` edge `0.0173` maxDD `-1.381`
- `news_risk_high->index_1h` score `-1.163` n `32` status `ready` deltaP `-10.7223` edge `-0.0213` maxDD `-1.1725`
- `market_context_high->metal_24h` score `-1.3034` n `195` status `ready` deltaP `13.4322` edge `0.0002` maxDD `-11.8809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
