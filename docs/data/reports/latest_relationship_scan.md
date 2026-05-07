# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T20:44:07.192069+00:00`
- Price records: `582`
- Market context records: `682`
- Flow alert records: `1932`
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

- `market_context_high->crypto_major_24h` score `9.5068` n `146` status `ready` deltaP `23.6738` edge `0.6678` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5095` n `146` status `ready` deltaP `8.5744` edge `0.4901` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2079` n `147` status `ready` deltaP `7.2578` edge `0.0121` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.292` n `149` status `ready` deltaP `2.6658` edge `0.0026` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4643` n `149` status `ready` deltaP `2.3034` edge `0.0434` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6017` n `149` status `ready` deltaP `0.6466` edge `0.0039` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1953` n `149` status `ready` deltaP `-1.7668` edge `-0.0068` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.3072` n `149` status `ready` deltaP `-4.9651` edge `-0.0155` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.4357` n `149` status `ready` deltaP `4.2637` edge `-0.0166` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5908` n `147` status `ready` deltaP `3.0601` edge `-0.0007` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.7026` n `149` status `ready` deltaP `5.4481` edge `-0.0059` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7539` n `147` status `ready` deltaP `15.9516` edge `0.1181` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-1.8271` n `147` status `ready` deltaP `5.1477` edge `0.0704` maxDD `-15.2248`
- `market_context_high->index_24h` score `-2.0018` n `146` status `ready` deltaP `-6.0905` edge `0.0733` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.6155` n `147` status `ready` deltaP `-1.3883` edge `0.0065` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3675` n `149` status `ready` deltaP `-5.0695` edge `-0.0509` maxDD `-9.0076`
- `market_context_high->equity_24h` score `-3.4907` n `146` status `ready` deltaP `-8.2675` edge `0.0247` maxDD `-10.5047`
- `market_context_high->commodity_4h` score `-3.74` n `147` status `ready` deltaP `-5.8755` edge `0.0776` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.5476` n `147` status `ready` deltaP `1.9579` edge `-0.2042` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.8321` n `146` status `ready` deltaP `-9.4072` edge `-0.0396` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
