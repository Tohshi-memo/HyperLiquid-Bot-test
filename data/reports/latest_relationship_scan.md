# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T19:07:17.832931+00:00`
- Price records: `576`
- Market context records: `674`
- Flow alert records: `1913`
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

- `market_context_high->crypto_major_24h` score `9.0667` n `146` status `ready` deltaP `22.8225` edge `0.6368` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5176` n `146` status `ready` deltaP `8.6901` edge `0.49` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2071` n `147` status `ready` deltaP `7.2444` edge `0.0123` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3188` n `148` status `ready` deltaP `2.1507` edge `0.0026` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4966` n `148` status `ready` deltaP `2.1697` edge `0.0416` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5527` n `148` status `ready` deltaP `1.3038` edge `0.0058` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1155` n `148` status `ready` deltaP `-1.3086` edge `-0.0032` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.3094` n `148` status `ready` deltaP `-5.0227` edge `-0.0153` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3814` n `148` status `ready` deltaP `4.5974` edge `-0.0143` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.6507` n `148` status `ready` deltaP `5.8118` edge `-0.004` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.6692` n `147` status `ready` deltaP `5.5017` edge `0.0812` maxDD `-15.2248`
- `market_context_high->index_4h` score `-1.7208` n `147` status `ready` deltaP `2.3957` edge `-0.0071` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-1.7538` n `147` status `ready` deltaP `15.8929` edge `0.1185` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.3156` n `146` status `ready` deltaP `-7.0738` edge `0.0537` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.7445` n `147` status `ready` deltaP `-1.741` edge `-0.0019` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3176` n `148` status `ready` deltaP `-4.7912` edge `-0.0486` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5675` n `147` status `ready` deltaP `-5.2342` edge `0.0877` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.9254` n `146` status `ready` deltaP `-9.3214` edge `-0.0045` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.6328` n `147` status `ready` deltaP `1.6582` edge `-0.2093` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.7658` n `146` status `ready` deltaP `-8.6279` edge `-0.0363` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
