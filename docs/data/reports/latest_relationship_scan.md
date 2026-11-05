# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T01:22:25.838957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `-0.3697` n `146` status `ready` deltaP `6.8472` edge `0.1706` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5135` n `146` status `ready` deltaP `2.4813` edge `0.0404` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7245` n `146` status `ready` deltaP `-2.9714` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7897` n `146` status `ready` deltaP `2.3952` edge `-0.0018` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4558` n `146` status `ready` deltaP `-7.3435` edge `-0.0155` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5627` n `146` status `ready` deltaP `-9.2988` edge `-0.0132` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9603` n `146` status `ready` deltaP `-1.2926` edge `-0.0126` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1298` n `146` status `ready` deltaP `-7.4297` edge `0.0087` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4406` n `146` status `ready` deltaP `-18.6638` edge `-0.0176` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.5539` n `146` status `ready` deltaP `-9.3947` edge `0.0194` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.5628` n `146` status `ready` deltaP `-6.0372` edge `-0.0207` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.2092` n `146` status `ready` deltaP `-10.036` edge `0.0349` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3436` n `146` status `ready` deltaP `-7.5568` edge `-0.0557` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.9603` n `146` status `ready` deltaP `-1.4054` edge `-0.0458` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.1217` n `146` status `ready` deltaP `-7.7577` edge `-0.0546` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.7362` n `146` status `ready` deltaP `-13.0116` edge `-0.156` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.2448` n `146` status `ready` deltaP `-0.8353` edge `-0.0954` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.2697` n `146` status `ready` deltaP `-20.6807` edge `0.0248` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-11.6098` n `146` status `ready` deltaP `10.3238` edge `0.1422` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-12.3607` n `146` status `ready` deltaP `11.8809` edge `0.3411` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
