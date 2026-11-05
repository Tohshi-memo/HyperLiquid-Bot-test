# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T08:52:24.607755+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3930`

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

- `news_risk_high->crypto_alt_4h` score `-0.378` n `146` status `ready` deltaP `6.2375` edge `0.1736` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.643` n `146` status `ready` deltaP `1.8825` edge `0.0278` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.716` n `146` status `ready` deltaP `-2.8217` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7693` n `146` status `ready` deltaP `2.5449` edge `-0.0011` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.5422` n `146` status `ready` deltaP `-8.9939` edge `-0.0126` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.543` n `146` status `ready` deltaP `-8.5411` edge `-0.0187` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.711` n `146` status `ready` deltaP `2.0611` edge `-0.003` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1682` n `146` status `ready` deltaP `-7.7291` edge `0.0075` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.416` n `146` status `ready` deltaP `-18.4908` edge `-0.0156` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5838` n `146` status `ready` deltaP `-6.1869` edge `-0.0224` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8874` n `146` status `ready` deltaP `-12.1628` edge `-0.0049` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.2326` n `146` status `ready` deltaP `-10.4933` edge `0.036` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.394` n `146` status `ready` deltaP `-7.4071` edge `-0.0609` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4824` n `146` status `ready` deltaP `-10.1967` edge `-0.0684` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.6463` n `146` status `ready` deltaP `-6.5957` edge `-0.1517` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.4239` n `146` status `ready` deltaP `-11.7921` edge `-0.1381` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.0808` n `146` status `ready` deltaP `-19.4696` edge `0.1158` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.6959` n `146` status `ready` deltaP `1.4513` edge `-0.0649` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.8378` n `146` status `ready` deltaP `9.9778` edge `0.2307` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.6081` n `146` status `ready` deltaP `5.1335` edge `-0.2076` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
