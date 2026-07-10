# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T02:22:28.567928+00:00`
- Price records: `672`
- Market context records: `6240`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `14.0486` n `32` status `ready` deltaP `42.2194` edge `0.904` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1957` n `32` status `ready` deltaP `52.8912` edge `0.1637` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2011` n `32` status `ready` deltaP `43.9787` edge `0.0615` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.1505` n `32` status `ready` deltaP `15.625` edge `0.3777` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3236` n `32` status `ready` deltaP `27.994` edge `0.0209` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2579` n `192` status `ready` deltaP `2.4108` edge `0.2729` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `1.986` n `32` status `ready` deltaP `24.1709` edge `0.0249` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.8796` n `192` status `ready` deltaP `0.4446` edge `0.4069` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.354` n `32` status `ready` deltaP `14.2777` edge `0.1251` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7623` n `32` status `ready` deltaP `10.5726` edge `0.0734` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0696` n `192` status `ready` deltaP `19.8023` edge `0.1159` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.173` n `32` status `ready` deltaP `8.801` edge `0.0063` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3066` n `192` status `ready` deltaP `0.9107` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5172` n `192` status `ready` deltaP `4.281` edge `0.0239` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.6709` n `192` status `ready` deltaP `-1.9461` edge `0.0017` maxDD `-0.5708`
- `market_context_high->equity_4h` score `-0.6904` n `192` status `ready` deltaP `2.6677` edge `0.0164` maxDD `-2.671`
- `news_risk_high->metal_1h` score `-0.7893` n `32` status `ready` deltaP `-3.5928` edge `-0.0275` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8736` n `192` status `ready` deltaP `1.6155` edge `-0.0037` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9014` n `192` status `ready` deltaP `4.8434` edge `0.0274` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9457` n `192` status `ready` deltaP `4.3819` edge `0.0263` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
