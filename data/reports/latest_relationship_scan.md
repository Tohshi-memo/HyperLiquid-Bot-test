# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T22:52:24.524245+00:00`
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

- `market_context_high->crypto_major_24h` score `2.543` n `91` status `ready` deltaP `8.6405` edge `0.2751` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5657` n `91` status `ready` deltaP `18.2483` edge `0.2624` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.4305` n `96` status `ready` deltaP `11.8576` edge `0.0703` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.2266` n `96` status `ready` deltaP `7.4949` edge `0.1411` maxDD `-2.4411`
- `market_context_high->metal_4h` score `1.0544` n `96` status `ready` deltaP `16.7174` edge `0.034` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.82` n `96` status `ready` deltaP `9.9339` edge `0.1042` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.6995` n `96` status `ready` deltaP `13.2173` edge `0.0089` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.4662` n `96` status `ready` deltaP `9.506` edge `-0.0018` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.375` n `96` status `ready` deltaP `10.6707` edge `0.0871` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.1912` n `91` status `ready` deltaP `15.6918` edge `-0.0673` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.0925` n `96` status `ready` deltaP `5.3705` edge `0.0106` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.16` n `96` status `ready` deltaP `4.4461` edge `0.0001` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.2846` n `96` status `ready` deltaP `3.8363` edge `0.0162` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.373` n `96` status `ready` deltaP `2.6759` edge `0.0145` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4397` n `96` status `ready` deltaP `-3.2685` edge `0.0013` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4627` n `96` status `ready` deltaP `2.5661` edge `0.0086` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4671` n `96` status `ready` deltaP `1.4845` edge `0.0147` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9071` n `96` status `ready` deltaP `-8.0402` edge `-0.0061` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.8591` n `91` status `ready` deltaP `-3.3291` edge `0.0609` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.1357` n `91` status `ready` deltaP `-25.3034` edge `-0.026` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
