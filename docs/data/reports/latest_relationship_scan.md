# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T21:34:55.205409+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11621`

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

- `market_context_high->crypto_major_24h` score `2.6736` n `91` status `ready` deltaP `9.5086` edge `0.2802` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6009` n `91` status `ready` deltaP `18.5955` edge `0.2646` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.3814` n `96` status `ready` deltaP `11.4085` edge `0.0692` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.0973` n `96` status `ready` deltaP `6.7327` edge `0.1354` maxDD `-2.4411`
- `market_context_high->metal_4h` score `0.9695` n `96` status `ready` deltaP `15.9553` edge `0.032` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.7412` n `96` status `ready` deltaP `9.3242` edge `0.1017` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.7114` n `96` status `ready` deltaP `13.367` edge `0.0089` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.4986` n `96` status `ready` deltaP `9.6557` edge `-0.0001` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.26` n `96` status `ready` deltaP `9.9085` edge `0.0826` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.143` n `91` status `ready` deltaP `15.3446` edge `-0.069` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.0649` n `96` status `ready` deltaP `5.0711` edge `0.0103` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1861` n `96` status `ready` deltaP `3.9888` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.3552` n `96` status `ready` deltaP `3.0742` edge `0.0154` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3715` n `96` status `ready` deltaP `2.6759` edge `0.0147` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4483` n `96` status `ready` deltaP `-3.4182` edge `0.0012` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4627` n `96` status `ready` deltaP `2.5661` edge `0.0086` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4741` n `96` status `ready` deltaP `1.3348` edge `0.0148` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9079` n `96` status `ready` deltaP `-8.0402` edge `-0.0062` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.9667` n `91` status `ready` deltaP `-4.1971` edge `0.0529` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.2123` n `91` status `ready` deltaP `-26.1714` edge `-0.0266` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
