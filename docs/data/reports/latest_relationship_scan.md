# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T12:22:17.863812+00:00`
- Price records: `645`
- Market context records: `754`
- Flow alert records: `2128`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `13.2064` n `146` status `ready` deltaP `31.4894` edge `0.924` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6777` n `146` status `ready` deltaP `7.5118` edge `0.5112` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.4884` n `146` status `ready` deltaP `2.927` edge `0.2207` maxDD `-5.9609`
- `market_context_high->equity_24h` score `-0.0907` n `146` status `ready` deltaP `1.3975` edge `0.2436` maxDD `-10.5047`
- `market_context_high->fx_1h` score `-0.2483` n `171` status `ready` deltaP `3.4913` edge `0.0027` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4279` n `159` status `ready` deltaP `6.2974` edge `0.0095` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6648` n `171` status `ready` deltaP `0.7867` edge `0.0368` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7197` n `171` status `ready` deltaP `-1.5047` edge `-0.0012` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.9141` n `171` status `ready` deltaP `0.807` edge `0.0038` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0104` n `171` status `ready` deltaP `6.4902` edge `-0.0005` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3355` n `171` status `ready` deltaP `5.2011` edge `-0.0145` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5395` n `171` status `ready` deltaP `-4.3089` edge `-0.0224` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.6014` n `159` status `ready` deltaP `17.3331` edge `0.1216` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7382` n `159` status `ready` deltaP `1.8777` edge `-0.0051` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-2.0494` n `171` status `ready` deltaP `-4.4275` edge `-0.0373` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.1659` n `159` status `ready` deltaP `2.5477` edge `0.0595` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5631` n `159` status `ready` deltaP `-1.0023` edge `0.0083` maxDD `-10.5498`
- `market_context_high->unknown_4h` score `-3.6931` n `159` status `ready` deltaP `5.1684` edge `-0.1544` maxDD `-8.3588`
- `market_context_high->commodity_4h` score `-3.7614` n `159` status `ready` deltaP `-5.8888` edge `0.0759` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-5.472` n `146` status `ready` deltaP `-16.554` edge `-0.074` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
