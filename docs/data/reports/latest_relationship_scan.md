# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T14:52:28.767445+00:00`
- Price records: `672`
- Market context records: `5991`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11236`

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

- `news_risk_high->fx_24h` score `7.5275` n `30` status `ready` deltaP `68.9236` edge `0.1678` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.4161` n `30` status `ready` deltaP `33.3681` edge `0.1661` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1543` n `30` status `ready` deltaP `43.0488` edge `0.0638` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2418` n `30` status `ready` deltaP `26.9261` edge `0.0212` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1006` n `230` status `ready` deltaP `7.5385` edge `0.1509` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7858` n `30` status `ready` deltaP `9.8902` edge `0.0815` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1919` n `30` status `ready` deltaP `5.3194` edge `0.0353` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0867` n `30` status `ready` deltaP `9.2361` edge `0.0367` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.3871` n `230` status `ready` deltaP `3.9625` edge `0.0368` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.4118` n `30` status `ready` deltaP `1.5369` edge `-0.0264` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.5168` n `230` status `ready` deltaP `2.1166` edge `-0.0005` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.5796` n `203` status `ready` deltaP `22.4377` edge `0.3389` maxDD `-31.2762`
- `market_context_high->commodity_1h` score `-0.6237` n `230` status `ready` deltaP `-0.8552` edge `0.0021` maxDD `-0.8698`
- `market_context_high->fx_1h` score `-0.8078` n `230` status `ready` deltaP `-2.0594` edge `-0.0019` maxDD `-0.8015`
- `news_risk_high->index_1h` score `-1.0353` n `30` status `ready` deltaP `-9.4012` edge `-0.0186` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.093` n `230` status `ready` deltaP `2.6439` edge `0.019` maxDD `-9.807`
- `market_context_high->commodity_4h` score `-1.1292` n `230` status `ready` deltaP `-0.3168` edge `-0.0007` maxDD `-4.0228`
- `market_context_high->index_1h` score `-1.1454` n `230` status `ready` deltaP `-1.1403` edge `0.0035` maxDD `-1.3078`
- `market_context_high->crypto_alt_1h` score `-1.1758` n `230` status `ready` deltaP `1.6962` edge `0.0132` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.1923` n `230` status `ready` deltaP `0.0848` edge `0.0153` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
