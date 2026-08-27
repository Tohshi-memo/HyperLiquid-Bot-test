# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T21:37:28.055519+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.2522` n `50` status `ready` deltaP `11.6319` edge `4.2768` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.527` n `50` status `ready` deltaP `37.8403` edge `1.6691` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7378` n `50` status `ready` deltaP `25.0976` edge `0.9041` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.8748` n `50` status `ready` deltaP `46.0903` edge `0.1032` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.5374` n `50` status `ready` deltaP `26.0139` edge `0.2975` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8663` n `50` status `ready` deltaP `45.0488` edge `0.0309` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `2.9552` n `50` status `ready` deltaP `16.2275` edge `0.1737` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.8278` n `128` status `ready` deltaP `5.3819` edge `0.273` maxDD `-3.1917`
- `news_risk_high->index_24h` score `2.6438` n `50` status `ready` deltaP `30.0139` edge `0.0353` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2948` n `148` status `ready` deltaP `18.2598` edge `0.1102` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5444` n `50` status `ready` deltaP `20.6527` edge `0.008` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2026` n `50` status `ready` deltaP `17.1138` edge `0.014` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `0.8749` n `50` status `ready` deltaP `19.2927` edge `0.0206` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8318` n `148` status `ready` deltaP `8.5248` edge `0.0575` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5237` n `50` status `ready` deltaP `14.4491` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1211` n `50` status `ready` deltaP `7.3593` edge `0.0004` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0703` n `50` status `ready` deltaP `4.9521` edge `-0.0014` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.1123` n `50` status `ready` deltaP `7.4634` edge `-0.006` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1171` n `50` status `ready` deltaP `4.7988` edge `-0.0021` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4542` n `148` status `ready` deltaP `6.3283` edge `-0.0087` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
