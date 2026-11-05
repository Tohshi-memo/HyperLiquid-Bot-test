# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T12:52:29.534503+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3787`

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

- `news_risk_high->crypto_alt_4h` score `0.031` n `146` status `ready` deltaP `7.457` edge `0.2179` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4536` n `146` status `ready` deltaP `3.3795` edge `0.0421` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7238` n `146` status `ready` deltaP `-2.9714` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7418` n `146` status `ready` deltaP `2.8443` edge `-0.0008` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4512` n `146` status `ready` deltaP `-7.4695` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5672` n `146` status `ready` deltaP `-8.8405` edge `-0.0198` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7782` n `146` status `ready` deltaP `0.994` edge `-0.0045` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2766` n `146` status `ready` deltaP `-16.2909` edge `-0.0124` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3551` n `146` status `ready` deltaP `-9.3758` edge `0.0029` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.4997` n `146` status `ready` deltaP `-5.2887` edge `-0.0176` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9363` n `146` status `ready` deltaP `-12.3382` edge `-0.01` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.1026` n `146` status `ready` deltaP `-6.0598` edge `-0.0456` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6593` n `146` status `ready` deltaP `-12.9323` edge `0.0167` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6573` n `146` status `ready` deltaP `-11.8735` edge `-0.0718` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.7219` n `146` status `ready` deltaP `-10.8775` edge `-0.0857` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.2639` n `146` status `ready` deltaP `-9.2299` edge `-0.1856` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.4033` n `146` status `ready` deltaP `-16.7903` edge `0.1544` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.5369` n `146` status `ready` deltaP `1.9086` edge `-0.0547` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.1684` n `146` status `ready` deltaP `9.8198` edge `0.2042` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.5672` n `146` status `ready` deltaP `2.8753` edge `-0.3155` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
