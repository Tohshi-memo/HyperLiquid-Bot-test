# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T01:37:25.963214+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `-0.3971` n `146` status `ready` deltaP `6.6948` edge `0.1681` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5354` n `146` status `ready` deltaP `2.4813` edge `0.0376` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7245` n `146` status `ready` deltaP `-2.9714` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7909` n `146` status `ready` deltaP `2.3952` edge `-0.0019` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4667` n `146` status `ready` deltaP `-7.4932` edge `-0.0159` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5627` n `146` status `ready` deltaP `-9.2988` edge `-0.0132` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9571` n `146` status `ready` deltaP `-1.2926` edge `-0.0122` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1143` n `146` status `ready` deltaP `-7.28` edge `0.009` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4398` n `146` status `ready` deltaP `-18.6638` edge `-0.0175` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5682` n `146` status `ready` deltaP `-6.0372` edge `-0.0214` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.573` n `146` status `ready` deltaP `-9.5677` edge `0.0181` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.2044` n `146` status `ready` deltaP `-10.036` edge `0.0353` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.364` n `146` status `ready` deltaP `-7.5568` edge `-0.0574` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-5.0198` n `146` status `ready` deltaP `-1.5784` edge `-0.0496` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.1434` n `146` status `ready` deltaP `-7.9101` edge `-0.0554` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.7664` n `146` status `ready` deltaP `-13.1641` edge `-0.1575` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.2292` n `146` status `ready` deltaP `-0.8353` edge `-0.0941` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.2361` n `146` status `ready` deltaP `-20.6807` edge `0.0276` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-11.7615` n `146` status `ready` deltaP `10.1508` edge `0.1239` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-12.4483` n `146` status `ready` deltaP `11.8809` edge `0.3338` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
