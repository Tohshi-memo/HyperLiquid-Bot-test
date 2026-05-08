# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T10:52:20.474787+00:00`
- Price records: `639`
- Market context records: `747`
- Flow alert records: `2109`
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

- `market_context_high->crypto_major_24h` score `12.9323` n `146` status `ready` deltaP `30.8232` edge `0.9056` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6226` n `146` status `ready` deltaP `7.6024` edge `0.506` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.307` n `146` status `ready` deltaP `2.159` edge `0.2107` maxDD `-5.9609`
- `market_context_high->fx_1h` score `-0.3204` n `165` status `ready` deltaP `4.2155` edge `0.003` maxDD `-0.291`
- `market_context_high->equity_24h` score `-0.327` n `146` status `ready` deltaP `0.5744` edge `0.2294` maxDD `-10.5047`
- `market_context_high->fx_4h` score `-0.4569` n `156` status `ready` deltaP `5.9805` edge `0.0092` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.5241` n `165` status `ready` deltaP `2.0506` edge `0.0401` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9332` n `165` status `ready` deltaP `0.6733` edge `0.0031` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0567` n `165` status `ready` deltaP `5.8983` edge `-0.0025` maxDD `-11.4508`
- `market_context_high->equity_1h` score `-1.0779` n `165` status `ready` deltaP `-1.2285` edge `-0.0006` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3941` n `165` status `ready` deltaP `4.7388` edge `-0.0163` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5161` n `165` status `ready` deltaP `-3.9561` edge `-0.0228` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.6174` n `156` status `ready` deltaP `17.2223` edge `0.121` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7771` n `156` status `ready` deltaP `1.572` edge `-0.0063` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-2.0238` n `165` status `ready` deltaP `-3.9656` edge `-0.0371` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.215` n `156` status `ready` deltaP `2.2945` edge `0.0571` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6149` n `156` status `ready` deltaP `-1.3359` edge `0.0062` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.7233` n `156` status `ready` deltaP `-5.7723` edge `0.0783` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.7887` n `156` status `ready` deltaP `4.874` edge `-0.1604` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.4147` n `146` status `ready` deltaP `-15.9453` edge `-0.0707` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
