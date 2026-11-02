# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T19:52:32.357519+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4999`

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

- `news_risk_high->crypto_alt_4h` score `0.0467` n `146` status `ready` deltaP `4.8655` edge `0.2372` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4425` n `146` status `ready` deltaP `1.8825` edge `0.0535` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5821` n `146` status `ready` deltaP `-0.2768` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8913` n `126` status `ready` deltaP `12.5744` edge `0.1275` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0149` n `146` status `ready` deltaP `0.0` edge `-0.0046` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2522` n `146` status `ready` deltaP `-3.5061` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3242` n `146` status `ready` deltaP `-5.5471` edge `-0.0106` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.5892` n `126` status `ready` deltaP `17.4107` edge `0.6307` maxDD `-65.3749`
- `news_risk_high->index_4h` score `-2.2207` n `146` status `ready` deltaP `-4.9511` edge `-0.0216` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2824` n `126` status `ready` deltaP `-17.1379` edge `-0.0075` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.2881` n `146` status `ready` deltaP `-8.0285` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.507` n `126` status `ready` deltaP `-6.4237` edge `0.0056` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6781` n `146` status `ready` deltaP `-6.4863` edge `-0.0325` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1648` n `146` status `ready` deltaP `-7.7065` edge `-0.0398` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7084` n `146` status `ready` deltaP `-10.9506` edge `-0.0006` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.0844` n `126` status `ready` deltaP `12.5496` edge `0.4022` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8373` n `146` status `ready` deltaP `-6.843` edge `-0.037` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0864` n `146` status `ready` deltaP `-14.3836` edge `-0.0927` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.9711` n `126` status `ready` deltaP `-18.5764` edge `-0.1094` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-12.006` n `146` status `ready` deltaP `-2.9694` edge `-0.1446` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
