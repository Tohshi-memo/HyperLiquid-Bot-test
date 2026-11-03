# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T03:07:27.946829+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4836`

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

- `news_risk_high->crypto_alt_24h` score `0.3223` n `126` status `ready` deltaP `22.4454` edge `0.8422` maxDD `-65.3749`
- `news_risk_high->crypto_alt_4h` score `0.0353` n `146` status `ready` deltaP `4.2558` edge `0.2398` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4791` n `146` status `ready` deltaP `1.4334` edge `0.0518` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5541` n `146` status `ready` deltaP `0.1723` edge `-0.0021` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8578` n `126` status `ready` deltaP `12.5744` edge `0.1318` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9466` n `146` status `ready` deltaP `0.7485` edge `-0.0039` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2285` n `146` status `ready` deltaP `-3.2012` edge `-0.011` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3055` n `146` status `ready` deltaP `-5.2477` edge `-0.0102` maxDD `-3.1082`
- `news_risk_high->equity_24h` score `-2.0278` n `126` status `ready` deltaP `17.5843` edge `0.6323` maxDD `-67.0937`
- `news_risk_high->index_24h` score `-2.1251` n `126` status `ready` deltaP `-2.6042` edge `0.0291` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1492` n `146` status `ready` deltaP `-4.3414` edge `-0.0165` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3349` n `146` status `ready` deltaP `-8.4776` edge `-0.0014` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.5327` n `126` status `ready` deltaP `-20.4366` edge `-0.0176` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7023` n `146` status `ready` deltaP `-6.9354` edge `-0.0326` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2151` n `146` status `ready` deltaP `-8.0059` edge `-0.042` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8072` n `146` status `ready` deltaP `-12.1701` edge `-0.0007` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.9165` n `146` status `ready` deltaP `-7.7577` edge `-0.0375` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1494` n `146` status `ready` deltaP `-14.8409` edge `-0.0949` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-8.7372` n `126` status `ready` deltaP `-13.5416` edge `0.0432` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-11.2661` n `126` status `ready` deltaP `-25.2728` edge `-0.0815` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
