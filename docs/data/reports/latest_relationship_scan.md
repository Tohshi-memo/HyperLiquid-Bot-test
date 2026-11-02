# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T12:07:29.306767+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_24h` score `0.2962` n `118` status `ready` deltaP `18.1233` edge `0.6246` maxDD `-48.5962`
- `news_risk_high->crypto_alt_4h` score `0.2625` n `140` status `ready` deltaP `6.2369` edge `0.2355` maxDD `-12.4736`
- `news_risk_high->fx_1h` score `-0.5183` n `146` status `ready` deltaP `0.9208` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.5283` n `146` status `ready` deltaP `1.4334` edge `0.0455` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8006` n `118` status `ready` deltaP `13.7947` edge `0.131` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.0952` n `146` status `ready` deltaP `-0.7485` edge `-0.0063` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.1998` n `140` status `ready` deltaP `-2.5436` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2782` n `146` status `ready` deltaP `-4.9483` edge `-0.0087` maxDD `-3.1082`
- `news_risk_high->fx_24h` score `-2.1779` n `118` status `ready` deltaP `-15.3072` edge `-0.0063` maxDD `-2.336`
- `news_risk_high->index_4h` score `-2.2352` n `140` status `ready` deltaP `-4.6298` edge `-0.0256` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.3745` n `146` status `ready` deltaP `-8.4776` edge `-0.0047` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.905` n `146` status `ready` deltaP `-7.3845` edge `-0.0556` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9057` n `118` status `ready` deltaP `-10.1901` edge `-0.0204` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.317` n `146` status `ready` deltaP `-8.6047` edge `-0.0465` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1528` n `140` status `ready` deltaP `-13.7412` edge `-0.0195` maxDD `-9.4631`
- `news_risk_high->metal_4h` score `-4.4988` n `140` status `ready` deltaP `-3.9024` edge `-0.0284` maxDD `-9.3056`
- `news_risk_high->equity_24h` score `-5.5878` n `118` status `ready` deltaP `6.4825` edge `0.2499` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2338` n `140` status `ready` deltaP `-14.5906` edge `-0.1036` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.3496` n `140` status `ready` deltaP `-3.4582` edge `-0.2113` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.3772` n `118` status `ready` deltaP `-25.7887` edge `-0.1481` maxDD `-27.9126`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
