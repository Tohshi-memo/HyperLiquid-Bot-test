# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T03:07:30.920813+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3809`

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

- `news_risk_high->crypto_alt_4h` score `-0.4205` n `146` status `ready` deltaP `6.6948` edge `0.1651` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6702` n `146` status `ready` deltaP `1.5831` edge `0.0263` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7417` n `146` status `ready` deltaP `-3.2708` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8113` n `146` status `ready` deltaP `2.2455` edge `-0.0026` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5321` n `146` status `ready` deltaP `-8.3914` edge `-0.0183` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5881` n `146` status `ready` deltaP `-9.7561` edge `-0.0134` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8838` n `146` status `ready` deltaP `-0.378` edge `-0.0089` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1514` n `146` status `ready` deltaP `-7.7291` edge `0.0089` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4367` n `146` status `ready` deltaP `-18.6638` edge `-0.0171` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6477` n `146` status `ready` deltaP `-6.636` edge `-0.0276` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.6886` n `146` status `ready` deltaP `-10.6057` edge `0.0102` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.19` n `146` status `ready` deltaP `-10.036` edge `0.0365` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4611` n `146` status `ready` deltaP `-7.8562` edge `-0.0635` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.291` n `146` status `ready` deltaP `-8.8248` edge `-0.0616` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-5.4244` n `146` status `ready` deltaP `-2.6165` edge `-0.0764` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.7578` n `146` status `ready` deltaP `-13.0116` edge `-0.1578` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.9894` n `146` status `ready` deltaP `-20.1616` edge `0.0447` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-11.0265` n `146` status `ready` deltaP `0.0793` edge `-0.0833` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-12.6283` n `146` status `ready` deltaP `9.1127` edge `0.0197` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-13.0263` n `146` status `ready` deltaP `11.0158` edge `0.2914` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
