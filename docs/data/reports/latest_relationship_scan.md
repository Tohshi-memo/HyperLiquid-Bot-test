# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T00:22:24.563560+00:00`
- Price records: `672`
- Market context records: `6337`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.3479` n `32` status `ready` deltaP `43.0556` edge `1.0067` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0884` n `32` status `ready` deltaP `50.6944` edge `0.1694` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3863` n `32` status `ready` deltaP `16.6667` edge `0.5292` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2167` n `32` status `ready` deltaP `43.9787` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.5128` n `32` status `ready` deltaP `31.0764` edge `0.1061` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3991` n `32` status `ready` deltaP `28.8922` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.517` n `32` status `ready` deltaP `14.7268` edge `0.143` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9618` n `32` status `ready` deltaP `11.9199` edge `0.09` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.489` n `196` status `ready` deltaP `11.8654` edge `0.0413` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0507` n `196` status `ready` deltaP `6.4118` edge `0.0218` maxDD `-0.4926`
- `market_context_high->unknown_1h` score `-0.0691` n `207` status `ready` deltaP `-8.1822` edge `0.1496` maxDD `-3.7317`
- `market_context_high->metal_1h` score `-0.3617` n `207` status `ready` deltaP `4.3782` edge `0.0022` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.4921` n `140` status `ready` deltaP `16.4633` edge `0.084` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.5843` n `207` status `ready` deltaP `-0.99` edge `0.0` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5944` n `207` status `ready` deltaP `-2.8884` edge `0.0025` maxDD `-0.7564`
- `news_risk_high->index_24h` score `-0.6776` n `32` status `ready` deltaP `0.8681` edge `-0.0055` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.7335` n `32` status `ready` deltaP `5.7822` edge `-0.0652` maxDD `-0.7581`
- `market_context_high->fx_1h` score `-0.7579` n `207` status `ready` deltaP `-1.1803` edge `-0.0019` maxDD `-0.9376`
- `market_context_high->equity_4h` score `-0.7618` n `196` status `ready` deltaP `4.2466` edge `0.0439` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.7706` n `32` status `ready` deltaP `-3.5928` edge `-0.0251` maxDD `-1.6464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
