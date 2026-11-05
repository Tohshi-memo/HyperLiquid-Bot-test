# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T23:07:27.566930+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4319`

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

- `news_risk_high->crypto_alt_4h` score `-0.4015` n `146` status `ready` deltaP `6.9997` edge `0.1655` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4567` n `146` status `ready` deltaP `3.2298` edge `0.0427` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.653` n `146` status `ready` deltaP `3.2934` edge `0.0036` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6957` n `146` status `ready` deltaP `-2.5223` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.41` n `146` status `ready` deltaP `-6.7073` edge `-0.0109` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5096` n `146` status `ready` deltaP `-7.9423` edge `-0.0184` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6397` n `146` status `ready` deltaP `1.4513` edge `0.0102` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.3015` n `146` status `ready` deltaP `-5.4384` edge `0.0088` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4737` n `146` status `ready` deltaP `-10.5734` edge `0.001` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.6012` n `146` status `ready` deltaP `-21.0323` edge `-0.0224` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.6494` n `146` status `ready` deltaP `-12.2504` edge `0.0262` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-2.8483` n `146` status `ready` deltaP `-5.461` edge `-0.0284` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8677` n `146` status `ready` deltaP `-14.4567` edge `0.0095` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6869` n `146` status `ready` deltaP `-12.4833` edge `-0.0702` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.3617` n `146` status `ready` deltaP `-9.8104` edge `-0.0628` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.9158` n `146` status `ready` deltaP `-16.2294` edge `-0.2766` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.1643` n `146` status `ready` deltaP `-14.4928` edge `0.159` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.4841` n `146` status `ready` deltaP `2.2135` edge `0.031` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-12.3357` n `146` status `ready` deltaP `9.8989` edge `0.3564` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.3831` n `146` status `ready` deltaP `2.6199` edge `-0.2902` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
