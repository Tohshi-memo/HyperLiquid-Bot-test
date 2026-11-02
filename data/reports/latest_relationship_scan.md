# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T13:07:30.945579+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_4h` score `0.0415` n `144` status `ready` deltaP `5.437` edge `0.2265` maxDD `-13.5937`
- `news_risk_high->fx_1h` score `-0.5509` n `146` status `ready` deltaP `0.322` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5524` n `146` status `ready` deltaP `1.134` edge `0.0444` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8679` n `122` status `ready` deltaP `12.4403` edge `0.1314` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0724` n `146` status `ready` deltaP `-0.4491` edge `-0.0064` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1218` n `144` status `ready` deltaP `-1.1349` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->crypto_alt_24h` score `-1.1394` n `122` status `ready` deltaP `16.0462` edge `0.5699` maxDD `-56.5025`
- `news_risk_high->metal_1h` score `-1.2829` n `146` status `ready` deltaP `-4.9483` edge `-0.0093` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.0695` n `122` status `ready` deltaP `-14.1678` edge `0.0` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2384` n `144` status `ready` deltaP `-4.8272` edge `-0.0247` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3757` n `146` status `ready` deltaP `-8.4776` edge `-0.0048` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.7312` n `122` status `ready` deltaP `-8.2451` edge `-0.011` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.9191` n `146` status `ready` deltaP `-7.5342` edge `-0.0564` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.3506` n `146` status `ready` deltaP `-8.7544` edge `-0.0483` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9958` n `144` status `ready` deltaP `-12.3984` edge `-0.0149` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.5949` n `144` status `ready` deltaP `-5.0135` edge `-0.029` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.3169` n `122` status `ready` deltaP `7.7329` edge `0.2763` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.3102` n `144` status `ready` deltaP `-14.7357` edge `-0.109` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-11.7685` n `122` status `ready` deltaP `-26.1499` edge `-0.1539` maxDD `-29.865`
- `news_risk_high->crypto_major_24h` score `-11.8796` n `122` status `ready` deltaP `-22.1796` edge `-0.1889` maxDD `-40.9229`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
