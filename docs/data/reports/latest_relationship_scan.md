# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T16:07:35.013925+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4893`

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

- `news_risk_high->crypto_alt_4h` score `-0.1259` n `146` status `ready` deltaP `4.5607` edge `0.2171` maxDD `-14.0916`
- `news_risk_high->fx_1h` score `-0.5183` n `146` status `ready` deltaP `0.9208` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5431` n `146` status `ready` deltaP `1.2837` edge `0.0446` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8516` n `126` status `ready` deltaP `12.5744` edge `0.1326` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0928` n `146` status `ready` deltaP `-0.7485` edge `-0.0061` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1674` n `146` status `ready` deltaP `-1.9817` edge `-0.0113` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3351` n `146` status `ready` deltaP `-5.6968` edge `-0.011` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.0807` n `126` status `ready` deltaP `-14.5338` edge `0.001` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2458` n `146` status `ready` deltaP `-5.1036` edge `-0.0238` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2642` n `146` status `ready` deltaP `-7.7291` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->crypto_alt_24h` score `-2.4228` n `126` status `ready` deltaP `14.8065` edge `0.5412` maxDD `-65.3749`
- `news_risk_high->index_24h` score `-2.5585` n `126` status `ready` deltaP `-6.4237` edge `-0.001` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.845` n `146` status `ready` deltaP `-7.3845` edge `-0.0479` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.317` n `146` status `ready` deltaP `-8.455` edge `-0.0475` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8044` n `146` status `ready` deltaP `-10.9506` edge `-0.0086` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.6881` n `146` status `ready` deltaP `-5.6235` edge `-0.0327` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-4.843` n `126` status `ready` deltaP `9.9454` edge `0.3223` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.3064` n `146` status `ready` deltaP `-14.6885` edge `-0.109` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.9487` n `126` status `ready` deltaP `-21.1805` edge `-0.1735` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.291` n `126` status `ready` deltaP `-26.4881` edge `-0.1588` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
