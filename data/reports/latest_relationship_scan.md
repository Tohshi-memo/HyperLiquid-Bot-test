# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T06:22:24.092812+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.6877` n `146` status `ready` deltaP `9.2863` edge `0.2899` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4215` n `146` status `ready` deltaP `2.4813` edge `0.0522` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7004` n `146` status `ready` deltaP `-2.5223` edge `-0.0029` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7549` n `146` status `ready` deltaP `2.6946` edge `-0.0009` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2868` n `146` status `ready` deltaP `-4.7986` edge `-0.0108` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.4404` n `146` status `ready` deltaP `11.6034` edge `0.1608` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.4638` n `146` status `ready` deltaP `-7.622` edge `-0.0117` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.6565` n `146` status `ready` deltaP `2.4187` edge `0.0557` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7481` n `146` status `ready` deltaP `0.5367` edge `0.0024` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3368` n `146` status `ready` deltaP `-17.8534` edge `-0.0097` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4414` n `146` status `ready` deltaP `-9.8249` edge `-0.0013` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.527` n `146` status `ready` deltaP `-5.139` edge `-0.0221` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0928` n `146` status `ready` deltaP `-7.2574` edge `-0.0368` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8244` n `146` status `ready` deltaP `-12.475` edge `-0.0001` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3526` n `146` status `ready` deltaP `-3.1845` edge `-0.021` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.0347` n `146` status `ready` deltaP `-10.2677` edge `-0.0325` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.7646` n `146` status `ready` deltaP `20.2364` edge `0.6973` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-8.7859` n `146` status `ready` deltaP `17.8059` edge `0.5995` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.4053` n `146` status `ready` deltaP `0.6891` edge `-0.0356` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3435` n `146` status `ready` deltaP `-20.7834` edge `-0.064` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
