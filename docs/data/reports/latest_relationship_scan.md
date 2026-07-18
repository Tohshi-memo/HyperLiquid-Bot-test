# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T17:07:25.503104+00:00`
- Price records: `672`
- Market context records: `7161`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->fx_4h` score `0.1206` n `158` status `ready` deltaP `11.4426` edge `0.0121` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.3718` n `168` status `ready` deltaP `2.2348` edge `0.0014` maxDD `-0.4495`
- `market_context_high->crypto_alt_1h` score `-0.5962` n `168` status `ready` deltaP `0.1568` edge `0.0264` maxDD `-5.9775`
- `market_context_high->unknown_1h` score `-0.5995` n `168` status `ready` deltaP `-1.6146` edge `0.025` maxDD `-1.4688`
- `market_context_high->crypto_major_1h` score `-0.6428` n `168` status `ready` deltaP `3.4253` edge `0.0358` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.66` n `168` status `ready` deltaP `-0.9196` edge `-0.0164` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7619` n `168` status `ready` deltaP `1.0764` edge `-0.0042` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.9657` n `168` status `ready` deltaP `-7.4031` edge `-0.005` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-2.0736` n `158` status `ready` deltaP `-6.3812` edge `0.0122` maxDD `-6.1736`
- `market_context_high->commodity_4h` score `-2.1335` n `158` status `ready` deltaP `-5.3488` edge `-0.0386` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9438` n `158` status `ready` deltaP `-10.5531` edge `-0.0122` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.579` n `168` status `ready` deltaP `-1.0016` edge `-0.0389` maxDD `-15.5469`
- `market_context_high->index_4h` score `-3.9487` n `158` status `ready` deltaP `-2.5278` edge `-0.0423` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4892` n `133` status `ready` deltaP `-13.4581` edge `-0.1535` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-4.8381` n `158` status `ready` deltaP `2.9793` edge `0.0123` maxDD `-25.1605`
- `market_context_high->fx_24h` score `-4.8457` n `133` status `ready` deltaP `-14.4893` edge `-0.0245` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.4544` n `158` status `ready` deltaP `-2.7265` edge `-0.0267` maxDD `-24.7723`
- `market_context_high->unknown_24h` score `-10.0745` n `133` status `ready` deltaP `-32.5293` edge `-0.108` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.7574` n `133` status `ready` deltaP `-32.1232` edge `-0.1975` maxDD `-40.7836`
- `market_context_high->equity_4h` score `-14.8453` n `158` status `ready` deltaP `-4.3667` edge `-0.212` maxDD `-66.6799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
