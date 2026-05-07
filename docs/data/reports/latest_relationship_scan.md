# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T20:52:20.610013+00:00`
- Price records: `583`
- Market context records: `683`
- Flow alert records: `1934`
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

- `market_context_high->crypto_major_24h` score `9.5732` n `146` status `ready` deltaP `23.8137` edge `0.6724` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5104` n `146` status `ready` deltaP `8.5553` edge `0.4903` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2032` n `147` status `ready` deltaP `7.3489` edge `0.0121` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2862` n `149` status `ready` deltaP `2.7616` edge `0.0027` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4765` n `149` status `ready` deltaP `2.2107` edge `0.043` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5955` n `149` status `ready` deltaP `0.7505` edge `0.004` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.2031` n `149` status `ready` deltaP `-1.8337` edge `-0.007` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2939` n `149` status `ready` deltaP `-4.8731` edge `-0.015` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.4228` n `149` status `ready` deltaP `4.3653` edge `-0.0162` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5761` n `147` status `ready` deltaP `3.1694` edge `-0.0002` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.7091` n `149` status `ready` deltaP `5.3668` edge `-0.0059` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7602` n `147` status `ready` deltaP `15.873` edge `0.1181` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-1.8402` n `147` status `ready` deltaP `5.0894` edge `0.0697` maxDD `-15.2248`
- `market_context_high->index_24h` score `-1.9517` n `146` status `ready` deltaP `-5.929` edge `0.0764` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.599` n `147` status `ready` deltaP `-1.2711` edge `0.0071` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3585` n `149` status `ready` deltaP `-4.9715` edge `-0.0508` maxDD `-9.0076`
- `market_context_high->equity_24h` score `-3.4265` n `146` status `ready` deltaP `-8.0944` edge `0.0289` maxDD `-10.5047`
- `market_context_high->commodity_4h` score `-3.7604` n `147` status `ready` deltaP `-5.9811` edge `0.0766` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.5221` n `147` status `ready` deltaP `2.066` edge `-0.2028` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.8426` n `146` status `ready` deltaP `-9.5352` edge `-0.0401` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
