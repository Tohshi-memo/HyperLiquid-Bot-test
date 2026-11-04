# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T07:37:24.512589+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4404`

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

- `news_risk_high->crypto_alt_4h` score `0.5535` n `146` status `ready` deltaP `9.2863` edge `0.2727` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4426` n `146` status `ready` deltaP `2.3316` edge `0.0505` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7168` n `146` status `ready` deltaP `-2.8217` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7933` n `146` status `ready` deltaP `2.2455` edge `-0.0011` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2837` n `146` status `ready` deltaP `-4.6489` edge `-0.0114` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.4662` n `146` status `ready` deltaP `-7.622` edge `-0.012` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.6178` n `146` status `ready` deltaP `10.7354` edge `0.1518` maxDD `-16.6552`
- `news_risk_high->index_24h` score `-1.7133` n `146` status `ready` deltaP `1.5506` edge `0.0542` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.7739` n `146` status `ready` deltaP `0.5367` edge `-0.0009` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3446` n `146` status `ready` deltaP `-17.8534` edge `-0.0107` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4894` n `146` status `ready` deltaP `-10.274` edge `-0.0023` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5433` n `146` status `ready` deltaP `-5.139` edge `-0.0242` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0832` n `146` status `ready` deltaP `-7.2574` edge `-0.036` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.8678` n `146` status `ready` deltaP `-12.6274` edge `-0.0027` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.4756` n `146` status `ready` deltaP `-3.6418` edge `-0.0282` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.1547` n `146` status `ready` deltaP `-10.2677` edge `-0.0425` maxDD `-24.1554`
- `news_risk_high->crypto_alt_24h` score `-7.1607` n `146` status `ready` deltaP `19.3684` edge `0.6523` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-9.2574` n `146` status `ready` deltaP `16.9378` edge `0.566` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-10.6501` n `146` status `ready` deltaP `0.6891` edge `-0.056` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.3459` n `146` status `ready` deltaP `-20.7834` edge `-0.0642` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
