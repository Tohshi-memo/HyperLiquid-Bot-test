# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T04:37:29.877802+00:00`
- Price records: `672`
- Market context records: `6157`
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

- `news_risk_high->crypto_alt_24h` score `12.2916` n `30` status `ready` deltaP `42.7267` edge `0.7542` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.5874` n `30` status `ready` deltaP `66.8977` edge `0.1863` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2174` n `32` status `ready` deltaP `43.8975` edge `0.0634` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4214` n `32` status `ready` deltaP `29.1106` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.7127` n `195` status `ready` deltaP `1.1912` edge `0.2356` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2747` n `32` status `ready` deltaP `13.6071` edge `0.1194` maxDD `-2.0691`
- `news_risk_high->crypto_major_24h` score `0.8452` n `30` status `ready` deltaP `13.5933` edge `0.0957` maxDD `-4.2368`
- `news_risk_high->crypto_alt_1h` score `0.6798` n `32` status `ready` deltaP `8.8518` edge `0.0743` maxDD `-1.6923`
- `market_context_high->equity_4h` score `-0.0138` n `195` status `ready` deltaP `2.7702` edge `0.0721` maxDD `-2.671`
- `market_context_high->unknown_4h` score `-0.1364` n `195` status `ready` deltaP `-1.4612` edge `0.2516` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.1681` n `195` status `ready` deltaP `19.0632` edge `0.1082` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2339` n `30` status `ready` deltaP `7.4061` edge `0.0078` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2563` n `195` status `ready` deltaP `1.8029` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5607` n `195` status `ready` deltaP `4.3883` edge `0.0176` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6081` n `30` status `ready` deltaP `14.0497` edge `-0.1238` maxDD `-0.3101`
- `market_context_high->commodity_1h` score `-0.7425` n `195` status `ready` deltaP `-1.911` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7463` n `32` status `ready` deltaP `-2.7653` edge `-0.0275` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7825` n `195` status `ready` deltaP `2.6193` edge `-0.0028` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8799` n `195` status `ready` deltaP `-1.8237` edge `0.0109` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.8961` n `195` status `ready` deltaP `3.8358` edge `0.0348` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
