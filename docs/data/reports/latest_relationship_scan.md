# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T15:37:28.786732+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4869`

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

- `news_risk_high->crypto_alt_4h` score `-0.1` n `146` status `ready` deltaP `4.7131` edge `0.2194` maxDD `-14.0916`
- `news_risk_high->fx_1h` score `-0.5183` n `146` status `ready` deltaP `0.9208` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5368` n `146` status `ready` deltaP `1.2837` edge `0.0454` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8438` n `126` status `ready` deltaP `12.5744` edge `0.1336` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0784` n `146` status `ready` deltaP `-0.5988` edge `-0.0059` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1587` n `146` status `ready` deltaP `-1.8293` edge `-0.0112` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3265` n `146` status `ready` deltaP `-5.5471` edge `-0.0109` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.0533` n `126` status `ready` deltaP `-14.1866` edge `0.0022` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2284` n `146` status `ready` deltaP `-4.7987` edge `-0.0236` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2486` n `146` status `ready` deltaP `-7.5794` edge `-0.0002` maxDD `-3.2657`
- `news_risk_high->crypto_alt_24h` score `-2.4872` n `126` status `ready` deltaP `14.6329` edge `0.5341` maxDD `-65.3749`
- `news_risk_high->index_24h` score `-2.5624` n `126` status `ready` deltaP `-6.4237` edge `-0.0015` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.8294` n `146` status `ready` deltaP `-7.2348` edge `-0.0469` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3302` n `146` status `ready` deltaP `-8.6047` edge `-0.0476` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.808` n `146` status `ready` deltaP `-10.9506` edge `-0.0089` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6469` n `146` status `ready` deltaP `-5.3187` edge `-0.0313` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-4.9094` n `126` status `ready` deltaP `9.5982` edge `0.3161` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2968` n `146` status `ready` deltaP `-14.6885` edge `-0.1082` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-12.0305` n `126` status `ready` deltaP `-21.5278` edge `-0.178` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.3006` n `126` status `ready` deltaP `-26.4881` edge `-0.1596` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
