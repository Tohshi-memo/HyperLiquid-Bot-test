# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T03:22:26.225598+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10302`

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

- `market_context_high->unknown_24h` score `414.4793` n `75` status `ready` deltaP `2.1944` edge `34.5394` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.3749` n `53` status `ready` deltaP `35.23` edge `2.867` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.1412` n `75` status `ready` deltaP `29.7708` edge `2.3008` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.875` n `75` status `ready` deltaP `47.5834` edge `1.3405` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.2079` n `53` status `ready` deltaP `42.0434` edge `1.866` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2234` n `53` status `ready` deltaP `36.2402` edge `0.8067` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.2757` n `53` status `ready` deltaP `41.6667` edge `0.2452` maxDD `0.0`
- `market_context_high->index_24h` score `5.5799` n `75` status `ready` deltaP `31.9861` edge `0.2609` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0661` n `53` status `ready` deltaP `48.2254` edge `0.1383` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.8989` n `53` status `ready` deltaP `29.9986` edge `0.2386` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.2175` n `75` status `ready` deltaP `41.3334` edge `0.3543` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `3.6666` n `53` status `ready` deltaP `20.8957` edge `0.315` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5936` n `53` status `ready` deltaP `18.9131` edge `0.2364` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9959` n `53` status `ready` deltaP `27.0162` edge `0.0949` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3176` n `53` status `ready` deltaP `27.0873` edge `0.038` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0446` n `53` status `ready` deltaP `20.7461` edge `0.0757` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9032` n `53` status `ready` deltaP `25.5838` edge `0.2373` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7629` n `53` status `ready` deltaP `14.4261` edge `0.5804` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2131` n `53` status `ready` deltaP `16.4275` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7114` n `53` status `ready` deltaP `18.0431` edge `0.0761` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
