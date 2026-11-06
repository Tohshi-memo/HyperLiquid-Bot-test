# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T02:22:32.857292+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4314`

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

- `news_risk_high->crypto_alt_4h` score `-0.3266` n `146` status `ready` deltaP `6.9254` edge `0.1756` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6469` n `146` status `ready` deltaP `2.631` edge `0.0223` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6965` n `146` status `ready` deltaP `-2.5223` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7261` n `146` status `ready` deltaP `2.6946` edge `0.0015` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4261` n `146` status `ready` deltaP `-6.9254` edge `-0.0115` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5361` n `146` status `ready` deltaP `-8.2417` edge `-0.0198` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.6724` n `146` status `ready` deltaP `0.9132` edge `0.0096` maxDD `-4.0745`
- `news_risk_high->equity_1h` score `-2.4426` n `146` status `ready` deltaP `-6.1869` edge `-0.0043` maxDD `-16.4088`
- `news_risk_high->commodity_1h` score `-2.4474` n `146` status `ready` deltaP `-10.4237` edge `0.0022` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.4872` n `146` status `ready` deltaP `-12.1628` edge `0.0464` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.7462` n `146` status `ready` deltaP `-23.1621` edge `-0.0268` maxDD `-2.336`
- `news_risk_high->crypto_major_1h` score `-3.0391` n `146` status `ready` deltaP `-5.7604` edge `-0.0423` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8656` n `146` status `ready` deltaP `-14.5358` edge `0.0102` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.7496` n `146` status `ready` deltaP `-12.8615` edge `-0.0729` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.0713` n `146` status `ready` deltaP `-9.2847` edge `-0.0421` maxDD `-24.1554`
- `news_risk_high->metal_24h` score `-9.1532` n `146` status `ready` deltaP `-16.9763` edge `-0.2914` maxDD `-16.6552`
- `news_risk_high->commodity_24h` score `-9.4731` n `146` status `ready` deltaP `-14.7983` edge `0.1353` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-9.4753` n `146` status `ready` deltaP `1.9787` edge `0.0333` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-10.9266` n `146` status `ready` deltaP `9.9778` edge `0.4733` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-13.9093` n `146` status `ready` deltaP `4.7875` edge `-0.1157` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
