# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T16:22:32.212102+00:00`
- Price records: `672`
- Market context records: `6516`
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

- `news_risk_high->crypto_alt_24h` score `13.2463` n `32` status `ready` deltaP `36.211` edge `0.8772` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.5771` n `138` status `ready` deltaP `10.263` edge `0.8097` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5128` n `32` status `ready` deltaP `53.8995` edge `0.1834` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.9471` n `32` status `ready` deltaP `20.911` edge `0.5728` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7377` n `38` status `ready` deltaP `39.6261` edge `0.0519` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.7949` n `179` status `ready` deltaP `-5.2487` edge `0.358` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.3145` n `32` status `ready` deltaP `24.063` edge `0.053` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8167` n `38` status `ready` deltaP `22.7624` edge `0.0177` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.6874` n `138` status `ready` deltaP `15.0503` edge `0.2271` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5798` n `168` status `ready` deltaP `13.1025` edge `0.0286` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5551` n `38` status `ready` deltaP `4.9007` edge `0.0922` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.2981` n `168` status `ready` deltaP `9.4367` edge `0.1173` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.075` n `38` status `ready` deltaP `1.5837` edge `0.05` maxDD `-2.0756`
- `market_context_high->unknown_4h` score `0.0747` n `168` status `ready` deltaP `-20.0711` edge `0.3806` maxDD `-10.5788`
- `market_context_high->equity_4h` score `-0.3124` n `168` status `ready` deltaP `10.6997` edge `0.0585` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.3398` n `32` status `ready` deltaP `6.1633` edge `0.0025` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.4286` n `179` status `ready` deltaP `-0.4073` edge `-0.0015` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.4982` n `179` status `ready` deltaP `7.0527` edge `0.0204` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5325` n `179` status `ready` deltaP `6.7825` edge `0.0131` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5461` n `179` status `ready` deltaP `0.2685` edge `-0.0035` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
