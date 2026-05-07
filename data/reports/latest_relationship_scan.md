# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T16:37:20.958225+00:00`
- Price records: `566`
- Market context records: `663`
- Flow alert records: `1882`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `848`

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

- `market_context_high->crypto_major_24h` score `8.3193` n `146` status `ready` deltaP `21.3553` edge `0.5843` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3775` n `146` status `ready` deltaP `8.8896` edge `0.477` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1676` n `146` status `ready` deltaP `7.8529` edge `0.0133` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3481` n `147` status `ready` deltaP `1.5873` edge `0.0026` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5016` n `147` status `ready` deltaP `2.0627` edge `0.0419` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5805` n `147` status `ready` deltaP `1.0094` edge `0.0042` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1353` n `147` status `ready` deltaP `-4.0453` edge `-0.0073` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1446` n `147` status `ready` deltaP `-1.463` edge `-0.0046` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.197` n `147` status `ready` deltaP `5.5826` edge `-0.0055` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5761` n `147` status `ready` deltaP `6.1588` edge `-0.0001` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.771` n `146` status `ready` deltaP `5.0087` edge `0.076` maxDD `-15.2248`
- `market_context_high->index_4h` score `-1.9086` n `146` status `ready` deltaP `1.6985` edge `-0.0181` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-1.9141` n `146` status `ready` deltaP `15.5542` edge `0.1074` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.7776` n `146` status `ready` deltaP `-8.7689` edge `0.0265` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.0236` n `146` status `ready` deltaP `-2.5139` edge `-0.02` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.2404` n `146` status `ready` deltaP `-4.5812` edge `0.1106` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.3633` n `147` status `ready` deltaP `-5.0923` edge `-0.0504` maxDD `-9.0076`
- `market_context_high->equity_24h` score `-4.552` n `146` status `ready` deltaP `-11.1382` edge `-0.0446` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.6515` n `146` status `ready` deltaP `-7.2844` edge `-0.0306` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6945` n `146` status `ready` deltaP `1.5168` edge `-0.2135` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
