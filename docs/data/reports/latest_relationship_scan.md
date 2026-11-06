# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T00:37:28.679884+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.4256` n `146` status `ready` deltaP `7.0776` edge `0.1619` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5666` n `146` status `ready` deltaP `2.9304` edge `0.0306` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6554` n `146` status `ready` deltaP `3.2934` edge `0.0034` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.6965` n `146` status `ready` deltaP `-2.5223` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.3976` n `146` status `ready` deltaP `-6.4688` edge `-0.0109` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5384` n `146` status `ready` deltaP `-8.3914` edge `-0.0191` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6369` n `146` status `ready` deltaP `1.3699` edge `0.0111` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.314` n `146` status `ready` deltaP `-5.5881` edge `0.0082` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4462` n `146` status `ready` deltaP `-10.274` edge `0.0013` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.5613` n `146` status `ready` deltaP `-12.1628` edge `0.0369` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.663` n `146` status `ready` deltaP `-21.951` edge `-0.0242` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.9887` n `146` status `ready` deltaP `-5.7604` edge `-0.0381` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8704` n `146` status `ready` deltaP `-14.5358` edge `0.0098` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7024` n `146` status `ready` deltaP `-12.5571` edge `-0.071` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.338` n `146` status `ready` deltaP `-9.5891` edge `-0.0623` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.0728` n `146` status `ready` deltaP `-16.9763` edge `-0.2847` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.2913` n `146` status `ready` deltaP `-14.6253` edge `0.1493` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.3983` n `146` status `ready` deltaP `2.1309` edge `0.0387` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.5758` n `146` status `ready` deltaP `9.9778` edge `0.4192` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.7967` n `146` status `ready` deltaP `3.5764` edge `-0.2214` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
