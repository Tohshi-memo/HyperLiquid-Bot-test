# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T21:07:33.249382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3872`

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

- `news_risk_high->crypto_alt_4h` score `0.2309` n `146` status `ready` deltaP `8.6765` edge `0.2354` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3959` n `146` status `ready` deltaP `3.3795` edge `0.0495` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6654` n `146` status `ready` deltaP `-1.9235` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8101` n `146` status `ready` deltaP `2.2455` edge `-0.0025` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4161` n `146` status `ready` deltaP `-6.7447` edge `-0.0144` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.464` n `146` status `ready` deltaP `-7.7744` edge `-0.0107` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9066` n `146` status `ready` deltaP `-0.5304` edge `-0.0108` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2185` n `146` status `ready` deltaP `-8.3279` edge `0.0073` maxDD `-3.2657`
- `news_risk_high->index_24h` score `-2.3273` n `146` status `ready` deltaP `-6.6265` edge `0.03` maxDD `-7.402`
- `news_risk_high->fx_24h` score `-2.4574` n `146` status `ready` deltaP `-18.8368` edge `-0.0186` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5931` n `146` status `ready` deltaP `-6.3366` edge `-0.0226` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1757` n `146` status `ready` deltaP `-6.6586` edge `-0.0477` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.2236` n `146` status `ready` deltaP `-10.036` edge `0.0337` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-4.0626` n `146` status `ready` deltaP `1.5358` edge `0.0094` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-4.9397` n `146` status `ready` deltaP `-6.2333` edge `-0.0496` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0379` n `146` status `ready` deltaP `-11.1824` edge `-0.11` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-9.5911` n `146` status `ready` deltaP `13.265` edge `0.3814` maxDD `-118.6236`
- `news_risk_high->equity_4h` score `-10.9739` n `146` status `ready` deltaP `-0.0731` edge `-0.0779` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-11.6515` n `146` status `ready` deltaP `11.8809` edge `0.4002` maxDD `-102.3626`
- `news_risk_high->commodity_24h` score `-11.8457` n `146` status `ready` deltaP `-20.6807` edge `-0.0232` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
