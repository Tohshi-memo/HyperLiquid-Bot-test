# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T16:07:53.678624+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4372`

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

- `news_risk_high->crypto_alt_4h` score `0.2126` n `146` status `ready` deltaP `6.3899` edge `0.2483` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4667` n `146` status `ready` deltaP `1.7328` edge `0.0514` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6638` n `146` status `ready` deltaP `-1.7738` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9095` n `146` status `ready` deltaP `1.0479` edge `-0.0028` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1801` n `146` status `ready` deltaP `-3.3016` edge `-0.0071` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.405` n `146` status `ready` deltaP `-6.25` edge `-0.0133` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.7186` n `146` status `ready` deltaP `11.9506` edge `0.1353` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.8623` n `146` status `ready` deltaP `0.3354` edge `0.0432` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.0358` n `146` status `ready` deltaP `-2.9694` edge `-0.0111` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3051` n `146` status `ready` deltaP `-16.4645` edge `-0.0149` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5086` n `146` status `ready` deltaP `-10.4237` edge `-0.0029` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.6991` n `146` status `ready` deltaP `-7.0851` edge `-0.0312` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2522` n `146` status `ready` deltaP `-8.455` edge `-0.0421` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.1773` n `146` status `ready` deltaP `-15.3713` edge `-0.0102` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4806` n `146` status `ready` deltaP `-4.7089` edge `-0.0215` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.7599` n `146` status `ready` deltaP `22.667` edge `0.8099` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.9054` n `146` status `ready` deltaP `-13.6214` edge `-0.0827` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3419` n `146` status `ready` deltaP `17.8059` edge `0.6365` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.3096` n `146` status `ready` deltaP `-0.8353` edge `-0.1008` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3573` n `146` status `ready` deltaP `-20.6098` edge `-0.0663` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
