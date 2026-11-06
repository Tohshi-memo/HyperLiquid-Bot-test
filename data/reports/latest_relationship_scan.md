# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T06:22:26.105028+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4282`

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

- `news_risk_high->crypto_alt_4h` score `-0.0988` n `145` status `ready` deltaP `7.7061` edge `0.1996` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4456` n `145` status `ready` deltaP `4.0285` edge `0.0388` maxDD `-5.8225`
- `news_risk_high->index_1h` score `-0.6459` n `145` status `ready` deltaP `3.6382` edge `0.0019` maxDD `-1.3981`
- `news_risk_high->fx_1h` score `-0.7256` n `145` status `ready` deltaP `-3.0663` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->metal_1h` score `-1.4757` n `145` status `ready` deltaP `-7.5139` edge `-0.0184` maxDD `-2.9898`
- `news_risk_high->fx_4h` score `-1.477` n `145` status `ready` deltaP `-7.8143` edge `-0.0121` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.6564` n `145` status `ready` deltaP `1.0198` edge `0.0066` maxDD `-4.0609`
- `news_risk_high->index_24h` score `-2.2682` n `145` status `ready` deltaP `-11.8983` edge `0.0658` maxDD `-7.1819`
- `news_risk_high->equity_1h` score `-2.3349` n `145` status `ready` deltaP `-5.1456` edge `0.0019` maxDD `-16.3557`
- `news_risk_high->commodity_1h` score `-2.5537` n `145` status `ready` deltaP `-11.4382` edge `0.0001` maxDD `-3.2657`
- `news_risk_high->crypto_major_1h` score `-2.719` n `145` status `ready` deltaP `-4.6696` edge `-0.0229` maxDD `-9.4709`
- `news_risk_high->fx_24h` score `-2.8454` n `145` status `ready` deltaP `-25.4265` edge `-0.0296` maxDD `-2.255`
- `news_risk_high->commodity_4h` score `-4.0619` n `145` status `ready` deltaP `-16.1344` edge `0.0045` maxDD `-9.5011`
- `news_risk_high->crypto_major_4h` score `-5.3775` n `145` status `ready` deltaP `-8.4977` edge `-0.0092` maxDD `-22.915`
- `news_risk_high->metal_4h` score `-5.6476` n `145` status `ready` deltaP `-12.6714` edge `-0.0718` maxDD `-9.1483`
- `news_risk_high->metal_24h` score `-8.9741` n `145` status `ready` deltaP `-16.6173` edge `-0.2912` maxDD `-16.0021`
- `news_risk_high->equity_24h` score `-9.0551` n `145` status `ready` deltaP `10.3604` edge `0.5887` maxDD `-99.6557`
- `news_risk_high->equity_4h` score `-9.6342` n `145` status `ready` deltaP `1.4771` edge `0.0087` maxDD `-51.3786`
- `news_risk_high->commodity_24h` score `-10.2096` n `145` status `ready` deltaP `-17.3296` edge `0.0908` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.2401` n `145` status `ready` deltaP `7.2485` edge `0.0819` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
