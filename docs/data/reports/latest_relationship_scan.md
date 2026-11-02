# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T21:52:35.372818+00:00`
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
- `news_risk_high->crypto_alt_1h` score `-0.4776` n `146` status `ready` deltaP `1.5831` edge `0.051` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6054` n `146` status `ready` deltaP `-0.7259` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.889` n `126` status `ready` deltaP `12.5744` edge `0.1278` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9359` n `146` status `ready` deltaP `0.8982` edge `-0.004` maxDD `-1.3981`
- `news_risk_high->crypto_alt_24h` score `-1.0763` n `126` status `ready` deltaP `18.7996` edge `0.6872` maxDD `-65.3749`
- `news_risk_high->fx_4h` score `-1.2601` n `146` status `ready` deltaP `-3.6585` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2985` n `146` status `ready` deltaP `-5.098` edge `-0.0103` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.1198` n `146` status `ready` deltaP `-3.7316` edge `-0.0168` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2977` n `146` status `ready` deltaP `-8.1782` edge `-0.0003` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3913` n `126` status `ready` deltaP `-18.5268` edge `-0.0122` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4069` n `126` status `ready` deltaP `-5.382` edge `0.0115` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6135` n `146` status `ready` deltaP `-5.7378` edge `-0.0292` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2151` n `146` status `ready` deltaP `-8.0059` edge `-0.042` maxDD `-9.4709`
- `news_risk_high->equity_24h` score `-3.5325` n `126` status `ready` deltaP `13.9385` edge `0.4637` maxDD `-67.0937`
- `news_risk_high->commodity_4h` score `-3.6892` n `146` status `ready` deltaP `-10.9506` edge `0.001` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7877` n `146` status `ready` deltaP `-6.5382` edge `-0.0349` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.8186` n `146` status `ready` deltaP `-13.3165` edge `-0.0775` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.356` n `126` status `ready` deltaP `-17.1875` edge `-0.0674` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.5088` n `146` status `ready` deltaP `-1.7499` edge `-0.1113` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
