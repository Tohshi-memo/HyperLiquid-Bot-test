# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T14:07:29.053783+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->crypto_alt_4h` score `-0.0088` n `146` status `ready` deltaP `7.3073` edge `0.2138` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5041` n `146` status `ready` deltaP `2.0322` edge `0.0446` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7082` n `146` status `ready` deltaP `-2.672` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8508` n `146` status `ready` deltaP `1.6467` edge `-0.0019` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3343` n `146` status `ready` deltaP `-5.3974` edge `-0.0129` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4595` n `146` status `ready` deltaP `-7.5988` edge `-0.0113` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8494` n `146` status `ready` deltaP `0.2248` edge `-0.0085` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-1.9783` n `146` status `ready` deltaP `-1.9552` edge `0.0436` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.2701` n `146` status `ready` deltaP `-8.1782` edge `0.002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4101` n `146` status `ready` deltaP `-18.3178` edge `-0.016` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6368` n `146` status `ready` deltaP `-6.4863` edge `-0.0272` maxDD `-16.4088`
- `news_risk_high->metal_24h` score `-2.7379` n `146` status `ready` deltaP `6.3801` edge `0.0875` maxDD `-16.6552`
- `news_risk_high->crypto_major_1h` score `-3.2475` n `146` status `ready` deltaP `-8.1556` edge `-0.0437` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.512` n `146` status `ready` deltaP `-10.0554` edge `0.0098` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8261` n `146` status `ready` deltaP `-5.4878` edge `-0.0451` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0099` n `146` status `ready` deltaP `-12.4079` edge `-0.0995` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.7656` n `146` status `ready` deltaP `14.9951` edge `0.4757` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-11.3357` n `146` status `ready` deltaP `12.9189` edge `0.4196` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.399` n `146` status `ready` deltaP `-1.1429` edge `-0.1062` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2441` n `146` status `ready` deltaP `-20.6807` edge `-0.0564` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
