# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T13:07:31.435792+00:00`
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

- `news_risk_high->crypto_alt_4h` score `-0.0292` n `146` status `ready` deltaP `7.1554` edge `0.2122` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4893` n `146` status `ready` deltaP `2.0322` edge `0.0465` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.709` n `146` status `ready` deltaP `-2.672` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8256` n `146` status `ready` deltaP `1.9461` edge `-0.0018` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.3234` n `146` status `ready` deltaP `-5.2477` edge `-0.0125` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4721` n `146` status `ready` deltaP `-7.7508` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.877` n `146` status `ready` deltaP `-0.2311` edge `-0.009` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-1.9337` n `146` status `ready` deltaP `-1.2632` edge `0.0447` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.336` n `146` status `ready` deltaP `-8.777` edge `0.0005` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.382` n `146` status `ready` deltaP `-17.9718` edge `-0.0147` maxDD `-2.336`
- `news_risk_high->metal_24h` score `-2.5793` n `146` status `ready` deltaP `7.0721` edge `0.0961` maxDD `-16.6552`
- `news_risk_high->equity_1h` score `-2.6134` n `146` status `ready` deltaP `-6.1869` edge `-0.0262` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1887` n `146` status `ready` deltaP `-7.8562` edge `-0.0408` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.599` n `146` status `ready` deltaP `-10.6633` edge `0.0066` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8213` n `146` status `ready` deltaP `-5.4878` edge `-0.0447` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0231` n `146` status `ready` deltaP `-12.4079` edge `-0.1006` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-8.6703` n `146` status `ready` deltaP `15.6871` edge `0.4833` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-11.218` n `146` status `ready` deltaP `13.265` edge `0.4271` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.5375` n `146` status `ready` deltaP `-1.5989` edge `-0.1147` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2021` n `146` status `ready` deltaP `-20.6807` edge `-0.0529` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
