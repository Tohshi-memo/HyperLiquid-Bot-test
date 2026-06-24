# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T15:37:30.115709+00:00`
- Price records: `672`
- Market context records: `4635`
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

- `market_context_high->unknown_1h` score `70.002` n `146` status `ready` deltaP `8.3094` edge `5.824` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.4801` n `146` status `ready` deltaP `9.7331` edge `0.4295` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.3077` n `146` status `ready` deltaP `3.398` edge `0.0313` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5652` n `146` status `ready` deltaP `-1.9502` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7341` n `146` status `ready` deltaP `2.059` edge `0.0004` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.8429` n `146` status `ready` deltaP `-2.0958` edge `0.0046` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.8904` n `146` status `ready` deltaP `1.7437` edge `-0.0135` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.0028` n `146` status `ready` deltaP `5.9534` edge `0.0425` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-1.1704` n `146` status `ready` deltaP `5.1751` edge `-0.0397` maxDD `-4.7201`
- `market_context_high->equity_4h` score `-1.5514` n `146` status `ready` deltaP `-0.236` edge `-0.0204` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7526` n `146` status `ready` deltaP `-4.813` edge `-0.0131` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9525` n `146` status `ready` deltaP `-4.3905` edge `-0.0841` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-4.9893` n `146` status `ready` deltaP `-8.5117` edge `-0.0078` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.1505` n `146` status `ready` deltaP `11.2847` edge `0.046` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.5775` n `146` status `ready` deltaP `-2.3952` edge `-0.1201` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.772` n `146` status `ready` deltaP `-5.9921` edge `-0.1491` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.9358` n `146` status `ready` deltaP `-7.6104` edge `-0.0731` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.9849` n `146` status `ready` deltaP `-2.7439` edge `-0.2679` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.1363` n `146` status `ready` deltaP `-6.0809` edge `-0.3376` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.1231` n `146` status `ready` deltaP `-4.7967` edge `-0.4279` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
