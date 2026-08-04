# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T05:37:32.508883+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_24h` score `37.4091` n `46` status `ready` deltaP `26.2983` edge `2.9464` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `9.338` n `46` status `ready` deltaP `45.2144` edge `0.4941` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.1593` n `46` status `ready` deltaP `37.9151` edge `0.4451` maxDD `-0.434`
- `market_context_high->unknown_4h` score `5.8929` n `88` status `ready` deltaP `1.9678` edge `0.5775` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2221` n `88` status `ready` deltaP `15.5211` edge `0.083` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.3927` n `88` status `ready` deltaP `18.847` edge `0.0107` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2649` n `88` status `ready` deltaP `5.8315` edge `0.0248` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.2347` n `88` status `ready` deltaP `8.5806` edge `-0.0028` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.4468` n `88` status `ready` deltaP `1.8781` edge `-0.0164` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.4518` n `88` status `ready` deltaP `6.1114` edge `0.0248` maxDD `-3.211`
- `market_context_high->metal_1h` score `-0.5378` n `88` status `ready` deltaP `-1.6195` edge `-0.0087` maxDD `-1.6224`
- `market_context_high->crypto_alt_4h` score `-0.9796` n `88` status `ready` deltaP `3.1042` edge `-0.0073` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2887` n `88` status `ready` deltaP `-3.62` edge `-0.0122` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.4964` n `88` status `ready` deltaP `6.0629` edge `-0.0787` maxDD `-10.619`
- `market_context_high->fx_24h` score `-1.6258` n `46` status `ready` deltaP `-3.7062` edge `0.0098` maxDD `-4.3126`
- `market_context_high->index_4h` score `-1.7734` n `88` status `ready` deltaP `-8.8969` edge `-0.0426` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.3512` n `88` status `ready` deltaP `2.8988` edge `-0.2539` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6547` n `88` status `ready` deltaP `-13.0988` edge `-0.0799` maxDD `-7.6533`
- `market_context_high->metal_24h` score `-4.8662` n `46` status `ready` deltaP `-24.1621` edge `-0.1276` maxDD `-2.6802`
- `market_context_high->equity_4h` score `-6.4156` n `88` status `ready` deltaP `1.7045` edge `-0.3008` maxDD `-35.3129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
