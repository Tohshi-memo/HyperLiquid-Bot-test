# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T23:36:18.835012+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0655` n `146` status `ready` deltaP `7.7619` edge `0.2035` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.487` n `146` status `ready` deltaP `2.631` edge `0.0428` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6973` n `146` status `ready` deltaP `-2.5223` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8496` n `146` status `ready` deltaP `1.7964` edge `-0.0028` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4231` n `146` status `ready` deltaP `-6.8944` edge `-0.0143` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5422` n `146` status `ready` deltaP `-8.9939` edge `-0.0126` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.95` n `146` status `ready` deltaP `-1.1402` edge `-0.0123` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2029` n `146` status `ready` deltaP `-8.1782` edge `0.0076` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4581` n `146` status `ready` deltaP `-18.8368` edge `-0.0187` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4609` n `146` status `ready` deltaP `-8.3566` edge `0.0244` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6235` n `146` status `ready` deltaP `-6.636` edge `-0.0245` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.2248` n `146` status `ready` deltaP `-10.036` edge `0.0336` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.2429` n `146` status `ready` deltaP `-6.958` edge `-0.0513` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.579` n `146` status `ready` deltaP `-0.1943` edge `-0.0221` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.0077` n `146` status `ready` deltaP `-6.843` edge `-0.0512` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.3497` n `146` status `ready` deltaP `-11.9446` edge `-0.1309` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-10.6553` n `146` status `ready` deltaP `11.5349` edge `0.2565` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.1558` n `146` status `ready` deltaP `-0.6828` edge `-0.089` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.5085` n `146` status `ready` deltaP `-20.6807` edge `0.0049` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-11.9887` n `146` status `ready` deltaP `11.8809` edge `0.3721` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
