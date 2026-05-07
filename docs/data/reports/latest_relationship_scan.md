# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T13:22:16.572426+00:00`
- Price records: `553`
- Market context records: `649`
- Flow alert records: `1842`
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

- `market_context_high->crypto_major_24h` score `7.3142` n `146` status `ready` deltaP `19.3519` edge `0.5139` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.0463` n `146` status `ready` deltaP `8.7243` edge `0.4505` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1683` n `146` status `ready` deltaP `7.7502` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3528` n `146` status `ready` deltaP `1.4365` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.3847` n `146` status `ready` deltaP `2.6241` edge `0.0479` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6618` n `146` status `ready` deltaP `0.225` edge `-0.001` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.2001` n `146` status `ready` deltaP `-4.6011` edge `-0.009` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2724` n `146` status `ready` deltaP `-2.1604` edge `-0.0106` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.2924` n `146` status `ready` deltaP `5.1851` edge `-0.0108` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.7208` n `146` status `ready` deltaP `5.4906` edge `-0.0077` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1156` n `146` status `ready` deltaP `3.7614` edge `0.0556` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.1786` n `146` status `ready` deltaP `0.1529` edge `-0.0303` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3592` n `146` status `ready` deltaP `14.1897` edge `0.0794` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9267` n `146` status `ready` deltaP `-8.8769` edge `0.0148` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.1637` n `146` status `ready` deltaP `-4.4026` edge `0.1158` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.3991` n `146` status `ready` deltaP `-4.1623` edge `-0.0403` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4824` n `146` status `ready` deltaP `-5.3659` edge `-0.0585` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.5085` n `146` status `ready` deltaP `-5.4492` edge `-0.0245` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6603` n `146` status `ready` deltaP `-11.4125` edge `-0.0518` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8818` n `146` status `ready` deltaP `0.5701` edge `-0.2228` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
