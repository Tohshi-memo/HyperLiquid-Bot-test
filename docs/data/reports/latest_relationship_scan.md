# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T19:52:36.477719+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4030`

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

- `news_risk_high->crypto_alt_4h` score `0.1652` n `146` status `ready` deltaP `8.5241` edge `0.228` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.399` n `146` status `ready` deltaP `3.3795` edge `0.0491` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6249` n `146` status `ready` deltaP `-1.175` edge `-0.0022` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7885` n `146` status `ready` deltaP `2.3952` edge `-0.0017` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3811` n `146` status `ready` deltaP `-6.1459` edge `-0.0139` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4204` n `146` status `ready` deltaP `-7.0122` edge `-0.0102` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8837` n `146` status `ready` deltaP `-0.2255` edge `-0.0099` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1933` n `146` status `ready` deltaP `-8.1782` edge `0.0084` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.2558` n `146` status `ready` deltaP `-5.7614` edge `0.0334` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4558` n `146` status `ready` deltaP `-18.8368` edge `-0.0184` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5425` n `146` status `ready` deltaP `-6.0372` edge `-0.0181` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1877` n `146` status `ready` deltaP `-6.8083` edge `-0.0477` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.2392` n `146` status `ready` deltaP `-10.036` edge `0.0324` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-3.7954` n `146` status `ready` deltaP `2.4008` edge `0.0259` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.8693` n `146` status `ready` deltaP `-5.6235` edge `-0.0478` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.1233` n `146` status `ready` deltaP `-11.3348` edge `-0.1161` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.2903` n `146` status `ready` deltaP `14.13` edge `0.4142` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.8883` n `146` status `ready` deltaP `0.2318` edge `-0.0728` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.5171` n `146` status `ready` deltaP `11.8809` edge `0.4114` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-12.0005` n `146` status `ready` deltaP `-20.6807` edge `-0.0361` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
