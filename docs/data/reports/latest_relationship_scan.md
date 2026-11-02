# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T22:52:29.780215+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.2143` n `146` status `ready` deltaP `5.6277` edge `0.2536` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4745` n `146` status `ready` deltaP `1.5831` edge `0.0514` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6054` n `146` status `ready` deltaP `-0.7259` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->crypto_alt_24h` score `-0.8397` n `126` status `ready` deltaP `19.494` edge `0.7129` maxDD `-65.3749`
- `news_risk_high->metal_24h` score `-0.889` n `126` status `ready` deltaP `12.5744` edge `0.1278` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9347` n `146` status `ready` deltaP `0.8982` edge `-0.0039` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2846` n `146` status `ready` deltaP `-4.1159` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.332` n `146` status `ready` deltaP `-5.6968` edge `-0.0106` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.0741` n `146` status `ready` deltaP `-3.1219` edge `-0.015` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3121` n `146` status `ready` deltaP `-8.3279` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3572` n `126` status `ready` deltaP `-4.8612` edge `0.0144` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4454` n `126` status `ready` deltaP `-19.2213` edge `-0.0145` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6259` n `146` status `ready` deltaP `-5.8875` edge `-0.0298` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2127` n `146` status `ready` deltaP `-8.0059` edge `-0.0418` maxDD `-9.4709`
- `news_risk_high->equity_24h` score `-3.2655` n `126` status `ready` deltaP `14.6329` edge `0.4933` maxDD `-67.0937`
- `news_risk_high->commodity_4h` score `-3.7476` n `146` status `ready` deltaP `-11.5604` edge `0.0002` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7841` n `146` status `ready` deltaP `-6.5382` edge `-0.0346` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.7882` n `146` status `ready` deltaP `-13.0116` edge `-0.077` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.0785` n `126` status `ready` deltaP `-16.493` edge `-0.0489` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.352` n `146` status `ready` deltaP `-1.1402` edge `-0.1023` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
