# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T10:07:29.059987+00:00`
- Price records: `672`
- Market context records: `4817`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `11.9151` n `116` status `ready` deltaP `11.5476` edge `0.9577` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.792` n `116` status `ready` deltaP `17.8459` edge `0.6514` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.3157` n `109` status `ready` deltaP `12.879` edge `0.1942` maxDD `-4.3004`
- `market_context_high->equity_4h` score `0.3675` n `116` status `ready` deltaP `9.9401` edge `0.119` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.1663` n `116` status `ready` deltaP `13.0992` edge `0.0512` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.092` n `116` status `ready` deltaP `6.2151` edge `0.025` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.1258` n `116` status `ready` deltaP `7.8638` edge `0.0188` maxDD `-3.988`
- `market_context_high->fx_4h` score `-0.3228` n `116` status `ready` deltaP `4.9727` edge `0.0031` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6427` n `116` status `ready` deltaP `2.3229` edge `0.0077` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.0527` n `116` status `ready` deltaP `-2.8908` edge `-0.0035` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.374` n `116` status `ready` deltaP `-1.0479` edge `-0.0071` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1861` n `109` status `ready` deltaP `19.8761` edge `0.0981` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3381` n `116` status `ready` deltaP `-1.5435` edge `-0.0723` maxDD `-14.04`
- `market_context_high->fx_24h` score `-2.6866` n `109` status `ready` deltaP `-12.4857` edge `-0.0191` maxDD `-3.057`
- `market_context_high->crypto_alt_1h` score `-2.7118` n `116` status `ready` deltaP `2.3591` edge `-0.0404` maxDD `-13.7718`
- `market_context_high->crypto_major_1h` score `-2.8388` n `116` status `ready` deltaP `0.5936` edge `-0.0712` maxDD `-21.0696`
- `market_context_high->crypto_alt_4h` score `-4.1058` n `116` status `ready` deltaP `6.7967` edge `-0.0061` maxDD `-39.9142`
- `market_context_high->index_24h` score `-4.2776` n `109` status `ready` deltaP `-6.1147` edge `-0.1168` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-7.9231` n `116` status `ready` deltaP `3.8582` edge `-0.1678` maxDD `-64.5634`
- `market_context_high->metal_4h` score `-8.6014` n `116` status `ready` deltaP `5.0883` edge `-0.3171` maxDD `-60.899`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
