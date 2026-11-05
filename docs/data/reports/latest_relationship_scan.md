# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T20:07:34.919907+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4194`

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

- `news_risk_high->crypto_alt_4h` score `0.2781` n `146` status `ready` deltaP `8.2953` edge `0.244` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3147` n `146` status `ready` deltaP `3.3795` edge `0.0599` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6614` n `146` status `ready` deltaP `3.2934` edge `0.0029` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7292` n `146` status `ready` deltaP `-3.1211` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->fx_4h` score `-1.4728` n `146` status `ready` deltaP `-7.8387` edge `-0.0114` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5493` n `146` status `ready` deltaP `-8.5411` edge `-0.0195` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6439` n `146` status `ready` deltaP `1.5221` edge `0.0092` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.2384` n `146` status `ready` deltaP `-4.8396` edge `0.0129` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4006` n `146` status `ready` deltaP `-9.8249` edge `0.0021` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4626` n `146` status `ready` deltaP `-18.9525` edge `-0.0185` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-2.7103` n `146` status `ready` deltaP `-5.3113` edge `-0.0179` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-2.7968` n `146` status `ready` deltaP `-12.2504` edge `0.0073` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.766` n `146` status `ready` deltaP `-13.4704` edge `0.0114` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.683` n `146` status `ready` deltaP `-12.4049` edge `-0.0704` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-5.828` n `146` status `ready` deltaP `-9.5891` edge `-0.0198` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-8.4831` n `146` status `ready` deltaP `-14.1497` edge `-0.2544` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-8.9711` n `146` status `ready` deltaP `-14.4928` edge `0.1751` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.2552` n `146` status `ready` deltaP `2.4353` edge `0.0486` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.4601` n `146` status `ready` deltaP `9.8989` edge `0.2627` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.9917` n `146` status `ready` deltaP `1.9266` edge `-0.3636` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
