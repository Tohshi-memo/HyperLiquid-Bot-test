# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T01:37:34.807001+00:00`
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

- `market_context_high->crypto_major_24h` score `2.3409` n `91` status `ready` deltaP `7.5989` edge `0.2652` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.544` n `96` status `ready` deltaP `8.8668` edge `0.1584` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.4868` n `96` status `ready` deltaP `12.4564` edge `0.071` maxDD `-0.4112`
- `market_context_high->commodity_24h` score `1.4107` n `91` status `ready` deltaP `16.5122` edge `0.2541` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.2146` n `96` status `ready` deltaP `18.0894` edge `0.0382` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9341` n `96` status `ready` deltaP `11.001` edge `0.1066` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.7881` n `96` status `ready` deltaP `14.2652` edge `0.0093` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.4911` n `96` status `ready` deltaP `11.4329` edge `0.0917` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.3199` n `96` status `ready` deltaP `9.2066` edge `-0.012` maxDD `-0.4843`
- `market_context_high->unknown_24h` score `0.2947` n `91` status `ready` deltaP `16.3862` edge `-0.0633` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.1212` n `96` status `ready` deltaP `5.6699` edge `0.011` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.0714` n `96` status `ready` deltaP `5.9705` edge `0.0013` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.1341` n `96` status `ready` deltaP `5.2083` edge `0.0196` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3629` n `96` status `ready` deltaP `2.8256` edge `0.0148` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.3891` n `96` status `ready` deltaP `-2.3703` edge `0.0018` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4157` n `96` status `ready` deltaP `2.233` edge `0.0163` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.466` n `96` status `ready` deltaP `2.4137` edge `0.0092` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9063` n `96` status `ready` deltaP `-8.0402` edge `-0.006` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.6038` n `91` status `ready` deltaP `-1.4194` edge `0.0809` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.0439` n `91` status `ready` deltaP `-24.2617` edge `-0.0253` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
