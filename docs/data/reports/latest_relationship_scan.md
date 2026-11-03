# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T16:52:46.375819+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4374`

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

- `news_risk_high->crypto_alt_4h` score `0.2488` n `146` status `ready` deltaP `6.8472` edge `0.2499` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4581` n `146` status `ready` deltaP `1.8825` edge `0.0515` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6794` n `146` status `ready` deltaP `-2.0732` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9107` n `146` status `ready` deltaP `1.0479` edge `-0.0029` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.17` n `146` status `ready` deltaP `-3.1519` edge `-0.0068` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4303` n `146` status `ready` deltaP `-6.7073` edge `-0.0135` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.6874` n `146` status `ready` deltaP `11.9506` edge `0.1379` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.822` n `146` status `ready` deltaP `0.8562` edge `0.0449` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0634` n `146` status `ready` deltaP `-3.4268` edge `-0.0116` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2966` n `146` status `ready` deltaP `-16.4645` edge `-0.0138` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5229` n `146` status `ready` deltaP `-10.5734` edge `-0.0031` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6836` n `146` status `ready` deltaP `-6.9354` edge `-0.0302` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2199` n `146` status `ready` deltaP `-8.1556` edge `-0.0414` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1167` n `146` status `ready` deltaP `-14.914` edge `-0.0082` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4672` n `146` status `ready` deltaP `-4.5565` edge `-0.0214` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.7454` n `146` status `ready` deltaP `22.8406` edge `0.8106` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.9188` n `146` status `ready` deltaP `-13.7738` edge `-0.0828` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.1815` n `146` status `ready` deltaP `18.3267` edge `0.6464` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.4038` n `146` status `ready` deltaP `-1.2926` edge `-0.1056` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2676` n `146` status `ready` deltaP `-20.089` edge `-0.0623` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
