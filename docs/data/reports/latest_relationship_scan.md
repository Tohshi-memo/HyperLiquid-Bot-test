# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T05:37:25.020345+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4558`

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

- `news_risk_high->crypto_alt_4h` score `0.2183` n `146` status `ready` deltaP `5.7802` edge `0.2531` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4495` n `146` status `ready` deltaP `1.8825` edge `0.0526` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5953` n `146` status `ready` deltaP `-0.5762` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8609` n `130` status `ready` deltaP `12.4546` edge `0.1322` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9179` n `146` status `ready` deltaP `1.0479` edge `-0.0035` maxDD `-1.3981`
- `news_risk_high->crypto_alt_24h` score `-0.9644` n `130` status `ready` deltaP `22.2035` edge `0.8481` maxDD `-77.5812`
- `news_risk_high->fx_4h` score `-1.2087` n `146` status `ready` deltaP `-2.8963` edge `-0.0105` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.293` n `146` status `ready` deltaP `-5.098` edge `-0.0096` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-2.0661` n `130` status `ready` deltaP `17.3424` edge `0.629` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.0935` n `130` status `ready` deltaP `-2.2356` edge `0.0307` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1287` n `146` status `ready` deltaP `-4.0365` edge `-0.0159` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3888` n `146` status `ready` deltaP `-9.0764` edge `-0.0019` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4544` n `130` status `ready` deltaP `-18.9744` edge `-0.0173` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7031` n `146` status `ready` deltaP `-6.9354` edge `-0.0327` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2391` n `146` status `ready` deltaP `-8.3053` edge `-0.042` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.782` n `146` status `ready` deltaP `-12.1701` edge `0.0014` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8949` n `146` status `ready` deltaP `-7.7577` edge `-0.0357` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0454` n `146` status `ready` deltaP `-14.2312` edge `-0.0903` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.7241` n `130` status `ready` deltaP `-12.6602` edge `0.0664` maxDD `-51.3874`
- `news_risk_high->commodity_24h` score `-11.6446` n `130` status `ready` deltaP `-24.0278` edge `-0.0824` maxDD `-35.8908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
