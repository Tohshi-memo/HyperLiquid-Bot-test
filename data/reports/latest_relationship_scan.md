# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T08:07:48.420339+00:00`
- Price records: `672`
- Market context records: `6167`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.687` n `32` status `ready` deltaP `42.7191` edge `0.7872` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.3769` n `32` status `ready` deltaP `64.7766` edge `0.1829` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1107` n `32` status `ready` deltaP `42.8186` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3532` n `32` status `ready` deltaP `28.3632` edge `0.0209` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6948` n `195` status `ready` deltaP `0.8923` edge `0.2361` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.5174` n `32` status `ready` deltaP `16.1405` edge `0.1649` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.1773` n `32` status `ready` deltaP `12.7102` edge `0.1129` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5887` n `32` status `ready` deltaP `7.955` edge `0.0686` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.2826` n `195` status `ready` deltaP `-0.9783` edge `0.2833` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.1899` n `195` status `ready` deltaP `20.9833` edge `0.1413` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.0147` n `32` status `ready` deltaP `10.0301` edge `0.0184` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.104` n `195` status `ready` deltaP `2.6626` edge `0.0653` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.3006` n `195` status `ready` deltaP `1.0555` edge `-0.001` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6335` n `195` status `ready` deltaP `3.814` edge `0.0121` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7353` n `195` status `ready` deltaP `-1.911` edge `-0.0039` maxDD `-0.5708`
- `news_risk_high->commodity_24h` score `-0.7979` n `32` status `ready` deltaP `12.0382` edge `-0.1262` maxDD `-0.3101`
- `news_risk_high->metal_1h` score `-0.8078` n `32` status `ready` deltaP `-3.5127` edge `-0.0304` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8771` n `195` status `ready` deltaP `1.8719` edge `-0.0057` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9872` n `195` status `ready` deltaP `2.939` edge `0.0291` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.0022` n `195` status `ready` deltaP `-2.7205` edge `0.0012` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
