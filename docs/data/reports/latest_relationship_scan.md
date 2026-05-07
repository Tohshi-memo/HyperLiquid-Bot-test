# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T22:37:19.655665+00:00`
- Price records: `590`
- Market context records: `691`
- Flow alert records: `1956`
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

- `market_context_high->crypto_major_24h` score `10.1038` n `146` status `ready` deltaP `24.7768` edge `0.7102` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6127` n `146` status `ready` deltaP `8.4244` edge `0.4997` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2098` n `149` status `ready` deltaP `7.1918` edge `0.0123` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2689` n `149` status `ready` deltaP `3.0789` edge `0.0028` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5225` n `149` status `ready` deltaP `2.0861` edge `0.04` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5667` n `149` status `ready` deltaP `1.1243` edge `0.0052` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.0706` n `149` status `ready` deltaP `-1.0932` edge `-0.0009` maxDD `-4.4826`
- `market_context_high->crypto_major_4h` score `-1.2244` n `149` status `ready` deltaP `15.2433` edge `0.112` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.2303` n `149` status `ready` deltaP `-4.4083` edge `-0.0128` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3704` n `149` status `ready` deltaP `4.5548` edge `-0.0131` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.6011` n `146` status `ready` deltaP `-4.8169` edge `0.0982` maxDD `-5.9609`
- `market_context_high->index_4h` score `-1.6019` n `149` status `ready` deltaP `3.0566` edge `-0.0016` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6284` n `149` status `ready` deltaP `6.0002` edge `-0.0034` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9788` n `149` status `ready` deltaP `4.2419` edge `0.0638` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6492` n `149` status `ready` deltaP `-1.3293` edge `0.0033` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-2.9219` n `146` status `ready` deltaP `-6.9024` edge `0.063` maxDD `-10.5047`
- `market_context_high->metal_1h` score `-3.28` n `149` status `ready` deltaP `-4.6361` edge `-0.0465` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7462` n `149` status `ready` deltaP `-5.833` edge `0.0768` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.5184` n `149` status `ready` deltaP `1.9631` edge `-0.2018` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.9158` n `146` status `ready` deltaP `-10.4166` edge `-0.0436` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
