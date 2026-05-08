# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T00:22:09.411855+00:00`
- Price records: `597`
- Market context records: `700`
- Flow alert records: `1978`
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

- `market_context_high->crypto_major_24h` score `10.5651` n `146` status `ready` deltaP `25.7129` edge `0.7424` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5965` n `146` status `ready` deltaP `8.2971` edge `0.4992` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1944` n `149` status `ready` deltaP `7.4581` edge `0.0125` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2632` n `149` status `ready` deltaP `3.2189` edge `0.0026` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5114` n `149` status `ready` deltaP `2.1342` edge `0.0406` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.602` n `149` status `ready` deltaP `0.6404` edge `0.0039` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1487` n `149` status `ready` deltaP `-1.5588` edge `-0.0043` maxDD `-4.4826`
- `market_context_high->crypto_major_4h` score `-1.1703` n `149` status `ready` deltaP `15.9087` edge `0.1145` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.2006` n `149` status `ready` deltaP `-4.2917` edge `-0.0111` maxDD `-2.1602`
- `market_context_high->index_24h` score `-1.2758` n `146` status `ready` deltaP `-3.7361` edge `0.1181` maxDD `-5.9609`
- `market_context_high->crypto_alt_1h` score `-1.4309` n `149` status `ready` deltaP `4.2339` edge `-0.016` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.64` n `149` status `ready` deltaP `2.5799` edge `-0.0016` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6632` n `149` status `ready` deltaP `5.7755` edge `-0.0048` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9663` n `149` status `ready` deltaP `4.1874` edge `0.0652` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.4392` n `146` status `ready` deltaP `-5.744` edge `0.0955` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.5416` n `149` status `ready` deltaP `-0.5397` edge `0.007` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.333` n `149` status `ready` deltaP `-4.9831` edge `-0.0486` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8691` n `149` status `ready` deltaP `-6.5439` edge `0.0713` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.3605` n `149` status `ready` deltaP `2.6915` edge `-0.1935` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.9853` n `146` status `ready` deltaP `-11.2731` edge `-0.0468` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
