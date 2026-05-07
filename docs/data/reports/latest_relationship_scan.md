# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T21:07:18.378200+00:00`
- Price records: `584`
- Market context records: `684`
- Flow alert records: `1937`
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

- `market_context_high->crypto_major_24h` score `9.6515` n `146` status `ready` deltaP `23.9529` edge `0.678` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5293` n `146` status `ready` deltaP `8.5364` edge `0.492` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1977` n `147` status `ready` deltaP `7.4396` edge `0.0122` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2812` n `149` status `ready` deltaP `2.857` edge `0.0027` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5091` n `149` status `ready` deltaP `2.1183` edge `0.0409` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5894` n `149` status `ready` deltaP `0.8541` edge `0.0041` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1801` n `149` status `ready` deltaP `-1.7268` edge `-0.0058` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2793` n `149` status `ready` deltaP `-4.7813` edge `-0.0144` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3943` n `149` status `ready` deltaP `4.4665` edge `-0.0145` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5638` n `147` status `ready` deltaP `3.2784` edge `0.0001` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.691` n `149` status `ready` deltaP `5.4583` edge `-0.005` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7451` n `147` status `ready` deltaP `15.9709` edge `0.1187` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-1.8424` n `147` status `ready` deltaP `5.0313` edge `0.0699` maxDD `-15.2248`
- `market_context_high->index_24h` score `-1.9028` n `146` status `ready` deltaP `-5.7682` edge `0.0794` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.586` n `147` status `ready` deltaP `-1.1542` edge `0.0074` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.335` n `149` status `ready` deltaP `-4.8738` edge `-0.0495` maxDD `-9.0076`
- `market_context_high->equity_24h` score `-3.3575` n `146` status `ready` deltaP `-7.922` edge `0.0335` maxDD `-10.5047`
- `market_context_high->commodity_4h` score `-3.7892` n `147` status `ready` deltaP `-6.0862` edge `0.0749` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.4943` n `147` status `ready` deltaP `2.1738` edge `-0.2012` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.8532` n `146` status `ready` deltaP `-9.6627` edge `-0.0406` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
