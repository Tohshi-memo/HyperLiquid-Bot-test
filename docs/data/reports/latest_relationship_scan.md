# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T06:37:32.801476+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `10686.7122` n `117` status `ready` deltaP `1.2705` edge `890.5707` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6558.8336` n `117` status `ready` deltaP `-1.2299` edge `546.6082` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1232` n `117` status `ready` deltaP `5.6234` edge `0.0132` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3009` n `117` status `ready` deltaP `3.0785` edge `0.0031` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9362` n `117` status `ready` deltaP `6.8245` edge `0.0151` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.5149` n `117` status `ready` deltaP `-10.9154` edge `-0.0017` maxDD `-0.4752`
- `market_context_high->crypto_major_1h` score `-1.6143` n `117` status `ready` deltaP `2.2238` edge `-0.0108` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.7263` n `117` status `ready` deltaP `-3.4319` edge `0.002` maxDD `-1.7019`
- `market_context_high->equity_1h` score `-1.7625` n `117` status `ready` deltaP `6.5408` edge `0.0071` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4641` n `117` status `ready` deltaP `-10.1477` edge `-0.0246` maxDD `-4.3803`
- `market_context_high->index_4h` score `-2.8404` n `117` status `ready` deltaP `-7.635` edge `-0.0225` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.6601` n `117` status `ready` deltaP `-6.3668` edge `-0.0515` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-5.4639` n `117` status `ready` deltaP `-7.5054` edge `-0.0015` maxDD `-6.6366`
- `market_context_high->crypto_major_4h` score `-5.6415` n `117` status `ready` deltaP `-3.8514` edge `-0.0047` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-6.1984` n `117` status `ready` deltaP `-4.0038` edge `-0.0867` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.8675` n `117` status `ready` deltaP `-18.2666` edge `-0.0837` maxDD `-15.3451`
- `market_context_high->metal_24h` score `-8.9377` n `117` status `ready` deltaP `-0.9616` edge `0.0712` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-13.9385` n `117` status `ready` deltaP `10.9375` edge `0.2001` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.4788` n `117` status `ready` deltaP `-30.0614` edge `-0.1469` maxDD `-40.0741`
- `market_context_high->crypto_alt_24h` score `-16.4486` n `117` status `ready` deltaP `3.6324` edge `-0.0148` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
