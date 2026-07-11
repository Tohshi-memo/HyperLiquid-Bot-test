# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T16:52:28.636717+00:00`
- Price records: `672`
- Market context records: `6411`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11095`

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

- `news_risk_high->crypto_alt_24h` score `13.1382` n `32` status `ready` deltaP `33.8542` edge `0.8839` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6895` n `32` status `ready` deltaP `56.4236` edge `0.1813` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.2127` n `32` status `ready` deltaP `36.2847` edge `0.1297` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1789` n `32` status `ready` deltaP `43.5213` edge `0.0627` maxDD `-0.0345`
- `market_context_high->unknown_24h` score `4.1546` n `146` status `ready` deltaP `12.1267` edge `0.5954` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `3.9534` n `32` status `ready` deltaP `15.4514` edge `0.4818` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4841` n `32` status `ready` deltaP `29.9401` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4936` n `32` status `ready` deltaP `14.4274` edge `0.142` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.845` n `32` status `ready` deltaP `10.2732` edge `0.086` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.6576` n `208` status `ready` deltaP `-5.5475` edge `0.1926` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.3832` n `208` status `ready` deltaP `11.1984` edge `0.0411` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0809` n `208` status `ready` deltaP `7.8565` edge `0.022` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.286` n `32` status `ready` deltaP `6.2313` edge `-0.0309` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.4375` n `146` status `ready` deltaP `18.5978` edge `0.0964` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4665` n `208` status `ready` deltaP `2.3175` edge `0.0025` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6367` n `32` status `ready` deltaP `-1.0479` edge `-0.0249` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.6889` n `208` status `ready` deltaP `-0.3484` edge `-0.0017` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.6929` n `208` status `ready` deltaP `-2.7032` edge `-0.0025` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.7455` n `208` status `ready` deltaP `-3.9325` edge `0.0026` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.7549` n `32` status `ready` deltaP `0.5208` edge `-0.0131` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
