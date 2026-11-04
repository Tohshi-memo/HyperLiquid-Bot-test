# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T23:22:26.156504+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0225` n `146` status `ready` deltaP `7.9143` edge `0.208` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5018` n `146` status `ready` deltaP `2.4813` edge `0.0419` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6887` n `146` status `ready` deltaP `-2.3726` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8628` n `146` status `ready` deltaP `1.6467` edge `-0.0029` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4231` n `146` status `ready` deltaP `-6.8944` edge `-0.0143` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5327` n `146` status `ready` deltaP `-8.8415` edge `-0.0124` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9405` n `146` status `ready` deltaP `-0.9877` edge `-0.0121` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2017` n `146` status `ready` deltaP `-8.1782` edge `0.0077` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.4472` n `146` status `ready` deltaP `-8.1836` edge `0.025` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4589` n `146` status `ready` deltaP `-18.8368` edge `-0.0188` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.636` n `146` status `ready` deltaP `-6.7857` edge `-0.0251` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.2248` n `146` status `ready` deltaP `-10.036` edge `0.0336` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.2597` n `146` status `ready` deltaP `-7.1077` edge `-0.0517` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.5268` n `146` status `ready` deltaP `-0.0213` edge `-0.0189` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.9907` n `146` status `ready` deltaP `-6.6906` edge `-0.0508` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.2979` n `146` status `ready` deltaP `-11.7921` edge `-0.1276` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-10.5441` n `146` status `ready` deltaP `11.7079` edge `0.2696` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-11.122` n `146` status `ready` deltaP `-0.5304` edge `-0.0872` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.5397` n `146` status `ready` deltaP `-20.6807` edge `0.0023` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-11.9503` n `146` status `ready` deltaP `11.8809` edge `0.3753` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
