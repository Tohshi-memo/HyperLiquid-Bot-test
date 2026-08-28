# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T13:07:33.332534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11609`

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

- `news_risk_high->unknown_24h` score `53.5837` n `50` status `ready` deltaP `11.6118` edge `4.3879` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.1679` n `50` status `ready` deltaP `41.4073` edge `2.3654` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.6778` n `54` status `ready` deltaP `24.9097` edge `0.8213` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4439` n `50` status `ready` deltaP `30.1005` edge `0.3458` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.6646` n `50` status `ready` deltaP `45.487` edge `0.0897` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9159` n `54` status `ready` deltaP `45.4889` edge `0.0321` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `3.3237` n `50` status `ready` deltaP `19.8752` edge `0.1938` maxDD `-2.6128`
- `market_context_high->metal_24h` score `2.5697` n `132` status `ready` deltaP `23.2446` edge `0.1611` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.515` n `50` status `ready` deltaP `28.5546` edge `0.0343` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.479` n `132` status `ready` deltaP `17.9232` edge `0.1278` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.122` n `56` status `ready` deltaP `12.5749` edge `0.1287` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `1.8777` n `132` status `ready` deltaP `5.5512` edge `0.1927` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.4935` n `56` status `ready` deltaP `20.092` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1111` n `56` status `ready` deltaP `15.601` edge `0.0191` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `1.0543` n `132` status `ready` deltaP `7.2719` edge `0.0844` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.9685` n `54` status `ready` deltaP `22.0924` edge `0.0532` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5287` n `56` status `ready` deltaP `14.2964` edge `0.0045` maxDD `-0.5618`
- `news_risk_high->metal_4h` score `0.4047` n `54` status `ready` deltaP `11.8112` edge `0.0081` maxDD `-0.249`
- `news_risk_high->metal_1h` score `0.3339` n `56` status `ready` deltaP `6.8435` edge `0.0048` maxDD `-0.1413`
- `news_risk_high->index_1h` score `0.0501` n `56` status `ready` deltaP `5.9346` edge `0.0008` maxDD `-0.0486`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
