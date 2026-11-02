# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T19:22:34.519569+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0261` n `146` status `ready` deltaP `4.5607` edge `0.2299` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4503` n `146` status `ready` deltaP `1.8825` edge `0.0525` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5657` n `146` status `ready` deltaP `0.0226` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8921` n `126` status `ready` deltaP `12.5744` edge `0.1274` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0317` n `146` status `ready` deltaP `-0.1497` edge `-0.005` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2435` n `146` status `ready` deltaP `-3.3537` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3343` n `146` status `ready` deltaP `-5.6968` edge `-0.0109` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.7196` n `126` status `ready` deltaP `17.0635` edge `0.6163` maxDD `-65.3749`
- `news_risk_high->index_4h` score `-2.2459` n `146` status `ready` deltaP `-5.256` edge `-0.0228` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2566` n `126` status `ready` deltaP `-16.7907` edge `-0.0065` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.257` n `146` status `ready` deltaP `-7.7291` edge `0.0001` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.518` n `126` status `ready` deltaP `-6.4237` edge `0.0042` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.7101` n `146` status `ready` deltaP `-6.636` edge `-0.0356` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1636` n `146` status `ready` deltaP `-7.7065` edge `-0.0397` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7192` n `146` status `ready` deltaP `-10.9506` edge `-0.0015` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.2257` n `126` status `ready` deltaP `12.2024` edge `0.3864` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8433` n `146` status `ready` deltaP `-6.843` edge `-0.0375` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1756` n `146` status `ready` deltaP `-14.6885` edge `-0.0981` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-11.1213` n `126` status `ready` deltaP `-18.9236` edge `-0.1196` maxDD `-43.1482`
- `news_risk_high->commodity_24h` score `-12.105` n `126` status `ready` deltaP `-26.4881` edge `-0.1433` maxDD `-32.7755`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
