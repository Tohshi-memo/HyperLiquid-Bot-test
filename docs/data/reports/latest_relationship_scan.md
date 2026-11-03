# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T00:37:29.550050+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.059` n `146` status `ready` deltaP `4.5607` edge `0.2408` maxDD `-14.0916`
- `news_risk_high->crypto_alt_24h` score `-0.424` n `126` status `ready` deltaP `20.7093` edge `0.7581` maxDD `-65.3749`
- `news_risk_high->crypto_alt_1h` score `-0.4768` n `146` status `ready` deltaP `1.4334` edge `0.0521` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5891` n `146` status `ready` deltaP `-0.4265` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8773` n `126` status `ready` deltaP `12.5744` edge `0.1293` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9059` n `146` status `ready` deltaP `1.1976` edge `-0.0035` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2419` n `146` status `ready` deltaP `-3.3537` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3273` n `146` status `ready` deltaP `-5.5471` edge `-0.011` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0654` n `146` status `ready` deltaP `-2.9694` edge `-0.0149` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2893` n `146` status `ready` deltaP `-8.0285` edge `-0.0006` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.295` n `126` status `ready` deltaP `-4.3403` edge `0.0189` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.5312` n `126` status `ready` deltaP `-20.4366` edge `-0.0174` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6158` n `146` status `ready` deltaP `-5.8875` edge `-0.0285` maxDD `-16.4088`
- `news_risk_high->equity_24h` score `-2.8099` n `126` status `ready` deltaP `15.8482` edge `0.5436` maxDD `-67.0937`
- `news_risk_high->crypto_major_1h` score `-3.1636` n `146` status `ready` deltaP `-7.7065` edge `-0.0397` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7646` n `146` status `ready` deltaP `-11.7128` edge `-0.0002` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8571` n `146` status `ready` deltaP `-7.3004` edge `-0.0356` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9634` n `146` status `ready` deltaP `-13.9263` edge `-0.0855` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-9.5829` n `126` status `ready` deltaP `-15.2778` edge `-0.0157` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.44` n `146` status `ready` deltaP `-1.445` edge `-0.1076` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
