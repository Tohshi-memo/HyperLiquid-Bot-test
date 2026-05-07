# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T11:07:24.513042+00:00`
- Price records: `544`
- Market context records: `640`
- Flow alert records: `1813`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_major_24h` score `6.4802` n `146` status `ready` deltaP `17.8969` edge `0.4541` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.7761` n `146` status `ready` deltaP `8.4669` edge `0.4297` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1139` n `146` status `ready` deltaP `8.6009` edge `0.0152` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3534` n `146` status `ready` deltaP `1.4389` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5199` n `146` status `ready` deltaP `1.8631` edge `0.0417` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6831` n `146` status `ready` deltaP `-0.0486` edge `-0.0019` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1455` n `146` status `ready` deltaP `-4.2034` edge `-0.0071` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1792` n `146` status `ready` deltaP `5.8651` edge `-0.0059` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3107` n `146` status `ready` deltaP `-2.4739` edge `-0.0117` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6552` n `146` status `ready` deltaP `6.0705` edge `-0.0061` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1152` n `146` status `ready` deltaP `3.736` edge `0.0558` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3266` n `146` status `ready` deltaP `-0.962` edge `-0.0352` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5056` n `146` status `ready` deltaP `13.3951` edge `0.0725` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0144` n `146` status `ready` deltaP `-8.7128` edge `0.0064` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.3213` n `146` status `ready` deltaP `-5.0664` edge `0.1071` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.4286` n `146` status `ready` deltaP `-5.0381` edge `-0.0562` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.4847` n `146` status `ready` deltaP `-4.588` edge `-0.0446` maxDD `-10.5498`
- `market_context_high->fx_24h` score `-4.4056` n `146` status `ready` deltaP `-4.1158` edge `-0.0202` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.8033` n `146` status `ready` deltaP `-11.5944` edge `-0.0625` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8243` n `146` status `ready` deltaP `1.1986` edge `-0.2222` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
