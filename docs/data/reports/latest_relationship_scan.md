# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T10:37:27.716288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3528`

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

- `news_risk_high->crypto_alt_4h` score `-0.2858` n `146` status `ready` deltaP `6.3899` edge `0.1844` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5783` n `146` status `ready` deltaP `2.4813` edge `0.0321` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6903` n `146` status `ready` deltaP `-2.3726` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7669` n `146` status `ready` deltaP `2.5449` edge `-0.0009` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.4971` n `146` status `ready` deltaP `-8.2317` edge `-0.0119` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.5446` n `146` status `ready` deltaP `-8.5411` edge `-0.0189` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-1.7608` n `146` status `ready` deltaP `1.2989` edge `-0.0043` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.2353` n `146` status `ready` deltaP `-8.3279` edge `0.0059` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.3456` n `146` status `ready` deltaP `-17.4527` edge `-0.0135` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5729` n `146` status `ready` deltaP `-6.0372` edge `-0.022` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8999` n `146` status `ready` deltaP `-12.1628` edge `-0.0065` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.3292` n `146` status `ready` deltaP `-7.2574` edge `-0.0565` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.4224` n `146` status `ready` deltaP `-11.5604` edge `0.0273` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.548` n `146` status `ready` deltaP `-10.8065` edge `-0.0698` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-6.916` n `146` status `ready` deltaP `-7.8068` edge `-0.1661` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.2103` n `146` status `ready` deltaP `-11.7921` edge `-0.1203` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-9.75` n `146` status `ready` deltaP `-18.2585` edge `0.1353` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.7599` n `146` status `ready` deltaP `1.1464` edge `-0.0682` maxDD `-52.2214`
- `news_risk_high->equity_24h` score `-13.8894` n `146` status `ready` deltaP `9.9778` edge `0.2264` maxDD `-102.3626`
- `news_risk_high->crypto_alt_24h` score `-15.0736` n `146` status `ready` deltaP `3.9224` edge `-0.2592` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
