# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T21:07:30.046143+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4913`

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

- `news_risk_high->crypto_alt_4h` score `0.2065` n `146` status `ready` deltaP `5.6277` edge `0.2526` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4565` n `146` status `ready` deltaP `1.7328` edge `0.0527` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6054` n `146` status `ready` deltaP `-0.7259` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8906` n `126` status `ready` deltaP `12.5744` edge `0.1276` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.949` n `146` status `ready` deltaP `0.7485` edge `-0.0041` maxDD `-1.3981`
- `news_risk_high->crypto_alt_24h` score `-1.2672` n `126` status `ready` deltaP `18.2788` edge `0.6662` maxDD `-65.3749`
- `news_risk_high->fx_4h` score `-1.2688` n `146` status `ready` deltaP `-3.811` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2907` n `146` status `ready` deltaP `-4.9483` edge `-0.0103` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.1561` n `146` status `ready` deltaP `-4.1889` edge `-0.0184` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2726` n `146` status `ready` deltaP `-7.8788` edge `-0.0002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3502` n `126` status `ready` deltaP `-18.006` edge `-0.0104` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4519` n `126` status `ready` deltaP `-5.9028` edge `0.0092` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6205` n `146` status `ready` deltaP `-5.8875` edge `-0.0291` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1875` n `146` status `ready` deltaP `-7.8562` edge `-0.0407` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6892` n `146` status `ready` deltaP `-10.9506` edge `0.001` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-3.739` n `126` status `ready` deltaP `13.4176` edge `0.4407` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.7925` n `146` status `ready` deltaP `-6.5382` edge `-0.0353` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.867` n `146` status `ready` deltaP `-13.6214` edge `-0.0795` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.5897` n `126` status `ready` deltaP `-17.7083` edge `-0.0834` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.6618` n `146` status `ready` deltaP `-2.2072` edge `-0.121` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
