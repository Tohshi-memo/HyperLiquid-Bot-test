# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T23:22:30.889829+00:00`
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

- `market_context_high->crypto_major_24h` score `2.4828` n `91` status `ready` deltaP `8.2933` edge `0.2724` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5383` n `91` status `ready` deltaP `17.9011` edge `0.2612` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.4665` n `96` status `ready` deltaP `12.157` edge `0.0713` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.293` n `96` status `ready` deltaP `7.7998` edge `0.1446` maxDD `-2.4411`
- `market_context_high->metal_4h` score `1.092` n `96` status `ready` deltaP `17.0223` edge `0.0351` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.8539` n `96` status `ready` deltaP `10.2388` edge `0.105` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.7234` n `96` status `ready` deltaP `13.5167` edge `0.0089` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.471` n `96` status `ready` deltaP `9.506` edge `-0.0014` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.421` n `96` status `ready` deltaP `10.9756` edge `0.0889` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.1948` n `91` status `ready` deltaP `15.6918` edge `-0.067` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.0925` n `96` status `ready` deltaP `5.3705` edge `0.0106` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1434` n `96` status `ready` deltaP `4.751` edge `0.0002` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.253` n `96` status `ready` deltaP `4.1412` edge `0.0168` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3831` n `96` status `ready` deltaP `2.5262` edge `0.0142` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4397` n `96` status `ready` deltaP `-3.2685` edge `0.0013` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4619` n `96` status `ready` deltaP `2.5661` edge `0.0087` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4756` n `96` status `ready` deltaP `1.3348` edge `0.0146` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9157` n `96` status `ready` deltaP `-8.1899` edge `-0.0062` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.8169` n `91` status `ready` deltaP `-2.9819` edge `0.064` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.1055` n `91` status `ready` deltaP `-24.9561` edge `-0.0258` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
