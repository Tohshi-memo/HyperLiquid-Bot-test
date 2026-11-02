# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T21:37:30.257346+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.2387` n `146` status `ready` deltaP `5.9326` edge `0.2547` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4612` n `146` status `ready` deltaP `1.7328` edge `0.0521` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6054` n `146` status `ready` deltaP `-0.7259` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8898` n `126` status `ready` deltaP `12.5744` edge `0.1277` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9359` n `146` status `ready` deltaP `0.8982` edge `-0.004` maxDD `-1.3981`
- `news_risk_high->crypto_alt_24h` score `-1.1368` n `126` status `ready` deltaP `18.626` edge `0.6806` maxDD `-65.3749`
- `news_risk_high->fx_4h` score `-1.2601` n `146` status `ready` deltaP `-3.6585` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2899` n `146` status `ready` deltaP `-4.9483` edge `-0.0102` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.1309` n `146` status `ready` deltaP `-3.8841` edge `-0.0172` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2845` n `146` status `ready` deltaP `-8.0285` edge `-0.0002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3776` n `126` status `ready` deltaP `-18.3532` edge `-0.0116` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4213` n `126` status `ready` deltaP `-5.5556` edge `0.0108` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6088` n `146` status `ready` deltaP `-5.7378` edge `-0.0286` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1935` n `146` status `ready` deltaP `-7.8562` edge `-0.0412` maxDD `-9.4709`
- `news_risk_high->equity_24h` score `-3.6008` n `126` status `ready` deltaP `13.7649` edge `0.4561` maxDD `-67.0937`
- `news_risk_high->commodity_4h` score `-3.688` n `146` status `ready` deltaP `-10.9506` edge `0.0011` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7877` n `146` status `ready` deltaP `-6.5382` edge `-0.0349` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.8162` n `146` status `ready` deltaP `-13.3165` edge `-0.0773` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.4311` n `126` status `ready` deltaP `-17.3611` edge `-0.0725` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.551` n `146` status `ready` deltaP `-1.9024` edge `-0.1138` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
