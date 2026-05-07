# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T20:22:15.462758+00:00`
- Price records: `581`
- Market context records: `680`
- Flow alert records: `1928`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `9.4343` n `146` status `ready` deltaP `23.5334` edge `0.6627` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5087` n `146` status `ready` deltaP `8.5935` edge `0.4899` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2127` n `147` status `ready` deltaP `7.1665` edge `0.0121` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.297` n `149` status `ready` deltaP `2.5698` edge `0.0026` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4485` n `149` status `ready` deltaP `2.3964` edge `0.0441` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5981` n `149` status `ready` deltaP `0.7168` edge `0.0039` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1864` n `149` status `ready` deltaP `-1.6996` edge `-0.0065` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2996` n `149` status `ready` deltaP `-4.8841` edge `-0.0154` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.4463` n `149` status `ready` deltaP `4.1617` edge `-0.0168` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.608` n `147` status `ready` deltaP `2.9503` edge `-0.0014` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.7123` n `149` status `ready` deltaP `5.3564` edge `-0.0061` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7476` n `147` status `ready` deltaP `16.0304` edge `0.1181` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-1.808` n `147` status `ready` deltaP `5.2061` edge `0.0716` maxDD `-15.2248`
- `market_context_high->index_24h` score `-2.0532` n `146` status `ready` deltaP `-6.2527` edge `0.0701` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.6345` n `147` status `ready` deltaP `-1.506` edge `0.0057` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3778` n `149` status `ready` deltaP `-5.1679` edge `-0.0511` maxDD `-9.0076`
- `market_context_high->equity_24h` score `-3.5634` n `146` status `ready` deltaP `-8.4413` edge `0.0198` maxDD `-10.5047`
- `market_context_high->commodity_4h` score `-3.7159` n `147` status `ready` deltaP `-5.7696` edge `0.0789` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.5695` n `147` status `ready` deltaP `1.8494` edge `-0.2053` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.8207` n `146` status `ready` deltaP `-9.2786` edge `-0.039` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
