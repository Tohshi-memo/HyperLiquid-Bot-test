# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T12:07:33.388344+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3781`

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

- `news_risk_high->crypto_alt_4h` score `-0.1317` n `146` status `ready` deltaP `6.9997` edge `0.2001` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5284` n `146` status `ready` deltaP `2.9304` edge `0.0355` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6981` n `146` status `ready` deltaP `-2.5223` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7705` n `146` status `ready` deltaP `2.5449` edge `-0.0012` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4536` n `146` status `ready` deltaP `-7.4695` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5944` n `146` status `ready` deltaP `-9.2896` edge `-0.0203` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.8059` n `146` status `ready` deltaP `0.5367` edge `-0.005` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2916` n `146` status `ready` deltaP `-8.9267` edge `0.0052` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.297` n `146` status `ready` deltaP `-16.6381` edge `-0.0127` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5581` n `146` status `ready` deltaP `-5.7378` edge `-0.0221` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9293` n `146` status `ready` deltaP `-12.3382` edge `-0.0091` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.2045` n `146` status `ready` deltaP `-6.5089` edge `-0.0511` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.5832` n `146` status `ready` deltaP `-12.475` edge `0.02` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6439` n `146` status `ready` deltaP `-11.7211` edge `-0.0717` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9469` n `146` status `ready` deltaP `-11.3348` edge `-0.1014` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.1382` n `146` status `ready` deltaP `-8.7091` edge `-0.1786` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.5242` n `146` status `ready` deltaP `-17.3112` edge `0.1478` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.6743` n `146` status `ready` deltaP `1.4513` edge `-0.0631` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.0868` n `146` status `ready` deltaP `9.8198` edge `0.211` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.4053` n `146` status `ready` deltaP `3.0489` edge `-0.2959` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
