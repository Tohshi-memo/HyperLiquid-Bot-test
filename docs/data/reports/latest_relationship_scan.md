# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T11:37:31.172440+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4288`

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

- `news_risk_high->crypto_alt_4h` score `0.3015` n `146` status `ready` deltaP `6.3899` edge `0.2597` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4939` n `146` status `ready` deltaP `1.4334` edge `0.0499` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6374` n `146` status `ready` deltaP `-1.3247` edge `-0.0028` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9011` n `146` status `ready` deltaP `1.1976` edge `-0.0031` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2323` n `146` status `ready` deltaP `-4.1998` edge `-0.0078` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2846` n `146` status `ready` deltaP `-4.1159` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-2.0135` n `146` status `ready` deltaP `10.2145` edge `0.1223` maxDD `-16.6552`
- `news_risk_high->index_4h` score `-2.0254` n `146` status `ready` deltaP `-2.6646` edge `-0.0118` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.1465` n `146` status `ready` deltaP `-2.7896` edge `0.0276` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.3763` n `146` status `ready` deltaP `-17.159` edge `-0.0194` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4822` n `146` status `ready` deltaP `-9.8249` edge `-0.0047` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6992` n `146` status `ready` deltaP `-6.9354` edge `-0.0322` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2954` n `146` status `ready` deltaP `-8.9041` edge `-0.0427` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.2467` n `146` status `ready` deltaP `-15.2189` edge `-0.017` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.442` n `146` status `ready` deltaP `-4.5565` edge `-0.0193` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-6.2555` n `146` status `ready` deltaP `19.542` edge `0.7672` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.8334` n `146` status `ready` deltaP `-13.6214` edge `-0.0767` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-10.1772` n `146` status `ready` deltaP `14.6809` edge `0.5092` maxDD `-102.7472`
- `news_risk_high->equity_4h` score `-11.2806` n `146` status `ready` deltaP `-0.6828` edge `-0.0994` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.9109` n `146` status `ready` deltaP `-23.7348` edge `-0.0916` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
