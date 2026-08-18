# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T19:52:39.241908+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11624`

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

- `market_context_high->crypto_major_24h` score `2.7297` n `91` status `ready` deltaP `10.0294` edge `0.2814` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6643` n `91` status `ready` deltaP `19.2899` edge `0.2681` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.2735` n `96` status `ready` deltaP `10.5103` edge `0.0662` maxDD `-0.4112`
- `market_context_high->equity_4h` score `0.8907` n `96` status `ready` deltaP `5.6656` edge `0.1253` maxDD `-2.4411`
- `market_context_high->metal_4h` score `0.8565` n `96` status `ready` deltaP `14.8882` edge `0.0297` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6827` n `96` status `ready` deltaP `13.0676` edge `0.0085` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.6238` n `96` status `ready` deltaP `8.562` edge `0.097` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.4974` n `96` status `ready` deltaP `9.506` edge `0.0008` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.11` n `96` status `ready` deltaP `8.9939` edge `0.0762` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.0098` n `96` status `ready` deltaP `4.4723` edge `0.0097` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `0.0014` n `91` status `ready` deltaP `14.1293` edge `-0.0727` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.1941` n `96` status `ready` deltaP `3.8363` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->crypto_alt_1h` score `-0.433` n `96` status `ready` deltaP `1.9274` edge `0.0118` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4397` n `96` status `ready` deltaP `-3.2685` edge `0.0013` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4438` n `96` status `ready` deltaP `2.871` edge `0.009` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.4514` n `96` status `ready` deltaP `2.0071` edge `0.0145` maxDD `-0.5728`
- `market_context_high->crypto_major_1h` score `-0.5489` n `96` status `ready` deltaP `0.4366` edge `0.0112` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8635` n `96` status `ready` deltaP `-7.2917` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1203` n `91` status `ready` deltaP `-5.4124` edge `0.0413` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.3203` n `91` status `ready` deltaP `-27.3867` edge `-0.0275` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
