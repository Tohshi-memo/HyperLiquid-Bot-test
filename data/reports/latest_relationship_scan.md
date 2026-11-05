# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T12:37:28.411811+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0253` n `146` status `ready` deltaP `7.3046` edge `0.2117` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4801` n `146` status `ready` deltaP `3.2298` edge `0.0397` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7152` n `146` status `ready` deltaP `-2.8217` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7561` n `146` status `ready` deltaP `2.6946` edge `-0.001` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.452` n `146` status `ready` deltaP `-7.4695` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5758` n `146` status `ready` deltaP `-8.9902` edge `-0.0199` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7869` n `146` status `ready` deltaP `0.8415` edge `-0.0046` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2864` n `146` status `ready` deltaP `-16.4645` edge `-0.0125` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3359` n `146` status `ready` deltaP `-9.2261` edge `0.0035` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5215` n `146` status `ready` deltaP `-5.4384` edge `-0.0194` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9332` n `146` status `ready` deltaP `-12.3382` edge `-0.0096` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.1422` n `146` status `ready` deltaP `-6.2095` edge `-0.0479` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6364` n `146` status `ready` deltaP `-12.7799` edge `0.0176` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6439` n `146` status `ready` deltaP `-11.7211` edge `-0.0717` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.7977` n `146` status `ready` deltaP `-11.0299` edge `-0.091` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.2212` n `146` status `ready` deltaP `-9.0563` edge `-0.1832` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.446` n `146` status `ready` deltaP `-16.964` edge `0.152` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.5827` n `146` status `ready` deltaP `1.7562` edge `-0.0575` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.1348` n `146` status `ready` deltaP `9.8198` edge `0.207` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.5173` n `146` status `ready` deltaP `2.8753` edge `-0.3091` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
