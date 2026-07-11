# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T15:07:25.048211+00:00`
- Price records: `672`
- Market context records: `6402`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11091`

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

- `news_risk_high->crypto_alt_24h` score `13.5042` n `32` status `ready` deltaP `35.0694` edge `0.9063` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6708` n `32` status `ready` deltaP `56.25` edge `0.1809` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3236` n `32` status `ready` deltaP `37.3264` edge `0.132` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.1048` n `32` status `ready` deltaP `16.6667` edge `0.4931` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.0876` n `32` status `ready` deltaP `42.4543` edge `0.0622` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4458` n `32` status `ready` deltaP `29.491` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_24h` score `1.9678` n `146` status `ready` deltaP `8.5473` edge `0.4567` maxDD `-16.6425`
- `news_risk_high->crypto_major_1h` score `1.4289` n `32` status `ready` deltaP `13.6789` edge `0.1387` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8232` n `32` status `ready` deltaP `10.1235` edge `0.0842` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.4917` n `215` status `ready` deltaP `-5.4024` edge `0.1778` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.387` n `215` status `ready` deltaP `11.3053` edge `0.0407` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0314` n `215` status `ready` deltaP `7.3575` edge `0.0212` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2453` n `32` status `ready` deltaP `6.5307` edge `-0.0295` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3281` n `146` status `ready` deltaP `19.6205` edge `0.0987` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4671` n `215` status `ready` deltaP `2.2908` edge `0.0026` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5153` n `215` status `ready` deltaP `8.0573` edge `0.0501` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.6453` n `32` status `ready` deltaP `-1.1976` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.7043` n `215` status `ready` deltaP `-3.1409` edge `0.0026` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7297` n `215` status `ready` deltaP `-0.8578` edge `-0.0017` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.7384` n `215` status `ready` deltaP `-3.4884` edge `-0.0031` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
