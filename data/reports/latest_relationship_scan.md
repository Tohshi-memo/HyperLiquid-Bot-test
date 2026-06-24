# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T16:52:27.346209+00:00`
- Price records: `672`
- Market context records: `4640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9996`

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

- `market_context_high->unknown_1h` score `70.0439` n `146` status `ready` deltaP `8.4591` edge `5.8265` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.6853` n `146` status `ready` deltaP `9.7331` edge `0.4466` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3317` n `146` status `ready` deltaP `3.0986` edge `0.0313` maxDD `-2.0345`
- `market_context_high->unknown_24h` score `-0.5138` n `146` status `ready` deltaP `5.5223` edge `0.0127` maxDD `-4.7201`
- `market_context_high->fx_1h` score `-0.5816` n `146` status `ready` deltaP `-2.2496` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7025` n `146` status `ready` deltaP `2.5163` edge `0.0014` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.7806` n `146` status `ready` deltaP `-1.3473` edge `0.0076` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.8297` n `146` status `ready` deltaP `2.5059` edge `-0.0108` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.045` n `146` status `ready` deltaP `5.9534` edge `0.0371` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3479` n `146` status `ready` deltaP `0.5262` edge `0.0006` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7251` n `146` status `ready` deltaP `-4.5136` edge `-0.0128` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9525` n `146` status `ready` deltaP `-4.3905` edge `-0.0841` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-4.9881` n `146` status `ready` deltaP `-8.5117` edge `-0.0077` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.1709` n `146` status `ready` deltaP `11.2847` edge `0.0443` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.4025` n `146` status `ready` deltaP `-1.6467` edge `-0.1105` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.6101` n `146` status `ready` deltaP `-5.2436` edge `-0.1406` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.8098` n `146` status `ready` deltaP `-7.6104` edge `-0.0626` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6005` n `146` status `ready` deltaP `-1.9817` edge `-0.2237` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.9726` n `146` status `ready` deltaP `-5.3187` edge `-0.3217` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.7208` n `146` status `ready` deltaP `-4.0345` edge `-0.3814` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
