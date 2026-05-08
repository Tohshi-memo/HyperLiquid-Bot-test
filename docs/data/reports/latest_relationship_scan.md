# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T12:07:17.454418+00:00`
- Price records: `644`
- Market context records: `753`
- Flow alert records: `2125`
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

- `market_context_high->crypto_major_24h` score `13.158` n `146` status `ready` deltaP `31.3793` edge `0.9207` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6597` n `146` status `ready` deltaP `7.5268` edge `0.5096` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.4579` n `146` status `ready` deltaP `2.8002` edge `0.219` maxDD `-5.9609`
- `market_context_high->equity_24h` score `-0.1292` n `146` status `ready` deltaP `1.2616` edge `0.2413` maxDD `-10.5047`
- `market_context_high->fx_1h` score `-0.2579` n `170` status `ready` deltaP `3.3204` edge `0.0026` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.422` n `159` status `ready` deltaP `6.371` edge `0.0095` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6426` n `170` status `ready` deltaP `0.9896` edge `0.0373` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7301` n `170` status `ready` deltaP `-1.676` edge `-0.0014` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.9273` n `170` status `ready` deltaP `0.6419` edge `0.0038` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-0.9958` n `170` status `ready` deltaP `6.7555` edge `-0.0004` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3079` n `170` status `ready` deltaP `5.4871` edge `-0.0141` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5689` n `170` status `ready` deltaP `-4.5404` edge `-0.0233` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.5907` n `159` status `ready` deltaP `17.4068` edge `0.122` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7336` n `159` status `ready` deltaP `1.9351` edge `-0.0051` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-2.0334` n `170` status `ready` deltaP `-4.2096` edge `-0.0367` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.1571` n `159` status `ready` deltaP `2.5979` edge `0.0599` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.5588` n `159` status `ready` deltaP `-0.9495` edge `0.0083` maxDD `-10.5498`
- `market_context_high->unknown_4h` score `-3.6843` n `159` status `ready` deltaP `5.2337` edge `-0.1541` maxDD `-8.3588`
- `market_context_high->commodity_4h` score `-3.7666` n `159` status `ready` deltaP `-5.9537` edge `0.0759` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-5.4621` n `146` status `ready` deltaP `-16.4535` edge `-0.0734` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
