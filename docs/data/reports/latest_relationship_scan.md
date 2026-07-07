# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T03:22:24.776948+00:00`
- Price records: `672`
- Market context records: `5941`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `6.7684` n `30` status `ready` deltaP `61.8056` edge `0.152` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4872` n `30` status `ready` deltaP `39.2709` edge `0.216` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.6703` n `30` status `ready` deltaP `38.0183` edge `0.057` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.104` n `30` status `ready` deltaP `25.4291` edge `0.0197` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4797` n `221` status `ready` deltaP `10.4328` edge `0.1632` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8878` n `30` status `ready` deltaP `10.9381` edge `0.0876` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2247` n `30` status `ready` deltaP `5.4691` edge `0.0385` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.0873` n `223` status `ready` deltaP `6.1975` edge `0.0395` maxDD `-4.3608`
- `news_risk_high->index_24h` score `-0.2546` n `30` status `ready` deltaP `6.6319` edge `0.0103` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3205` n `223` status `ready` deltaP `3.66` edge `0.0016` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4227` n `30` status `ready` deltaP `1.8363` edge `-0.0298` maxDD `-1.2643`
- `market_context_high->index_1h` score `-0.5352` n `223` status `ready` deltaP `1.5695` edge `0.0057` maxDD `-0.7819`
- `market_context_high->commodity_1h` score `-0.5856` n `223` status `ready` deltaP `-3.0632` edge `-0.0031` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.7214` n `223` status `ready` deltaP `3.2102` edge `0.0287` maxDD `-7.0736`
- `market_context_high->fx_1h` score `-0.742` n `223` status `ready` deltaP `-1.7159` edge `-0.0009` maxDD `-0.6262`
- `market_context_high->crypto_alt_1h` score `-0.7431` n `223` status `ready` deltaP `2.6141` edge `0.025` maxDD `-7.0159`
- `market_context_high->equity_24h` score `-1.0603` n `213` status `ready` deltaP `18.0116` edge `0.2516` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0859` n `30` status `ready` deltaP `-10.0` edge `-0.0211` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.7021` n `221` status `ready` deltaP `-3.0136` edge `-0.0349` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.714` n `221` status `ready` deltaP `1.245` edge `0.0176` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
