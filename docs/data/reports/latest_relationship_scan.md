# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T10:52:13.065320+00:00`
- Price records: `672`
- Market context records: `968`
- Flow alert records: `2711`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `15.0682` n `150` status `ready` deltaP `34.1667` edge `1.0613` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.5011` n `150` status `ready` deltaP `10.7639` edge `0.72` maxDD `0.0`
- `market_context_high->equity_24h` score `1.3559` n `150` status `ready` deltaP `1.0` edge `0.3668` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.6517` n `150` status `ready` deltaP `-0.5972` edge `0.2578` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2852` n `205` status `ready` deltaP `2.8224` edge `0.0382` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3628` n `205` status `ready` deltaP `1.5679` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6559` n `205` status `ready` deltaP `0.961` edge `0.0158` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6594` n `193` status `ready` deltaP `1.9659` edge `0.002` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7245` n `205` status `ready` deltaP `2.9071` edge `0.0056` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-0.7811` n `205` status `ready` deltaP `-1.4802` edge `-0.0131` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.363` n `193` status `ready` deltaP `1.6839` edge `0.0904` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.6328` n `193` status `ready` deltaP `-1.394` edge `0.0255` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6615` n `205` status `ready` deltaP `6.1414` edge `-0.0071` maxDD `-11.4508`
- `market_context_high->metal_1h` score `-1.8829` n `205` status `ready` deltaP `-2.2908` edge `-0.0302` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0034` n `205` status `ready` deltaP `0.6025` edge `-0.027` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.4725` n `193` status `ready` deltaP `9.1882` edge `0.1033` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.8142` n `193` status `ready` deltaP `-0.9881` edge `0.0805` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.1609` n `193` status `ready` deltaP `7.817` edge `-0.1277` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.208` n `193` status `ready` deltaP `-1.8491` edge `0.0228` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-3.9697` n `150` status `ready` deltaP `5.3611` edge `0.0059` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
