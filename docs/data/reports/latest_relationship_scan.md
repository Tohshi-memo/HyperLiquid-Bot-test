# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T20:18:19.779069+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4933`

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

- `news_risk_high->crypto_alt_4h` score `0.1086` n `146` status `ready` deltaP `5.1704` edge `0.2431` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4667` n `146` status `ready` deltaP `1.5831` edge `0.0524` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5899` n `146` status `ready` deltaP `-0.4265` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8913` n `126` status `ready` deltaP `12.5744` edge `0.1275` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9898` n `146` status `ready` deltaP `0.2994` edge `-0.0045` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2688` n `146` status `ready` deltaP `-3.811` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.307` n `146` status `ready` deltaP `-5.2477` edge `-0.0104` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.4674` n `126` status `ready` deltaP `17.7579` edge `0.644` maxDD `-65.3749`
- `news_risk_high->index_4h` score `-2.1955` n `146` status `ready` deltaP `-4.6463` edge `-0.0204` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2881` n `146` status `ready` deltaP `-8.0285` edge `-0.0005` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3099` n `126` status `ready` deltaP `-17.4852` edge `-0.0087` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4969` n `126` status `ready` deltaP `-6.4237` edge `0.0069` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6657` n `146` status `ready` deltaP `-6.3366` edge `-0.0319` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2043` n `146` status `ready` deltaP `-8.0059` edge `-0.0411` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.7` n `146` status `ready` deltaP `-10.9506` edge `0.0001` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-3.9532` n `126` status `ready` deltaP `12.8968` edge `0.4167` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.8045` n `146` status `ready` deltaP `-6.5382` edge `-0.0363` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0092` n `146` status `ready` deltaP `-14.0787` edge `-0.0883` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.8306` n `126` status `ready` deltaP `-18.2291` edge `-0.1` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.8712` n `146` status `ready` deltaP `-2.6646` edge `-0.1354` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
