# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T22:07:29.472114+00:00`
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

- `market_context_high->crypto_major_24h` score `2.6327` n `91` status `ready` deltaP `9.1614` edge `0.2791` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5955` n `91` status `ready` deltaP `18.5955` edge `0.2639` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.397` n `96` status `ready` deltaP `11.5582` edge `0.0695` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.1408` n `96` status `ready` deltaP `7.0376` edge `0.137` maxDD `-2.4411`
- `market_context_high->metal_4h` score `1.0023` n `96` status `ready` deltaP `16.2601` edge `0.0327` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.7764` n `96` status `ready` deltaP `9.629` edge `0.1026` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.6983` n `96` status `ready` deltaP `13.2173` edge `0.0088` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.4986` n `96` status `ready` deltaP `9.6557` edge `-0.0001` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.306` n `96` status `ready` deltaP `10.2134` edge `0.0844` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.1828` n `91` status `ready` deltaP `15.6918` edge `-0.068` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.0781` n `96` status `ready` deltaP `5.2208` edge `0.0104` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1774` n `96` status `ready` deltaP `4.1412` edge `-0.0001` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.3284` n `96` status `ready` deltaP `3.379` edge `0.0156` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3606` n `96` status `ready` deltaP `2.8256` edge `0.0151` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4475` n `96` status `ready` deltaP `-3.4182` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.453` n `96` status `ready` deltaP `1.6342` edge `0.0155` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.4619` n `96` status `ready` deltaP `2.5661` edge `0.0087` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8985` n `96` status `ready` deltaP `-7.8905` edge `-0.006` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.9236` n `91` status `ready` deltaP `-3.8499` edge `0.0561` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.1809` n `91` status `ready` deltaP `-25.8242` edge `-0.0263` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
