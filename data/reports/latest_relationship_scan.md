# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T09:22:29.253057+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3702`

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

- `news_risk_high->crypto_alt_4h` score `-0.353` n `146` status `ready` deltaP `6.2375` edge `0.1768` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6437` n `146` status `ready` deltaP `1.8825` edge `0.0277` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7245` n `146` status `ready` deltaP `-2.9714` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7394` n `146` status `ready` deltaP `2.8443` edge `-0.0006` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.5248` n `146` status `ready` deltaP `-8.689` edge `-0.0124` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5617` n `146` status `ready` deltaP `-8.8405` edge `-0.0191` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7102` n `146` status `ready` deltaP `2.0611` edge `-0.0029` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1682` n `146` status `ready` deltaP `-7.7291` edge `0.0075` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4038` n `146` status `ready` deltaP `-18.3178` edge `-0.0152` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5589` n `146` status `ready` deltaP `-5.8875` edge `-0.0212` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8897` n `146` status `ready` deltaP `-12.1628` edge `-0.0052` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.281` n `146` status `ready` deltaP `-10.7982` edge `0.034` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3928` n `146` status `ready` deltaP `-7.4071` edge `-0.0608` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4836` n `146` status `ready` deltaP `-10.1967` edge `-0.0685` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.7292` n `146` status `ready` deltaP `-6.9417` edge `-0.1563` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.3687` n `146` status `ready` deltaP `-11.7921` edge `-0.1335` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-9.98` n `146` status `ready` deltaP `-19.1236` edge `0.1219` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7045` n `146` status `ready` deltaP `1.2989` edge `-0.0646` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.851` n `146` status `ready` deltaP `9.9778` edge `0.2296` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-14.7385` n `146` status `ready` deltaP `4.7875` edge `-0.222` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
