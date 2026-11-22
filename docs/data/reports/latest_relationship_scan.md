# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T06:52:25.403089+00:00`
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

- `market_context_high->unknown_1h` score `10787.1463` n `116` status `ready` deltaP `1.1821` edge `898.9408` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6631.3737` n `116` status `ready` deltaP `-1.3036` edge `552.6537` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.108` n `116` status `ready` deltaP `5.9157` edge `0.0132` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2788` n `116` status `ready` deltaP `3.3708` edge `0.003` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9633` n `116` status `ready` deltaP `6.5129` edge `0.0137` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4406` n `116` status `ready` deltaP `-10.6133` edge `-0.0017` maxDD `-0.4743`
- `market_context_high->crypto_major_1h` score `-1.5745` n `116` status `ready` deltaP `2.5088` edge `-0.0076` maxDD `-13.8788`
- `market_context_high->fx_4h` score `-1.7153` n `116` status `ready` deltaP `-3.2748` edge `0.0021` maxDD `-1.6808`
- `market_context_high->equity_1h` score `-1.7374` n `116` status `ready` deltaP `6.8552` edge `0.0071` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4987` n `116` status `ready` deltaP `-10.5358` edge `-0.0249` maxDD `-4.3803`
- `market_context_high->index_4h` score `-2.876` n `116` status `ready` deltaP `-8.0057` edge `-0.023` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.6426` n `116` status `ready` deltaP `-6.1481` edge `-0.0515` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-5.409` n `116` status `ready` deltaP `-7.5611` edge `-0.0016` maxDD `-6.5662`
- `market_context_high->crypto_major_4h` score `-5.7096` n `116` status `ready` deltaP `-4.2` edge `-0.0111` maxDD `-47.4317`
- `market_context_high->crypto_alt_4h` score `-6.2594` n `116` status `ready` deltaP `-4.3524` edge `-0.0922` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.8456` n `116` status `ready` deltaP `-18.0824` edge `-0.0841` maxDD `-15.2657`
- `market_context_high->metal_24h` score `-9.0302` n `116` status `ready` deltaP `-1.5026` edge `0.0671` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-13.9913` n `116` status `ready` deltaP `11.2428` edge `0.1913` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.515` n `116` status `ready` deltaP `-30.2203` edge `-0.1496` maxDD `-40.0143`
- `market_context_high->crypto_alt_24h` score `-16.4982` n `116` status `ready` deltaP `3.8494` edge `-0.0226` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
