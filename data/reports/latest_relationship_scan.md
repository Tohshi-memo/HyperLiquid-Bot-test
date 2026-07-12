# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T14:52:27.005501+00:00`
- Price records: `672`
- Market context records: `6509`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5884`

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

- `news_risk_high->crypto_alt_24h` score `13.2229` n `32` status `ready` deltaP `36.0377` edge `0.8764` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5032` n `32` status `ready` deltaP `53.8995` edge `0.1826` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3715` n `144` status `ready` deltaP `11.8934` edge `0.7817` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.9506` n `32` status `ready` deltaP `20.7377` edge `0.5744` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7937` n `38` status `ready` deltaP `40.2359` edge `0.0525` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.7014` n `180` status `ready` deltaP `-5.9215` edge `0.3547` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.4733` n `32` status `ready` deltaP `25.1029` edge `0.0593` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8071` n `38` status `ready` deltaP `22.6127` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.3681` n `144` status `ready` deltaP `12.9501` edge `0.2145` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5774` n `168` status `ready` deltaP `13.1025` edge `0.0284` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5644` n `38` status `ready` deltaP `5.0504` edge `0.0924` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.2957` n `168` status `ready` deltaP `9.4367` edge `0.1171` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.2752` n `168` status `ready` deltaP `-18.3` edge `0.3855` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0703` n `38` status `ready` deltaP `1.5837` edge `0.0494` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.3656` n `32` status `ready` deltaP `5.8167` edge `0.0015` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3893` n `168` status `ready` deltaP `9.3714` edge `0.0575` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4347` n `180` status `ready` deltaP `-0.2528` edge `-0.0019` maxDD `-0.8383`
- `market_context_high->crypto_alt_1h` score `-0.5041` n `180` status `ready` deltaP `6.7299` edge `0.0218` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.5106` n `180` status `ready` deltaP `0.9381` edge `-0.0034` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.5428` n `180` status `ready` deltaP `6.6001` edge `0.013` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
