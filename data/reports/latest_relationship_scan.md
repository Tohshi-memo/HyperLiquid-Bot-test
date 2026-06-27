# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T23:07:29.849087+00:00`
- Price records: `672`
- Market context records: `4982`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `12.0423` n `91` status `ready` deltaP `4.3973` edge `1.0243` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.65` n `88` status `ready` deltaP `18.0571` edge `0.551` maxDD `-6.3773`
- `market_context_high->unknown_24h` score `5.8471` n `78` status `ready` deltaP `28.1117` edge `0.3341` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.5379` n `88` status `ready` deltaP `14.7173` edge `0.4986` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `2.6759` n `88` status `ready` deltaP `23.5449` edge `0.1411` maxDD `-3.6725`
- `market_context_high->metal_4h` score `1.2754` n `88` status `ready` deltaP `12.5416` edge `0.1264` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.736` n `88` status `ready` deltaP `6.9013` edge `0.1865` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5563` n `88` status `ready` deltaP `7.3725` edge `0.0438` maxDD `-0.7272`
- `market_context_high->equity_1h` score `0.491` n `91` status `ready` deltaP `6.4931` edge `0.077` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.3737` n `91` status `ready` deltaP `4.2409` edge `0.1186` maxDD `-5.25`
- `market_context_high->crypto_alt_1h` score `0.1598` n `91` status `ready` deltaP `4.8941` edge `0.0901` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0983` n `91` status `ready` deltaP `3.142` edge `0.0369` maxDD `-1.3057`
- `market_context_high->fx_24h` score `-0.3472` n `78` status `ready` deltaP `4.5272` edge `0.0015` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.4017` n `91` status `ready` deltaP `1.1959` edge `0.0065` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4169` n `91` status `ready` deltaP `1.1993` edge `0.0132` maxDD `-0.6385`
- `market_context_high->commodity_4h` score `-0.8072` n `88` status `ready` deltaP `4.2267` edge `-0.0064` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.9098` n `88` status `ready` deltaP `-2.73` edge `-0.0014` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.5831` n `91` status `ready` deltaP `-10.2932` edge `-0.0035` maxDD `-0.4511`
- `market_context_high->commodity_24h` score `-3.5824` n `78` status `ready` deltaP `11.2046` edge `-0.0231` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.4289` n `78` status `ready` deltaP `-4.4738` edge `0.0075` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
