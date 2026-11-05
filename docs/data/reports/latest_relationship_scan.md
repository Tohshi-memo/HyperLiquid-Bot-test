# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T11:22:35.347551+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3498`

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

- `news_risk_high->crypto_alt_4h` score `-0.2123` n `146` status `ready` deltaP `6.6948` edge `0.1918` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5401` n `146` status `ready` deltaP `2.7807` edge `0.035` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6981` n `146` status `ready` deltaP `-2.5223` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7549` n `146` status `ready` deltaP `2.6946` edge `-0.0009` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4718` n `146` status `ready` deltaP `-7.7744` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5656` n `146` status `ready` deltaP `-8.8405` edge `-0.0196` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7877` n `146` status `ready` deltaP `0.8415` edge `-0.0047` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2592` n `146` status `ready` deltaP `-8.6273` edge `0.0059` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3272` n `146` status `ready` deltaP `-17.159` edge `-0.0131` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5495` n `146` status `ready` deltaP `-5.7378` edge `-0.021` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9222` n `146` status `ready` deltaP `-12.3382` edge `-0.0082` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.2441` n `146` status `ready` deltaP `-6.8083` edge `-0.0524` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.5022` n `146` status `ready` deltaP `-12.0177` edge `0.0237` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.5929` n `146` status `ready` deltaP `-11.2638` edge `-0.0705` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-7.0077` n `146` status `ready` deltaP `-8.1883` edge `-0.1712` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.0683` n `146` status `ready` deltaP `-11.4873` edge `-0.1105` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-9.6534` n `146` status `ready` deltaP `-17.832` edge `0.1405` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7201` n `146` status `ready` deltaP `1.2989` edge `-0.0659` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.0244` n `146` status `ready` deltaP `9.8198` edge `0.2162` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.2316` n `146` status `ready` deltaP `3.5698` edge `-0.2771` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
