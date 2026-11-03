# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T18:39:23.338002+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4500`

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

- `news_risk_high->crypto_alt_4h` score `0.259` n `146` status `ready` deltaP `6.8472` edge `0.2512` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4238` n `146` status `ready` deltaP `2.3316` edge `0.0529` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7043` n `146` status `ready` deltaP `-2.5223` edge `-0.0034` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9215` n `146` status `ready` deltaP `0.8982` edge `-0.0028` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.177` n `146` status `ready` deltaP `-3.3016` edge `-0.0067` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4849` n `146` status `ready` deltaP `-7.622` edge `-0.0144` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.6087` n `146` status `ready` deltaP `12.1242` edge `0.1433` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.748` n `146` status `ready` deltaP `1.7243` edge `0.0486` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0491` n `146` status `ready` deltaP `-3.1219` edge `-0.0118` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2786` n `146` status `ready` deltaP `-16.4645` edge `-0.0115` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5888` n `146` status `ready` deltaP `-11.3219` edge `-0.0036` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6921` n `146` status `ready` deltaP `-7.0851` edge `-0.0303` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2247` n `146` status `ready` deltaP `-8.1556` edge `-0.0418` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0875` n `146` status `ready` deltaP `-14.6091` edge `-0.0078` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3482` n `146` status `ready` deltaP `-3.4894` edge `-0.0186` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.8823` n `146` status `ready` deltaP `21.7989` edge `0.8` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.9744` n `146` status `ready` deltaP `-14.0787` edge `-0.0854` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-7.961` n `146` status `ready` deltaP `18.8476` edge `0.6613` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.5622` n `146` status `ready` deltaP `-2.2072` edge `-0.1127` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.1913` n `146` status `ready` deltaP `-19.9153` edge `-0.0571` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
