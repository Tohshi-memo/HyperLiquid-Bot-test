# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T21:42:42.859500+00:00`
- Price records: `586`
- Market context records: `687`
- Flow alert records: `1945`
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

- `market_context_high->crypto_major_24h` score `9.8021` n `146` status `ready` deltaP `24.2298` edge `0.6887` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5611` n `146` status `ready` deltaP `8.4988` edge `0.4949` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1875` n `147` status `ready` deltaP `7.62` edge `0.0123` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2706` n `149` status `ready` deltaP `3.0468` edge `0.0028` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5574` n `149` status `ready` deltaP `1.9345` edge `0.0381` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.574` n `149` status `ready` deltaP `1.0601` edge `0.0047` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1463` n `149` status `ready` deltaP `-1.5142` edge `-0.0044` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2503` n `149` status `ready` deltaP `-4.5989` edge `-0.0132` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3614` n `149` status `ready` deltaP `4.668` edge `-0.0131` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5368` n `147` status `ready` deltaP `3.4952` edge `0.0009` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6704` n `149` status `ready` deltaP `5.6402` edge `-0.0045` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7424` n `147` status `ready` deltaP `15.99` edge `0.1188` maxDD `-22.648`
- `market_context_high->index_24h` score `-1.8004` n `146` status `ready` deltaP `-5.4485` edge `0.0858` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-1.8625` n `147` status `ready` deltaP `4.9158` edge `0.069` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5494` n `147` status `ready` deltaP `-0.9218` edge `0.0089` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-3.2196` n `146` status `ready` deltaP `-7.5793` edge `0.0427` maxDD `-10.5047`
- `market_context_high->metal_1h` score `-3.2919` n `149` status `ready` deltaP `-4.6795` edge `-0.0472` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8468` n `147` status `ready` deltaP `-6.2955` edge `0.0715` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.446` n `147` status `ready` deltaP `2.3881` edge `-0.1986` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.8741` n `146` status `ready` deltaP `-9.916` edge `-0.0416` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
