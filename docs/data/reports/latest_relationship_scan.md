# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T08:22:23.284485+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2566`

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

- `market_context_high->unknown_1h` score `11499.6642` n `112` status `ready` deltaP `1.1175` edge `958.3177` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7491.1686` n `107` status `ready` deltaP `0.1454` edge `624.2915` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.4903` n `98` status `ready` deltaP `39.594` edge `1.6644` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.5667` n `98` status `ready` deltaP `22.7041` edge `1.4157` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2342` n `112` status `ready` deltaP `3.4431` edge `0.0135` maxDD `-2.6517`
- `market_context_high->metal_24h` score `-0.2701` n `98` status `ready` deltaP `15.3557` edge `0.1976` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.3551` n `107` status `ready` deltaP `12.9473` edge `0.0151` maxDD `-6.1475`
- `market_context_high->crypto_major_4h` score `-0.4492` n `107` status `ready` deltaP `0.0228` edge `0.3005` maxDD `-22.3259`
- `market_context_high->crypto_alt_4h` score `-0.6497` n `107` status `ready` deltaP `1.2622` edge `0.1893` maxDD `-17.1476`
- `market_context_high->crypto_major_1h` score `-0.8062` n `112` status `ready` deltaP `2.8443` edge `0.0644` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.8299` n `112` status `ready` deltaP `-1.62` edge `0.0031` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0377` n `112` status `ready` deltaP `-1.6253` edge `0.0281` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3806` n `112` status `ready` deltaP `-8.9019` edge `-0.0008` maxDD `-0.392`
- `market_context_high->index_4h` score `-2.1984` n `107` status `ready` deltaP `-6.1146` edge `-0.0081` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.5331` n `112` status `ready` deltaP `-11.4414` edge `-0.027` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.742` n `112` status `ready` deltaP `1.5077` edge `-0.0208` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-3.9803` n `107` status `ready` deltaP `-18.1787` edge `-0.0062` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.6311` n `98` status `ready` deltaP `-17.7721` edge `-0.0032` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2826` n `107` status `ready` deltaP `-22.4071` edge `-0.0981` maxDD `-14.7522`
- `market_context_high->index_24h` score `-9.1491` n `98` status `ready` deltaP `-16.7694` edge `-0.1084` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
