# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T16:37:32.184931+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4951`

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

- `news_risk_high->crypto_alt_4h` score `-0.122` n `146` status `ready` deltaP `4.5607` edge `0.2176` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5033` n `146` status `ready` deltaP `1.5831` edge `0.0477` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.526` n `146` status `ready` deltaP `0.7711` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8601` n `126` status `ready` deltaP `12.5744` edge `0.1315` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.064` n `146` status `ready` deltaP `-0.4491` edge `-0.0057` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1761` n `146` status `ready` deltaP `-2.1341` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3359` n `146` status `ready` deltaP `-5.6968` edge `-0.0111` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.1081` n `126` status `ready` deltaP `-14.881` edge `-0.0002` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2545` n `146` status `ready` deltaP `-5.256` edge `-0.0239` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2666` n `146` status `ready` deltaP `-7.7291` edge `-0.0007` maxDD `-3.2657`
- `news_risk_high->crypto_alt_24h` score `-2.3259` n `126` status `ready` deltaP `15.1538` edge `0.5513` maxDD `-65.3749`
- `news_risk_high->index_24h` score `-2.5523` n `126` status `ready` deltaP `-6.4237` edge `-0.0002` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.8021` n `146` status `ready` deltaP `-7.0851` edge `-0.0444` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2547` n `146` status `ready` deltaP `-8.1556` edge `-0.0443` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.796` n `146` status `ready` deltaP `-10.9506` edge `-0.0079` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7305` n `146` status `ready` deltaP `-5.9284` edge `-0.0342` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-4.7587` n `126` status `ready` deltaP `10.2926` edge `0.3308` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2944` n `146` status `ready` deltaP `-14.6885` edge `-0.108` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.8345` n `126` status `ready` deltaP `-20.8333` edge `-0.1663` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.2778` n `126` status `ready` deltaP `-26.4881` edge `-0.1577` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
