# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T02:37:30.728955+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.159` n `47` status `ready` deltaP `10.7148` edge `5.9489` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `36.6416` n `46` status `ready` deltaP `23.9508` edge `2.9094` maxDD `-0.5817`
- `market_context_high->equity_24h` score `21.2646` n `46` status `ready` deltaP `21.3466` edge `1.6398` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `20.9623` n `46` status `ready` deltaP `18.9236` edge `1.6207` maxDD `0.0`
- `market_context_high->index_24h` score `7.1387` n `46` status `ready` deltaP `30.3744` edge `0.4011` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9803` n `103` status `ready` deltaP `14.6889` edge `0.4169` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.637` n `103` status `ready` deltaP `17.7377` edge `0.3259` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `2.9004` n `103` status `ready` deltaP `-3.7402` edge `1.1709` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `2.6169` n `103` status `ready` deltaP `13.7565` edge `0.1754` maxDD `-1.5895`
- `news_risk_high->commodity_24h` score `2.521` n `103` status `ready` deltaP `23.9212` edge `0.1685` maxDD `-2.431`
- `market_context_high->index_4h` score `2.4868` n `47` status `ready` deltaP `29.3007` edge `0.0273` maxDD `-0.2323`
- `market_context_high->metal_24h` score `2.1546` n `46` status `ready` deltaP `24.3509` edge `0.0406` maxDD `-0.2042`
- `news_risk_high->crypto_major_1h` score `2.126` n `103` status `ready` deltaP `16.3014` edge `0.112` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.5734` n `103` status `ready` deltaP `23.0716` edge `0.0409` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.4861` n `47` status `ready` deltaP `11.9616` edge `0.0859` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.2179` n `103` status `ready` deltaP `29.6639` edge `0.1215` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8181` n `47` status `ready` deltaP `13.1131` edge `0.0086` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6649` n `103` status `ready` deltaP `15.502` edge `0.0114` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6322` n `47` status `ready` deltaP `9.2209` edge `0.0315` maxDD `-1.5564`
- `news_risk_high->metal_4h` score `0.3384` n `103` status `ready` deltaP `14.4225` edge `0.043` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
