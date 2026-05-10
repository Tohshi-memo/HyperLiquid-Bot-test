# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T08:22:18.748719+00:00`
- Price records: `672`
- Market context records: `956`
- Flow alert records: `2679`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.8335` n `159` status `ready` deltaP `32.7928` edge `1.0509` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `8.6717` n `159` status `ready` deltaP `9.2014` edge `0.6613` maxDD `0.0`
- `market_context_high->equity_24h` score `1.107` n `159` status `ready` deltaP `2.3585` edge `0.337` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.3555` n `159` status `ready` deltaP `0.9499` edge `0.2228` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2957` n `204` status `ready` deltaP `2.721` edge `0.038` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.6041` n `204` status `ready` deltaP `1.0098` edge `0.001` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.612` n `204` status `ready` deltaP `1.4794` edge `0.016` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.6983` n `204` status `ready` deltaP `3.2347` edge `0.0056` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-1.0345` n `192` status `ready` deltaP `1.7149` edge `0.002` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.0609` n `204` status `ready` deltaP `6.0878` edge `-0.0043` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.2099` n `192` status `ready` deltaP `2.6677` edge `0.0966` maxDD `-10.5498`
- `market_context_high->unknown_1h` score `-1.4318` n `204` status `ready` deltaP `-3.6222` edge `-0.018` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.4668` n `192` status `ready` deltaP `0.3049` edge `0.028` maxDD `-6.5149`
- `market_context_high->commodity_4h` score `-1.4822` n `192` status `ready` deltaP `-0.7749` edge `0.0819` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-1.8938` n `204` status `ready` deltaP `-2.5155` edge `-0.0301` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.922` n `204` status `ready` deltaP `1.2299` edge `-0.0244` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.4377` n `192` status `ready` deltaP `8.9939` edge `0.1075` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.2818` n `192` status `ready` deltaP `7.0249` edge `-0.1325` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.336` n `192` status `ready` deltaP `-2.2485` edge `0.0148` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.2601` n `159` status `ready` deltaP `6.1812` edge `-0.0368` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
