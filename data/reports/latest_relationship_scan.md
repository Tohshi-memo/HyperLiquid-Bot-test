# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T07:37:33.943582+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `news_risk_high->crypto_alt_4h` score `0.234` n `146` status `ready` deltaP `5.9326` edge `0.2541` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3848` n `146` status `ready` deltaP `2.4813` edge `0.0569` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5953` n `146` status `ready` deltaP `-0.5762` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8939` n `146` status `ready` deltaP `1.3473` edge `-0.0035` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2507` n `146` status `ready` deltaP `-3.6585` edge `-0.0108` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2743` n `146` status `ready` deltaP `-4.7986` edge `-0.0092` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.6045` n `138` status `ready` deltaP `10.4544` edge `0.1222` maxDD `-14.0483`
- `news_risk_high->index_4h` score `-2.045` n `146` status `ready` deltaP `-2.817` edge `-0.0133` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.219` n `138` status `ready` deltaP `-3.3439` edge `0.022` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3888` n `146` status `ready` deltaP `-9.0764` edge `-0.0019` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4253` n `138` status `ready` deltaP `-18.1461` edge `-0.0191` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6883` n `146` status `ready` deltaP `-6.7857` edge `-0.0318` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1935` n `146` status `ready` deltaP `-8.0059` edge `-0.0402` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8848` n `146` status `ready` deltaP `-12.7799` edge `-0.0031` maxDD `-9.5011`
- `news_risk_high->crypto_alt_24h` score `-4.1595` n `138` status `ready` deltaP `19.9804` edge `0.7622` maxDD `-99.6271`
- `news_risk_high->metal_4h` score `-4.7727` n `146` status `ready` deltaP `-6.9955` edge `-0.0306` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.4215` n `138` status `ready` deltaP `15.1193` edge `0.4983` maxDD `-70.4041`
- `news_risk_high->crypto_major_4h` score `-6.9716` n `146` status `ready` deltaP `-13.7738` edge `-0.0872` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.4808` n `146` status `ready` deltaP `-1.445` edge `-0.111` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.5853` n `138` status `ready` deltaP `-23.913` edge `-0.0958` maxDD `-41.1509`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
