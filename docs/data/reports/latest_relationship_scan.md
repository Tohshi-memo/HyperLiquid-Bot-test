# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T11:22:28.513540+00:00`
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

- `market_context_high->crypto_major_24h` score `2.0248` n `96` status `ready` deltaP `6.4236` edge `0.2467` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.8207` n `96` status `ready` deltaP `10.3912` edge `0.1713` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6881` n `96` status `ready` deltaP `14.2528` edge `0.0758` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3078` n `96` status `ready` deltaP `18.6992` edge `0.0419` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9917` n `96` status `ready` deltaP `11.001` edge `0.1114` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.9162` n `96` status `ready` deltaP `15.7622` edge `0.01` maxDD `-0.0982`
- `market_context_high->commodity_24h` score `0.8667` n `96` status `ready` deltaP `11.6319` edge `0.2169` maxDD `-4.666`
- `market_context_high->unknown_1h` score `0.1989` n `96` status `ready` deltaP `8.1587` edge `-0.0151` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1871` n `96` status `ready` deltaP `6.2687` edge `0.0125` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `0.1494` n `96` status `ready` deltaP `17.1875` edge `-0.0515` maxDD `-1.0505`
- `market_context_high->crypto_alt_4h` score `0.1164` n `96` status `ready` deltaP `9.2988` edge `0.0747` maxDD `-5.4926`
- `market_context_high->fx_4h` score `0.1143` n `96` status `ready` deltaP `8.8668` edge `0.0058` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.0887` n `96` status `ready` deltaP `7.6473` edge `0.0219` maxDD `-0.5728`
- `market_context_high->fx_1h` score `-0.3183` n `96` status `ready` deltaP `-1.1727` edge `0.0029` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3425` n `96` status `ready` deltaP `3.4306` edge `0.0177` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4455` n `96` status `ready` deltaP `1.7777` edge `0.0112` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5671` n `96` status `ready` deltaP `0.8893` edge `0.0064` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8939` n `96` status `ready` deltaP `-7.7408` edge `-0.0064` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2113` n `96` status `ready` deltaP `-3.6458` edge `0.0716` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.9898` n `96` status `ready` deltaP `-22.9166` edge `-0.0214` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
