# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T06:37:31.385630+00:00`
- Price records: `672`
- Market context records: `4802`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7530`

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

- `market_context_high->unknown_1h` score `10.8037` n `121` status `ready` deltaP `12.1456` edge `0.8611` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.786` n `120` status `ready` deltaP `18.8516` edge `0.6442` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.3555` n `114` status `ready` deltaP `13.4137` edge `0.1992` maxDD `-4.7201`
- `market_context_high->equity_4h` score `0.2804` n `120` status `ready` deltaP `9.7866` edge `0.1228` maxDD `-7.5011`
- `market_context_high->commodity_4h` score `0.0835` n `120` status `ready` deltaP `12.0935` edge `0.0473` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0222` n `121` status `ready` deltaP `4.9822` edge `0.0274` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.2285` n `120` status `ready` deltaP `8.5061` edge `0.0193` maxDD `-5.4242`
- `market_context_high->fx_4h` score `-0.3488` n `120` status `ready` deltaP `4.4716` edge `0.0031` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.5854` n `121` status `ready` deltaP `2.8146` edge `0.0092` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.8698` n `121` status `ready` deltaP `-0.725` edge `-0.0027` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.2664` n `121` status `ready` deltaP `-0.1076` edge `-0.0044` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.0622` n `114` status `ready` deltaP `20.2485` edge `0.1115` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2132` n `121` status `ready` deltaP `-0.2821` edge `-0.0643` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-2.9165` n `114` status `ready` deltaP `-11.906` edge `-0.0182` maxDD `-3.304`
- `market_context_high->crypto_alt_1h` score `-2.9615` n `121` status `ready` deltaP `1.6108` edge `-0.0371` maxDD `-14.9676`
- `market_context_high->crypto_major_1h` score `-4.3602` n `121` status `ready` deltaP `1.377` edge `-0.0635` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.5975` n `120` status `ready` deltaP `6.2296` edge `0.0032` maxDD `-45.3985`
- `market_context_high->index_24h` score `-6.9632` n `114` status `ready` deltaP `-8.4887` edge `-0.1302` maxDD `-23.4779`
- `market_context_high->crypto_major_4h` score `-8.1159` n `120` status `ready` deltaP `3.435` edge `-0.1403` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.351` n `120` status `ready` deltaP `6.5752` edge `-0.2904` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
