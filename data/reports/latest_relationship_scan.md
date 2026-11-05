# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T19:22:33.236344+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4230`

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

- `news_risk_high->crypto_alt_4h` score `0.5195` n `146` status `ready` deltaP `8.7519` edge `0.2719` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.2344` n `146` status `ready` deltaP `3.8286` edge `0.0672` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6303` n `146` status `ready` deltaP `3.5928` edge `0.0035` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7292` n `146` status `ready` deltaP `-3.1211` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4822` n `146` status `ready` deltaP `-7.9909` edge `-0.0116` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5579` n `146` status `ready` deltaP `-8.6908` edge `-0.0196` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6313` n `146` status `ready` deltaP `1.6743` edge `0.0098` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.1643` n `146` status `ready` deltaP `-4.5402` edge `0.0204` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4006` n `146` status `ready` deltaP `-9.8249` edge `0.0021` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4278` n `146` status `ready` deltaP `-18.4326` edge `-0.0175` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.6204` n `146` status `ready` deltaP `-4.8622` edge `-0.0134` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.8147` n `146` status `ready` deltaP `-12.2504` edge `0.005` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.7588` n `146` status `ready` deltaP `-13.4704` edge `0.012` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-5.6527` n `146` status `ready` deltaP `-9.4369` edge `-0.0062` maxDD `-24.1554`
- `news_risk_high->metal_4h` score `-5.6649` n `146` status `ready` deltaP `-12.2527` edge `-0.0699` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-8.3587` n `146` status `ready` deltaP `-13.6298` edge `-0.2475` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.9483` n `146` status `ready` deltaP `-14.4928` edge `0.177` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.0364` n `146` status `ready` deltaP `2.7397` edge `0.0648` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.5249` n `146` status `ready` deltaP `9.8989` edge `0.2573` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.9379` n `146` status `ready` deltaP `1.9266` edge `-0.3567` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
