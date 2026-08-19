# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T11:52:29.993254+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11750`

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

- `market_context_high->crypto_major_24h` score `1.9587` n `96` status `ready` deltaP `6.0764` edge `0.2435` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.9099` n `96` status `ready` deltaP `10.6961` edge `0.1767` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7313` n `96` status `ready` deltaP `14.5522` edge `0.0774` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.2774` n `96` status `ready` deltaP `18.3943` edge `0.0414` maxDD `-1.273`
- `market_context_high->index_1h` score `0.9414` n `96` status `ready` deltaP `16.0616` edge `0.0101` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.9289` n `96` status `ready` deltaP `10.6961` edge `0.1082` maxDD `-3.1677`
- `market_context_high->commodity_24h` score `0.8284` n `96` status `ready` deltaP `11.2847` edge `0.2143` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.2048` n `96` status `ready` deltaP `17.5347` edge `-0.0492` maxDD `-1.0505`
- `market_context_high->metal_1h` score `0.1716` n `96` status `ready` deltaP `6.119` edge `0.0122` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `0.1629` n `96` status `ready` deltaP `7.8593` edge `-0.0161` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1325` n `96` status `ready` deltaP `9.1717` edge `0.0061` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.1191` n `96` status `ready` deltaP `7.9522` edge `0.0224` maxDD `-0.5728`
- `market_context_high->crypto_alt_4h` score `0.0668` n `96` status `ready` deltaP `8.9939` edge `0.0726` maxDD `-5.4926`
- `market_context_high->fx_1h` score `-0.3183` n `96` status `ready` deltaP `-1.1727` edge `0.0029` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3425` n `96` status `ready` deltaP `3.4306` edge `0.0177` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.447` n `96` status `ready` deltaP `1.7777` edge `0.011` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5702` n `96` status `ready` deltaP `0.8893` edge `0.006` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.883` n `96` status `ready` deltaP `-7.5911` edge `-0.006` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2144` n `96` status `ready` deltaP `-3.6458` edge `0.0712` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.9513` n `96` status `ready` deltaP `-22.5694` edge `-0.0205` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
