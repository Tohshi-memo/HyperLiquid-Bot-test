# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T22:22:26.250407+00:00`
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

- `market_context_high->crypto_major_24h` score `2.6056` n `91` status `ready` deltaP `8.9877` edge `0.278` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5923` n `91` status `ready` deltaP `18.5955` edge `0.2635` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.397` n `96` status `ready` deltaP `11.5582` edge `0.0695` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.165` n `96` status `ready` deltaP `7.19` edge `0.138` maxDD `-2.4411`
- `market_context_high->metal_4h` score `1.0205` n `96` status `ready` deltaP `16.4126` edge `0.0332` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.797` n `96` status `ready` deltaP `9.7815` edge `0.1033` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.6863` n `96` status `ready` deltaP `13.0676` edge `0.0088` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5094` n `96` status `ready` deltaP `9.6557` edge `0.0008` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.329` n `96` status `ready` deltaP `10.3659` edge `0.0853` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.1864` n `91` status `ready` deltaP `15.6918` edge `-0.0677` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.0913` n `96` status `ready` deltaP `5.3705` edge `0.0105` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1695` n `96` status `ready` deltaP `4.2937` edge `-0.0001` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.3138` n `96` status `ready` deltaP `3.5315` edge `0.0158` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3613` n `96` status `ready` deltaP `2.8256` edge `0.015` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4397` n `96` status `ready` deltaP `-3.2685` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.453` n `96` status `ready` deltaP `1.6342` edge `0.0155` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.4619` n `96` status `ready` deltaP `2.5661` edge `0.0087` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8985` n `96` status `ready` deltaP `-7.8905` edge `-0.006` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.9014` n `91` status `ready` deltaP `-3.6763` edge `0.0578` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.1658` n `91` status `ready` deltaP `-25.6506` edge `-0.0262` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
