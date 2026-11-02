# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T15:07:29.367706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4881`

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

- `news_risk_high->crypto_alt_4h` score `-0.0561` n `146` status `ready` deltaP `5.018` edge `0.223` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5041` n `146` status `ready` deltaP `1.4334` edge `0.0486` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5175` n `146` status `ready` deltaP `0.9208` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8352` n `126` status `ready` deltaP `12.5744` edge `0.1347` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0485` n `146` status `ready` deltaP `-0.2994` edge `-0.0054` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1421` n `146` status `ready` deltaP `-1.5244` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3063` n `146` status `ready` deltaP `-5.2477` edge `-0.0103` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.0259` n `126` status `ready` deltaP `-13.8393` edge `0.0034` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2094` n `146` status `ready` deltaP `-4.4938` edge `-0.0232` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2882` n `146` status `ready` deltaP `-7.8788` edge `-0.0015` maxDD `-3.2657`
- `news_risk_high->crypto_alt_24h` score `-2.5293` n `126` status `ready` deltaP `14.6329` edge `0.5287` maxDD `-65.3749`
- `news_risk_high->index_24h` score `-2.5616` n `126` status `ready` deltaP `-6.4237` edge `-0.0014` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.8029` n `146` status `ready` deltaP `-7.0851` edge `-0.0445` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2894` n `146` status `ready` deltaP `-8.455` edge `-0.0452` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8346` n `146` status `ready` deltaP `-11.103` edge `-0.0101` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6057` n `146` status `ready` deltaP `-5.0138` edge `-0.0299` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-4.9364` n `126` status `ready` deltaP `9.4246` edge `0.3138` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2484` n `146` status `ready` deltaP `-14.3836` edge `-0.1062` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-12.0882` n `126` status `ready` deltaP `-21.875` edge `-0.1805` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.321` n `126` status `ready` deltaP `-26.4881` edge `-0.1613` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
