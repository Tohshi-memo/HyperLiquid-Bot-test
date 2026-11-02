# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T22:22:29.892600+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4542`

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

- `news_risk_high->crypto_alt_4h` score `0.2261` n `146` status `ready` deltaP `5.7802` edge `0.2541` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5064` n `146` status `ready` deltaP `1.2837` edge `0.0493` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.614` n `146` status `ready` deltaP `-0.8756` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.889` n `126` status `ready` deltaP `12.5744` edge `0.1278` maxDD `-14.0483`
- `news_risk_high->crypto_alt_24h` score `-0.9592` n `126` status `ready` deltaP `19.1468` edge `0.6999` maxDD `-65.3749`
- `news_risk_high->index_1h` score `-0.9622` n `146` status `ready` deltaP `0.5988` edge `-0.0042` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2767` n `146` status `ready` deltaP `-3.9634` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.3156` n `146` status `ready` deltaP `-5.3974` edge `-0.0105` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.097` n `146` status `ready` deltaP `-3.4268` edge `-0.0159` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3121` n `146` status `ready` deltaP `-8.3279` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3877` n `126` status `ready` deltaP `-5.2084` edge `0.0128` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.418` n `126` status `ready` deltaP `-18.8741` edge `-0.0133` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6408` n `146` status `ready` deltaP `-6.0372` edge `-0.0307` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2559` n `146` status `ready` deltaP `-8.3053` edge `-0.0434` maxDD `-9.4709`
- `news_risk_high->equity_24h` score `-3.4029` n `126` status `ready` deltaP `14.2857` edge `0.478` maxDD `-67.0937`
- `news_risk_high->commodity_4h` score `-3.7196` n `146` status `ready` deltaP `-11.2555` edge `0.0005` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7853` n `146` status `ready` deltaP `-6.5382` edge `-0.0347` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.8004` n `146` status `ready` deltaP `-13.1641` edge `-0.077` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.2215` n `126` status `ready` deltaP `-16.8403` edge `-0.0585` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.4244` n `146` status `ready` deltaP `-1.445` edge `-0.1063` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
