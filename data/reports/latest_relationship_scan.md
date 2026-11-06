# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T14:57:53.336351+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3923`

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

- `news_risk_high->equity_24h` score `0.8939` n `111` status `ready` deltaP `27.4713` edge `1.0901` maxDD `-86.0244`
- `news_risk_high->equity_4h` score `0.5841` n `111` status `ready` deltaP `12.3009` edge `0.1837` maxDD `-12.266`
- `news_risk_high->index_4h` score `0.3006` n `111` status `ready` deltaP `11.8436` edge `0.0177` maxDD `-1.3166`
- `news_risk_high->index_1h` score `-0.2517` n `111` status `ready` deltaP `5.8478` edge `0.0022` maxDD `-0.8765`
- `news_risk_high->index_24h` score `-0.3692` n `111` status `ready` deltaP `-0.0685` edge `0.1366` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.4558` n `111` status `ready` deltaP `0.1646` edge `0.0009` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.5203` n `111` status `ready` deltaP `2.5463` edge `0.0391` maxDD `-5.8225`
- `news_risk_high->crypto_major_1h` score `-0.7942` n `111` status `ready` deltaP `-2.1107` edge `0.0128` maxDD `-4.7103`
- `news_risk_high->crypto_alt_4h` score `-0.7968` n `111` status `ready` deltaP `1.9337` edge `0.1486` maxDD `-14.0916`
- `news_risk_high->metal_1h` score `-0.8157` n `111` status `ready` deltaP `-1.5011` edge `-0.0076` maxDD `-1.0293`
- `news_risk_high->crypto_major_4h` score `-1.0313` n `111` status `ready` deltaP `-1.9062` edge `0.0616` maxDD `-9.1553`
- `news_risk_high->fx_4h` score `-1.0583` n `111` status `ready` deltaP `-0.8789` edge `-0.0014` maxDD `-0.4745`
- `news_risk_high->equity_1h` score `-1.0749` n `111` status `ready` deltaP `0.3008` edge `0.029` maxDD `-8.5048`
- `news_risk_high->fx_24h` score `-1.1751` n `111` status `ready` deltaP `-13.0973` edge `0.0001` maxDD `-0.4086`
- `news_risk_high->metal_4h` score `-1.9032` n `111` status `ready` deltaP `-3.8315` edge `-0.039` maxDD `-1.8579`
- `news_risk_high->commodity_1h` score `-2.961` n `111` status `ready` deltaP `-15.1643` edge `-0.009` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.1267` n `111` status `ready` deltaP `-0.5626` edge `-0.2075` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-5.2864` n `111` status `ready` deltaP `-26.5354` edge `-0.0282` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.0504` n `111` status `ready` deltaP `-16.2552` edge `0.183` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.3765` n `111` status `ready` deltaP `-24.3165` edge `-0.0078` maxDD `-38.2504`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
