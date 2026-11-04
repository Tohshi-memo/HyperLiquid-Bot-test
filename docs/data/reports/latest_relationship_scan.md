# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T06:37:33.903359+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4411`

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

- `news_risk_high->crypto_alt_4h` score `0.6651` n `146` status `ready` deltaP `9.2863` edge `0.287` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.441` n `146` status `ready` deltaP `2.3316` edge `0.0507` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.709` n `146` status `ready` deltaP `-2.672` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7561` n `146` status `ready` deltaP `2.6946` edge `-0.001` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2915` n `146` status `ready` deltaP `-4.7986` edge `-0.0114` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4646` n `146` status `ready` deltaP `-7.622` edge `-0.0118` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.4747` n `146` status `ready` deltaP `11.4298` edge `0.1591` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.667` n `146` status `ready` deltaP `2.2451` edge `0.0555` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.752` n `146` status `ready` deltaP `0.5367` edge `0.0019` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3384` n `146` status `ready` deltaP `-17.8534` edge `-0.0099` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4438` n `146` status `ready` deltaP `-9.8249` edge `-0.0015` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5394` n `146` status `ready` deltaP `-5.139` edge `-0.0237` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.112` n `146` status `ready` deltaP `-7.4071` edge `-0.0374` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.845` n `146` status `ready` deltaP `-12.6274` edge `-0.0008` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3804` n `146` status `ready` deltaP `-3.3369` edge `-0.0223` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.0515` n `146` status `ready` deltaP `-10.2677` edge `-0.0339` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.8376` n `146` status `ready` deltaP `20.0628` edge `0.6891` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-8.8754` n `146` status `ready` deltaP `17.6323` edge `0.5932` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.4497` n `146` status `ready` deltaP `0.6891` edge `-0.0393` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3471` n `146` status `ready` deltaP `-20.7834` edge `-0.0643` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
