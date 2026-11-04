# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-04T01:22:24.277518+00:00`
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

- `news_risk_high->crypto_alt_4h` score `0.5057` n `146` status `ready` deltaP `8.9814` edge `0.2686` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3061` n `146` status `ready` deltaP `3.0801` edge `0.063` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.702` n `146` status `ready` deltaP `-2.5223` edge `-0.0031` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8124` n `146` status `ready` deltaP `1.9461` edge `-0.0007` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.1747` n `146` status `ready` deltaP `-3.3016` edge `-0.0064` maxDD `-3.1082`
- `news_risk_high->metal_24h` score `-1.38` n `146` status `ready` deltaP `12.2979` edge `0.1612` maxDD `-16.6552`
- `news_risk_high->fx_4h` score `-1.467` n `146` status `ready` deltaP `-7.622` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7151` n `146` status `ready` deltaP `2.0715` edge `0.0505` maxDD `-7.402`
- `news_risk_high->index_4h` score `-1.9157` n `146` status `ready` deltaP `-1.1402` edge `-0.0079` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.2357` n `146` status `ready` deltaP `-16.4645` edge `-0.006` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5301` n `146` status `ready` deltaP `-10.7231` edge `-0.0027` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-2.5799` n `146` status `ready` deltaP `-6.3366` edge `-0.0209` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.0053` n `146` status `ready` deltaP `-7.1077` edge `-0.0305` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-4.0495` n `146` status `ready` deltaP `-13.9994` edge `-0.0087` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.3456` n `146` status `ready` deltaP `-3.3369` edge `-0.0194` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.955` n `146` status `ready` deltaP `22.3198` edge `0.7872` maxDD `-118.6236`
- `news_risk_high->crypto_major_4h` score `-6.5029` n `146` status `ready` deltaP `-11.3348` edge `-0.0644` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-8.3119` n `146` status `ready` deltaP `19.0212` edge `0.6309` maxDD `-102.3626`
- `news_risk_high->equity_4h` score `-11.2716` n `146` status `ready` deltaP `-1.1402` edge `-0.0956` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.2952` n `146` status `ready` deltaP `-20.089` edge `-0.0646` maxDD `-43.7525`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
