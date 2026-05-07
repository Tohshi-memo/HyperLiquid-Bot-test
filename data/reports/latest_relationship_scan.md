# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T15:07:31.410158+00:00`
- Price records: `560`
- Market context records: `656`
- Flow alert records: `1863`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `795`

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

- `market_context_high->crypto_major_24h` score `7.8156` n `146` status `ready` deltaP `20.4446` edge `0.5484` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.1406` n `146` status `ready` deltaP `8.5823` edge `0.4593` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1343` n `146` status `ready` deltaP `8.4044` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3359` n `146` status `ready` deltaP `1.7768` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4423` n `146` status `ready` deltaP `2.293` edge `0.0453` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6368` n `146` status `ready` deltaP `0.4517` edge `0.0007` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.1164` n `146` status `ready` deltaP `5.9304` edge `-0.0011` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.159` n `146` status `ready` deltaP `-4.282` edge `-0.0077` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1977` n `146` status `ready` deltaP `-1.5411` edge `-0.0085` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.5607` n `146` status `ready` deltaP `6.1717` edge `0.0011` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9981` n `146` status `ready` deltaP `4.2707` edge `0.062` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.0465` n `146` status `ready` deltaP `0.9944` edge `-0.0249` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.1606` n `146` status `ready` deltaP `14.9325` edge `0.091` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9117` n `146` status `ready` deltaP `-9.1692` edge `0.018` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.0409` n `146` status `ready` deltaP `-3.9015` edge `0.1227` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.2397` n `146` status `ready` deltaP `-3.2648` edge `-0.033` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4742` n `146` status `ready` deltaP `-5.3538` edge `-0.0579` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.5847` n `146` status `ready` deltaP `-6.4503` edge `-0.0276` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7352` n `146` status `ready` deltaP `-11.614` edge `-0.0567` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8513` n `146` status `ready` deltaP `0.831` edge `-0.222` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
