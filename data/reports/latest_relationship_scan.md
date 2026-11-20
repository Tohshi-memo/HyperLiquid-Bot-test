# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T22:22:37.914745+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2736`

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

- `market_context_high->unknown_1h` score `10134.3029` n `126` status `ready` deltaP `1.4638` edge `844.5353` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6179.7561` n `126` status `ready` deltaP `-0.3145` edge `515.0123` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.5605` n `108` status `ready` deltaP `26.794` edge `1.0846` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.2038` n `126` status `ready` deltaP `3.8019` edge `0.015` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2563` n `126` status `ready` deltaP `3.607` edge `0.0043` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.4918` n `126` status `ready` deltaP `12.1007` edge `0.0369` maxDD `-10.1161`
- `market_context_high->crypto_alt_24h` score `-0.5335` n `108` status `ready` deltaP `13.8311` edge `0.8534` maxDD `-72.5383`
- `market_context_high->fx_1h` score `-1.4094` n `126` status `ready` deltaP `-8.9559` edge `-0.0018` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7975` n `126` status `ready` deltaP `5.8383` edge `0.0172` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9895` n `126` status `ready` deltaP `-7.9462` edge `-0.0005` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2344` n `126` status `ready` deltaP `-7.6229` edge `-0.0222` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.279` n `126` status `ready` deltaP `-2.1172` edge `-0.0125` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.4691` n `126` status `ready` deltaP `2.8585` edge `0.007` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1668` n `126` status `ready` deltaP `-3.2958` edge `-0.0142` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.226` n `126` status `ready` deltaP `0.721` edge `0.1463` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.705` n `108` status `ready` deltaP `12.963` edge `0.1275` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.8607` n `108` status `ready` deltaP `-19.9074` edge `-0.0117` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.98` n `126` status `ready` deltaP `-20.1873` edge `-0.0778` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.2566` n `126` status `ready` deltaP `1.1783` edge `0.0687` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.9972` n `108` status `ready` deltaP `-26.3888` edge `-0.1442` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
