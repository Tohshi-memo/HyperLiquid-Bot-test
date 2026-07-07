# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T02:52:29.756835+00:00`
- Price records: `672`
- Market context records: `5939`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11219`

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

- `news_risk_high->fx_24h` score `6.7323` n `30` status `ready` deltaP `61.4583` edge `0.1513` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4992` n `30` status `ready` deltaP `39.2709` edge `0.217` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.6399` n `30` status `ready` deltaP `37.7134` edge `0.0565` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1016` n `30` status `ready` deltaP `25.4291` edge `0.0195` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4097` n `221` status `ready` deltaP `10.1279` edge `0.1594` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8878` n `30` status `ready` deltaP `10.9381` edge `0.0876` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.22` n `30` status `ready` deltaP `5.4691` edge `0.0379` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.0629` n `221` status `ready` deltaP `6.4419` edge `0.041` maxDD `-4.3608`
- `news_risk_high->index_24h` score `-0.2774` n `30` status `ready` deltaP `6.2847` edge `0.0097` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3054` n `221` status `ready` deltaP `3.8597` edge `0.0022` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4414` n `30` status `ready` deltaP `1.5369` edge `-0.0302` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.56` n `221` status `ready` deltaP `-2.6452` edge `-0.0026` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5713` n `221` status `ready` deltaP `3.7134` edge `0.0341` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6488` n `221` status `ready` deltaP `3.101` edge `0.0296` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.6985` n `221` status `ready` deltaP `-1.2979` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.8099` n `221` status `ready` deltaP `1.7368` edge `0.0057` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1046` n `30` status `ready` deltaP `-10.2994` edge `-0.0215` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.1182` n `213` status `ready` deltaP `17.6643` edge `0.2465` maxDD `-31.2762`
- `market_context_high->metal_4h` score `-1.7398` n `221` status `ready` deltaP `-3.3184` edge `-0.0377` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.7515` n `221` status `ready` deltaP `0.9401` edge `0.0165` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
