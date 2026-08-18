# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T15:37:33.495662+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11630`

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

- `market_context_high->crypto_major_24h` score `2.4263` n `91` status `ready` deltaP `9.6121` edge `0.2589` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.7451` n `91` status `ready` deltaP `19.3727` edge `0.2779` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.2352` n `96` status `ready` deltaP `10.3606` edge `0.064` maxDD `-0.4112`
- `market_context_high->metal_4h` score `0.7175` n `96` status `ready` deltaP `14.126` edge `0.0232` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6959` n `96` status `ready` deltaP `13.2173` edge `0.0086` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5382` n `96` status `ready` deltaP `9.506` edge `0.0042` maxDD `-0.4843`
- `market_context_high->crypto_major_4h` score `0.406` n `96` status `ready` deltaP `8.1046` edge `0.0819` maxDD `-3.1677`
- `market_context_high->equity_4h` score `0.2096` n `96` status `ready` deltaP `3.2266` edge `0.0848` maxDD `-2.4411`
- `market_context_high->metal_1h` score `-0.0058` n `96` status `ready` deltaP `4.3226` edge `0.0094` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.0166` n `96` status `ready` deltaP `8.5366` edge `0.0687` maxDD `-5.4926`
- `market_context_high->fx_4h` score `-0.2084` n `96` status `ready` deltaP `3.5315` edge `0.0` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.3103` n `91` status `ready` deltaP `11.4785` edge `-0.081` maxDD `-0.3771`
- `market_context_high->commodity_4h` score `-0.3727` n `96` status `ready` deltaP `3.938` edge `0.011` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4794` n `96` status `ready` deltaP `-4.017` edge `0.0012` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.4938` n `96` status `ready` deltaP `1.1789` edge `0.009` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.591` n `96` status `ready` deltaP `0.2869` edge `0.0068` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6335` n `96` status `ready` deltaP `0.3303` edge `0.0105` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8565` n `96` status `ready` deltaP `-7.142` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.4695` n `91` status `ready` deltaP `-8.2579` edge `0.0155` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.5765` n `91` status `ready` deltaP `-30.2436` edge `-0.0298` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
