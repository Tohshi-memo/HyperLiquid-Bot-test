# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T21:22:43.937171+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.2269` n `146` status `ready` deltaP `5.7802` edge `0.2542` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4456` n `146` status `ready` deltaP `1.8825` edge `0.0531` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6054` n `146` status `ready` deltaP `-0.7259` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8898` n `126` status `ready` deltaP `12.5744` edge `0.1277` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9347` n `146` status `ready` deltaP `0.8982` edge `-0.0039` maxDD `-1.3981`
- `news_risk_high->crypto_alt_24h` score `-1.2051` n `126` status `ready` deltaP `18.4524` edge `0.673` maxDD `-65.3749`
- `news_risk_high->fx_4h` score `-1.2601` n `146` status `ready` deltaP `-3.6585` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2821` n `146` status `ready` deltaP `-4.7986` edge `-0.0102` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.1435` n `146` status `ready` deltaP `-4.0365` edge `-0.0178` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2714` n `146` status `ready` deltaP `-7.8788` edge `-0.0001` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3639` n `126` status `ready` deltaP `-18.1796` edge `-0.011` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4366` n `126` status `ready` deltaP `-5.7292` edge `0.01` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6057` n `146` status `ready` deltaP `-5.7378` edge `-0.0282` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1732` n `146` status `ready` deltaP `-7.7065` edge `-0.0405` maxDD `-9.4709`
- `news_risk_high->equity_24h` score `-3.6691` n `126` status `ready` deltaP `13.5913` edge `0.4485` maxDD `-67.0937`
- `news_risk_high->commodity_4h` score `-3.6868` n `146` status `ready` deltaP `-10.9506` edge `0.0012` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7901` n `146` status `ready` deltaP `-6.5382` edge `-0.0351` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.8368` n `146` status `ready` deltaP `-13.469` edge `-0.078` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.5158` n `126` status `ready` deltaP `-17.5347` edge `-0.0784` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.6028` n `146` status `ready` deltaP `-2.0548` edge `-0.1171` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
