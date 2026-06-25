# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T17:22:44.815649+00:00`
- Price records: `672`
- Market context records: `4744`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7470`

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

- `market_context_high->unknown_1h` score `82.3504` n `137` status `ready` deltaP `14.1593` edge `6.8099` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1972` n `134` status `ready` deltaP `12.4864` edge `0.4709` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.2241` n `125` status `ready` deltaP `15.9611` edge `0.2546` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.383` n `134` status `ready` deltaP `7.631` edge `0.0069` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.4955` n `137` status `ready` deltaP `2.3854` edge `0.0224` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.5315` n `134` status `ready` deltaP `6.4115` edge `0.0577` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.9082` n `134` status `ready` deltaP `-0.9874` edge `-0.003` maxDD `-1.882`
- `market_context_high->equity_1h` score `-0.9382` n `137` status `ready` deltaP `-1.3943` edge `-0.0147` maxDD `-5.37`
- `market_context_high->fx_1h` score `-1.2092` n `137` status `ready` deltaP `-4.3894` edge `-0.005` maxDD `-0.9869`
- `market_context_high->index_1h` score `-1.5302` n `137` status `ready` deltaP `-2.9099` edge `-0.0077` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.6405` n `134` status `ready` deltaP `7.0919` edge `0.018` maxDD `-9.1588`
- `market_context_high->commodity_24h` score `-2.474` n `125` status `ready` deltaP `17.6556` edge `0.076` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.5239` n `137` status `ready` deltaP `-3.1918` edge `-0.0693` maxDD `-15.3067`
- `market_context_high->crypto_alt_1h` score `-2.6331` n `137` status `ready` deltaP `-0.047` edge `-0.0394` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.1471` n `137` status `ready` deltaP `0.7201` edge `-0.0629` maxDD `-24.9637`
- `market_context_high->fx_24h` score `-4.3509` n `125` status `ready` deltaP `-14.3236` edge `-0.0199` maxDD `-4.7749`
- `market_context_high->crypto_alt_4h` score `-5.7661` n `134` status `ready` deltaP `1.3878` edge `-0.0466` maxDD `-50.8181`
- `market_context_high->index_24h` score `-7.28` n `125` status `ready` deltaP `-10.9597` edge `-0.1037` maxDD `-24.0589`
- `market_context_high->metal_4h` score `-8.4345` n `134` status `ready` deltaP `2.96` edge `-0.277` maxDD `-61.2596`
- `market_context_high->crypto_major_4h` score `-8.503` n `134` status `ready` deltaP `1.7246` edge `-0.1526` maxDD `-70.5889`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
