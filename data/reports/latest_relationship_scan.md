# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T10:37:24.390332+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4448`

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

- `news_risk_high->crypto_alt_4h` score `0.3148` n `146` status `ready` deltaP `6.3899` edge `0.2614` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4628` n `146` status `ready` deltaP `1.7328` edge `0.0519` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6459` n `146` status `ready` deltaP `-1.4744` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9275` n `146` status `ready` deltaP `0.8982` edge `-0.0033` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2331` n `146` status `ready` deltaP `-4.1998` edge `-0.0079` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2736` n `146` status `ready` deltaP `-3.9634` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.0261` n `146` status `ready` deltaP `-2.6646` edge `-0.0119` maxDD `-4.0745`
- `news_risk_high->metal_24h` score `-2.1279` n `146` status `ready` deltaP `9.5201` edge `0.1174` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-2.2177` n `146` status `ready` deltaP `-3.4841` edge `0.0231` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.3802` n `146` status `ready` deltaP `-17.159` edge `-0.0199` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4774` n `146` status `ready` deltaP `-9.8249` edge `-0.0043` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.7124` n `146` status `ready` deltaP `-7.0851` edge `-0.0329` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.287` n `146` status `ready` deltaP `-8.7544` edge `-0.043` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1727` n `146` status `ready` deltaP `-14.6091` edge `-0.0149` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.5231` n `146` status `ready` deltaP `-5.1662` edge `-0.022` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.485` n `146` status `ready` deltaP `18.8476` edge `0.7424` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8478` n `146` status `ready` deltaP `-13.6214` edge `-0.0779` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-10.7836` n `146` status `ready` deltaP `13.9864` edge `0.4633` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.2818` n `146` status `ready` deltaP `-0.6828` edge `-0.0995` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-13.0024` n `146` status `ready` deltaP `-24.4292` edge `-0.0946` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
