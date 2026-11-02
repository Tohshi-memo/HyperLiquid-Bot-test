# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T20:37:39.962036+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.1438` n `146` status `ready` deltaP `5.3229` edge `0.2466` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4667` n `146` status `ready` deltaP `1.5831` edge `0.0524` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5899` n `146` status `ready` deltaP `-0.4265` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8913` n `126` status `ready` deltaP `12.5744` edge `0.1275` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9766` n `146` status `ready` deltaP `0.4491` edge `-0.0044` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2688` n `146` status `ready` deltaP `-3.811` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2993` n `146` status `ready` deltaP `-5.098` edge `-0.0104` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.4023` n `126` status `ready` deltaP `17.9315` edge `0.6512` maxDD `-65.3749`
- `news_risk_high->index_4h` score `-2.1829` n `146` status `ready` deltaP `-4.4938` edge `-0.0198` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2869` n `146` status `ready` deltaP `-8.0285` edge `-0.0004` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3228` n `126` status `ready` deltaP `-17.6588` edge `-0.0092` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.4816` n `126` status `ready` deltaP `-6.25` edge `0.0077` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.6517` n `146` status `ready` deltaP `-6.1869` edge `-0.0311` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2067` n `146` status `ready` deltaP `-8.0059` edge `-0.0413` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6952` n `146` status `ready` deltaP `-10.9506` edge `0.0005` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-3.8818` n `126` status `ready` deltaP `13.0704` edge `0.4247` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.7997` n `146` status `ready` deltaP `-6.5382` edge `-0.0359` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.9598` n `146` status `ready` deltaP `-13.9263` edge `-0.0852` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.7519` n `126` status `ready` deltaP `-18.0555` edge `-0.0946` maxDD `-43.1482`
- `news_risk_high->equity_4h` score `-11.8002` n `146` status `ready` deltaP `-2.5121` edge `-0.1305` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
