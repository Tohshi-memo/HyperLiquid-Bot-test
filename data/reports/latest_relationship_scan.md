# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T03:52:24.495556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.1827` n `95` status `ready` deltaP `7.3319` edge `0.2538` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.6031` n `96` status `ready` deltaP `13.3546` edge `0.0747` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.52` n `96` status `ready` deltaP `8.8668` edge `0.1564` maxDD `-2.4411`
- `market_context_high->commodity_24h` score `1.3392` n `95` status `ready` deltaP `16.3378` edge `0.2461` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.1538` n `96` status `ready` deltaP `17.4796` edge `0.0372` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9741` n `96` status `ready` deltaP `11.3059` edge `0.1079` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.8588` n `96` status `ready` deltaP `15.0137` edge `0.0102` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.3776` n `96` status `ready` deltaP `10.8232` edge `0.0863` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.369` n `96` status `ready` deltaP `9.506` edge `-0.0099` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1236` n `96` status `ready` deltaP `5.6699` edge `0.0112` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.009` n `96` status `ready` deltaP `6.8851` edge `0.0032` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.0221` n `96` status `ready` deltaP `6.4278` edge `0.0208` maxDD `-0.5728`
- `market_context_high->unknown_24h` score `-0.3061` n `95` status `ready` deltaP `13.5179` edge `-0.0707` maxDD `-0.9275`
- `market_context_high->fx_1h` score `-0.3292` n `96` status `ready` deltaP `-1.3224` edge `0.0025` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.3434` n `96` status `ready` deltaP `3.125` edge `0.0153` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.397` n `96` status `ready` deltaP `2.5324` edge `0.0167` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.5039` n `96` status `ready` deltaP `1.8039` edge `0.0084` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8549` n `96` status `ready` deltaP `-7.142` edge `-0.0054` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1339` n `95` status `ready` deltaP `-3.1195` edge `0.0674` maxDD `-10.9474`
- `market_context_high->fx_24h` score `-4.2522` n `95` status `ready` deltaP `-25.2796` edge `-0.0293` maxDD `-1.8547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
