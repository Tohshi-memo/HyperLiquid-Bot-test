# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T15:37:30.044607+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8829`

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

- `market_context_high->equity_4h` score `2.3211` n `96` status `ready` deltaP `12.2205` edge `0.2008` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8656` n `96` status `ready` deltaP `15.3007` edge `0.0836` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.3471` n `96` status `ready` deltaP `4.6875` edge `0.2018` maxDD `-4.9964`
- `market_context_high->index_1h` score `0.921` n `96` status `ready` deltaP `15.7622` edge `0.0104` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.8905` n `96` status `ready` deltaP `16.1077` edge `0.0244` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.5237` n `96` status `ready` deltaP `8.6806` edge `0.1926` maxDD `-4.666`
- `market_context_high->crypto_major_4h` score `0.3666` n `96` status `ready` deltaP `9.1717` edge `0.0715` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `0.36` n `96` status `ready` deltaP `18.2291` edge `-0.0409` maxDD `-1.0505`
- `market_context_high->index_4h` score `0.1324` n `96` status `ready` deltaP `8.1046` edge `0.0225` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.1166` n `96` status `ready` deltaP `8.8668` edge `0.0061` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `0.1102` n `96` status `ready` deltaP `7.4102` edge `-0.0175` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.0094` n `96` status `ready` deltaP `4.622` edge `0.0071` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3284` n `96` status `ready` deltaP `-1.3224` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_alt_4h` score `-0.4253` n `96` status `ready` deltaP `7.0122` edge `0.0448` maxDD `-5.4926`
- `market_context_high->crypto_major_1h` score `-0.5662` n `96` status `ready` deltaP `2.3827` edge `-0.004` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.6029` n `96` status `ready` deltaP `0.8795` edge `-0.003` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6152` n `96` status `ready` deltaP `0.2795` edge `0.0043` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.883` n `96` status `ready` deltaP `-7.4414` edge `-0.007` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.4697` n `96` status `ready` deltaP `-5.5556` edge `0.0512` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.7301` n `96` status `ready` deltaP `-20.6597` edge `-0.0148` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
