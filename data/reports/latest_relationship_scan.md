# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T13:37:27.744406+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.1577` n `146` status `ready` deltaP `7.9143` edge `0.2311` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4271` n `146` status `ready` deltaP `3.6789` edge `0.0435` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7245` n `146` status `ready` deltaP `-2.9714` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7561` n `146` status `ready` deltaP `2.6946` edge `-0.001` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4481` n `146` status `ready` deltaP `-7.4695` edge `-0.0107` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5789` n `146` status `ready` deltaP `-8.9902` edge `-0.0203` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7615` n `146` status `ready` deltaP `1.2989` edge `-0.0044` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2472` n `146` status `ready` deltaP `-15.7701` edge `-0.0121` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.3911` n `146` status `ready` deltaP `-9.6752` edge `0.0019` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.4537` n `146` status `ready` deltaP `-4.8396` edge `-0.0147` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.9433` n `146` status `ready` deltaP `-12.3382` edge `-0.0109` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.0295` n `146` status `ready` deltaP `-5.6107` edge `-0.0425` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.6907` n `146` status `ready` deltaP `-13.0847` edge `0.0151` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.6853` n `146` status `ready` deltaP `-12.1784` edge `-0.0721` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.5293` n `146` status `ready` deltaP `-10.4202` edge `-0.0727` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-7.4039` n `146` status `ready` deltaP `-9.7508` edge `-0.1938` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.2812` n `146` status `ready` deltaP `-16.2695` edge `0.1611` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.4175` n `146` status `ready` deltaP `2.3659` edge `-0.0478` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-14.2728` n `146` status `ready` deltaP `9.8198` edge `0.1955` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.7698` n `146` status `ready` deltaP `2.3545` edge `-0.338` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
