# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T12:22:34.166722+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3787`

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

- `news_risk_high->crypto_alt_4h` score `-0.0871` n `146` status `ready` deltaP `7.1521` edge `0.2048` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5089` n `146` status `ready` deltaP `3.0801` edge `0.037` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7066` n `146` status `ready` deltaP `-2.672` edge `-0.0027` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7693` n `146` status `ready` deltaP `2.5449` edge `-0.0011` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4536` n `146` status `ready` deltaP `-7.4695` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5859` n `146` status `ready` deltaP `-9.1399` edge `-0.0202` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7964` n `146` status `ready` deltaP `0.6891` edge `-0.0048` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2962` n `146` status `ready` deltaP `-16.6381` edge `-0.0126` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3132` n `146` status `ready` deltaP `-9.0764` edge `0.0044` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5441` n `146` status `ready` deltaP `-5.5881` edge `-0.0213` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9316` n `146` status `ready` deltaP `-12.3382` edge `-0.0094` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.1794` n `146` status `ready` deltaP `-6.3592` edge `-0.05` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6098` n `146` status `ready` deltaP `-12.6274` edge `0.0188` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6439` n `146` status `ready` deltaP `-11.7211` edge `-0.0717` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.8831` n `146` status `ready` deltaP `-11.1824` edge `-0.0971` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.1809` n `146` status `ready` deltaP `-8.8827` edge `-0.181` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.4851` n `146` status `ready` deltaP `-17.1376` edge `0.1499` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.6345` n `146` status `ready` deltaP `1.6037` edge `-0.0608` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.1168` n `146` status `ready` deltaP `9.8198` edge `0.2085` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.4705` n `146` status `ready` deltaP `2.8753` edge `-0.3031` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
