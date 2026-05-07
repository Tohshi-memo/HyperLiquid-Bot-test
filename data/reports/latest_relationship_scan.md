# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T17:12:15.453029+00:00`
- Price records: `568`
- Market context records: `666`
- Flow alert records: `1889`
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

- `market_context_high->crypto_major_24h` score `8.4896` n `146` status `ready` deltaP `21.6537` edge `0.5965` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4427` n `146` status `ready` deltaP `8.849` edge `0.4827` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1794` n `146` status `ready` deltaP `7.6718` edge `0.013` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3571` n `147` status `ready` deltaP `1.4286` edge `0.0025` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5505` n `147` status `ready` deltaP `1.8707` edge `0.0391` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5584` n `147` status `ready` deltaP `1.2245` edge `0.0056` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1029` n `147` status `ready` deltaP `-1.2415` edge `-0.0026` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1882` n `147` status `ready` deltaP `-4.2119` edge `-0.0106` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2292` n `147` status `ready` deltaP `5.435` edge `-0.0072` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5777` n `147` status `ready` deltaP `6.1695` edge `-0.0003` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.6976` n `146` status `ready` deltaP `5.2511` edge `0.0805` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-1.8293` n `146` status `ready` deltaP `15.7584` edge `0.1131` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.8493` n `146` status `ready` deltaP `1.9298` edge `-0.0147` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.6961` n `146` status `ready` deltaP `-8.4241` edge `0.031` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.9283` n `146` status `ready` deltaP `-2.2673` edge `-0.0137` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3362` n `147` status `ready` deltaP `-4.8885` edge `-0.0495` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.3567` n `146` status `ready` deltaP `-4.8045` edge `0.1024` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.4396` n `146` status `ready` deltaP `-10.7686` edge `-0.0377` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.6729` n `146` status `ready` deltaP `1.5609` edge `-0.212` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.6743` n `146` status `ready` deltaP `-7.5577` edge `-0.0317` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
