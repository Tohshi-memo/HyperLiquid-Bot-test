# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T02:07:29.104649+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `-0.4457` n `146` status `ready` deltaP `6.3899` edge `0.1639` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6017` n `146` status `ready` deltaP `2.1819` edge `0.0311` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7253` n `146` status `ready` deltaP `-2.9714` edge `-0.0031` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8065` n `146` status `ready` deltaP `2.2455` edge `-0.0022` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4924` n `146` status `ready` deltaP `-7.7926` edge `-0.0172` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5627` n `146` status `ready` deltaP `-9.2988` edge `-0.0132` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9335` n `146` status `ready` deltaP `-0.9877` edge `-0.0112` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1095` n `146` status `ready` deltaP `-7.28` edge `0.0094` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4382` n `146` status `ready` deltaP `-18.6638` edge `-0.0173` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5955` n `146` status `ready` deltaP `-6.1869` edge `-0.0239` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.609` n `146` status `ready` deltaP `-9.9137` edge `0.0158` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1996` n `146` status `ready` deltaP `-10.036` edge `0.0357` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4443` n `146` status `ready` deltaP `-7.8562` edge `-0.0621` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-5.153` n `146` status `ready` deltaP `-1.9244` edge `-0.0584` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.1918` n `146` status `ready` deltaP `-8.215` edge `-0.0574` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.8316` n `146` status `ready` deltaP `-13.469` edge `-0.1609` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.164` n `146` status `ready` deltaP `-0.5304` edge `-0.0907` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-11.1689` n `146` status `ready` deltaP `-20.6807` edge `0.0332` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.0627` n `146` status `ready` deltaP `9.8048` edge `0.0876` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-12.6242` n `146` status `ready` deltaP `11.7079` edge `0.3203` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
