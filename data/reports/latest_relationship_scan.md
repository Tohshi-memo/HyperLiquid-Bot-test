# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T23:52:30.570553+00:00`
- Price records: `672`
- Market context records: `8247`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `7957.5053` n `43` status `ready` deltaP `38.5417` edge `662.8685` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.3748` n `54` status `ready` deltaP `27.1454` edge `0.4933` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.2009` n `54` status `ready` deltaP `22.5771` edge `0.1471` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7821` n `54` status `ready` deltaP `23.6393` edge `0.0933` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3747` n `54` status `ready` deltaP `12.0032` edge `0.2938` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8075` n `54` status `ready` deltaP `14.5542` edge `0.097` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7253` n `54` status `ready` deltaP `11.3551` edge `0.1078` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3773` n `54` status `ready` deltaP `17.0789` edge `0.2019` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.116` n `54` status `ready` deltaP `10.3489` edge `0.0708` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4974` n `54` status `ready` deltaP `7.352` edge `0.0213` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1829` n `54` status `ready` deltaP `7.2965` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1096` n `54` status `ready` deltaP `3.1049` edge `0.0105` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4666` n `54` status `ready` deltaP `4.4602` edge `0.0062` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1696` n `54` status `ready` deltaP `-8.8102` edge `-0.0435` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.0864` n `43` status `ready` deltaP `-18.6491` edge `-0.0446` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.7253` n `43` status `ready` deltaP `-20.5992` edge `-0.0883` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-8.9599` n `54` status `ready` deltaP `-32.7913` edge `-0.1973` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6503` n `43` status `ready` deltaP `-23.9624` edge `-0.3533` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-14.195` n `43` status `ready` deltaP `-19.3071` edge `-0.4711` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.114` n `43` status `ready` deltaP `-23.4415` edge `-1.2076` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
