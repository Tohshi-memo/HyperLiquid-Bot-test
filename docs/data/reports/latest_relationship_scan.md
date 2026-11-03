# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T08:22:36.284586+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4490`

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

- `news_risk_high->crypto_alt_4h` score `0.2309` n `146` status `ready` deltaP `5.9326` edge `0.2537` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.416` n `146` status `ready` deltaP `2.1819` edge `0.0549` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6202` n `146` status `ready` deltaP `-1.0253` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.8927` n `146` status `ready` deltaP `1.3473` edge `-0.0034` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.265` n `146` status `ready` deltaP `-4.6489` edge `-0.009` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.2689` n `146` status `ready` deltaP `-3.9634` edge `-0.0111` maxDD `-1.6794`
- `news_risk_high->metal_24h` score `-1.6926` n `141` status `ready` deltaP `9.8035` edge `0.1192` maxDD `-14.0483`
- `news_risk_high->index_4h` score `-2.0316` n `146` status `ready` deltaP `-2.6646` edge `-0.0126` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2493` n `141` status `ready` deltaP `-3.6865` edge `0.0204` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.39` n `146` status `ready` deltaP `-9.0764` edge `-0.002` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4009` n `141` status `ready` deltaP `-17.5716` edge `-0.0198` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6922` n `146` status `ready` deltaP `-6.7857` edge `-0.0323` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2367` n `146` status `ready` deltaP `-8.3053` edge `-0.0418` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9573` n `146` status `ready` deltaP `-13.2372` edge `-0.0061` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.7145` n `146` status `ready` deltaP `-6.5382` edge `-0.0288` maxDD `-9.3056`
- `news_risk_high->crypto_alt_24h` score `-5.2127` n `141` status `ready` deltaP `19.2524` edge `0.7377` maxDD `-107.0804`
- `news_risk_high->crypto_major_4h` score `-6.9778` n `146` status `ready` deltaP `-13.9263` edge `-0.0867` maxDD `-24.1554`
- `news_risk_high->equity_24h` score `-7.7646` n `141` status `ready` deltaP `14.3912` edge `0.4633` maxDD `-82.8366`
- `news_risk_high->equity_4h` score `-11.377` n `146` status `ready` deltaP `-0.9877` edge `-0.1054` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-12.852` n `141` status `ready` deltaP `-24.1134` edge `-0.0985` maxDD `-42.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
