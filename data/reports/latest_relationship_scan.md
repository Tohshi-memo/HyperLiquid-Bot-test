# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T04:22:31.577896+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4596`

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

- `news_risk_high->crypto_alt_24h` score `0.7722` n `126` status `ready` deltaP `23.3135` edge `0.8941` maxDD `-65.3749`
- `news_risk_high->crypto_alt_4h` score `0.1436` n `146` status `ready` deltaP `5.018` edge `0.2486` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4534` n `146` status `ready` deltaP `1.7328` edge `0.0531` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5868` n `146` status `ready` deltaP `-0.4265` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.7932` n `126` status `ready` deltaP `13.4425` edge `0.1343` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9167` n `146` status `ready` deltaP `1.0479` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2175` n `146` status `ready` deltaP `-3.0488` edge `-0.0106` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2915` n `146` status `ready` deltaP `-5.098` edge `-0.0094` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-1.4983` n `126` status `ready` deltaP `18.4524` edge `0.6944` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.027` n `126` status `ready` deltaP `-1.7362` edge `0.0359` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1492` n `146` status `ready` deltaP `-4.3414` edge `-0.0165` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3876` n `146` status `ready` deltaP `-9.0764` edge `-0.0018` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4798` n `126` status `ready` deltaP `-19.5685` edge `-0.0166` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7015` n `146` status `ready` deltaP `-6.9354` edge `-0.0325` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2091` n `146` status `ready` deltaP `-8.0059` edge `-0.0415` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7952` n `146` status `ready` deltaP `-12.1701` edge `0.0003` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9153` n `146` status `ready` deltaP `-7.7577` edge `-0.0374` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0912` n `146` status `ready` deltaP `-14.3836` edge `-0.0931` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-8.1877` n `126` status `ready` deltaP `-12.6736` edge `0.0832` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.1158` n `126` status `ready` deltaP `-24.5783` edge `-0.0736` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
