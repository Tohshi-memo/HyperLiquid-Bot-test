# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T15:53:33.985346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8829`

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

- `market_context_high->equity_4h` score `2.3247` n `96` status `ready` deltaP `12.2205` edge `0.2011` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.862` n `96` status `ready` deltaP `15.3007` edge `0.0833` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.2667` n `96` status `ready` deltaP `4.6875` edge `0.1951` maxDD `-4.9964`
- `market_context_high->index_1h` score `0.9079` n `96` status `ready` deltaP `15.6125` edge `0.0103` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.8603` n `96` status `ready` deltaP `15.9553` edge `0.0229` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.5069` n `96` status `ready` deltaP `8.5069` edge `0.1916` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.36` n `96` status `ready` deltaP `18.2291` edge `-0.0409` maxDD `-1.0505`
- `market_context_high->crypto_major_4h` score `0.2716` n `96` status `ready` deltaP `9.0193` edge `0.0646` maxDD `-3.1677`
- `market_context_high->index_4h` score `0.1312` n `96` status `ready` deltaP `8.1046` edge `0.0224` maxDD `-0.5728`
- `market_context_high->unknown_1h` score `0.109` n `96` status `ready` deltaP `7.4102` edge `-0.0176` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1079` n `96` status `ready` deltaP `8.7144` edge `0.006` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0238` n `96` status `ready` deltaP `4.4723` edge `0.0069` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3362` n `96` status `ready` deltaP `-1.4721` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_alt_4h` score `-0.4855` n `96` status `ready` deltaP `6.8598` edge `0.0408` maxDD `-5.4926`
- `market_context_high->crypto_major_1h` score `-0.6021` n `96` status `ready` deltaP `2.3827` edge `-0.0086` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.6217` n `96` status `ready` deltaP `0.8795` edge `-0.0054` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6239` n `96` status `ready` deltaP `0.1271` edge `0.0042` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8915` n `96` status `ready` deltaP `-7.5911` edge `-0.0071` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.4975` n `96` status `ready` deltaP `-5.7292` edge `0.0488` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.7114` n `96` status `ready` deltaP `-20.4861` edge `-0.0144` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
