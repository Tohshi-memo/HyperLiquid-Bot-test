# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T07:07:28.699733+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4407`

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

- `news_risk_high->crypto_alt_4h` score `0.612` n `146` status `ready` deltaP `9.2863` edge `0.2802` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4426` n `146` status `ready` deltaP `2.3316` edge `0.0505` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7175` n `146` status `ready` deltaP `-2.8217` edge `-0.0031` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7681` n `146` status `ready` deltaP `2.5449` edge `-0.001` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2931` n `146` status `ready` deltaP `-4.7986` edge `-0.0116` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4662` n `146` status `ready` deltaP `-7.622` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.5433` n `146` status `ready` deltaP `11.0826` edge `0.1557` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.6898` n `146` status `ready` deltaP `1.8979` edge `0.0549` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7637` n `146` status `ready` deltaP `0.5367` edge `0.0004` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3423` n `146` status `ready` deltaP `-17.8534` edge `-0.0104` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4594` n `146` status `ready` deltaP `-9.9746` edge `-0.0018` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5433` n `146` status `ready` deltaP `-5.139` edge `-0.0242` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0928` n `146` status `ready` deltaP `-7.2574` edge `-0.0368` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8582` n `146` status `ready` deltaP `-12.6274` edge `-0.0019` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4274` n `146` status `ready` deltaP `-3.4894` edge `-0.0252` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.0995` n `146` status `ready` deltaP `-10.2677` edge `-0.0379` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-6.996` n `146` status `ready` deltaP `19.7156` edge `0.6711` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-9.064` n `146` status `ready` deltaP `17.2851` edge `0.5798` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.5469` n `146` status `ready` deltaP `0.6891` edge `-0.0474` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3471` n `146` status `ready` deltaP `-20.7834` edge `-0.0643` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
