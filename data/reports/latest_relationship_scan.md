# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T18:37:10.720457+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->equity_24h` score `1.7415` n `138` status `ready` deltaP `4.7622` edge `0.4351` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.8439` n `174` status `ready` deltaP `11.7431` edge `0.0635` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7597` n `182` status `ready` deltaP `10.0958` edge `0.0303` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7474` n `138` status `ready` deltaP `19.147` edge `0.0154` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.1178` n `182` status `ready` deltaP `4.4483` edge `0.0004` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1486` n `174` status `ready` deltaP `6.0888` edge `0.007` maxDD `-0.4647`
- `market_context_high->index_24h` score `-0.186` n `138` status `ready` deltaP `4.432` edge `0.1081` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6077` n `182` status `ready` deltaP `-3.9909` edge `-0.0036` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.7917` n `138` status `ready` deltaP `1.3588` edge `0.0574` maxDD `-2.9283`
- `market_context_high->metal_1h` score `-0.8483` n `182` status `ready` deltaP `-5.1375` edge `-0.0109` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.0438` n `182` status `ready` deltaP `-3.3855` edge `-0.0165` maxDD `-5.247`
- `market_context_high->index_4h` score `-1.2068` n `174` status `ready` deltaP `-1.7575` edge `-0.0106` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.8097` n `182` status `ready` deltaP `-10.382` edge `-0.0459` maxDD `-6.3518`
- `market_context_high->metal_4h` score `-2.0426` n `174` status `ready` deltaP `-7.1979` edge `-0.0375` maxDD `-6.1111`
- `market_context_high->crypto_major_24h` score `-3.1587` n `138` status `ready` deltaP `1.1554` edge `-0.0215` maxDD `-14.2873`
- `market_context_high->equity_4h` score `-3.2396` n `174` status `ready` deltaP `-11.1404` edge `-0.1073` maxDD `-9.7016`
- `market_context_high->crypto_alt_24h` score `-3.8337` n `138` status `ready` deltaP `-10.3308` edge `-0.1063` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.9028` n `182` status `ready` deltaP `-10.637` edge `-0.0639` maxDD `-11.9002`
- `market_context_high->crypto_alt_4h` score `-5.9454` n `174` status `ready` deltaP `-11.5626` edge `-0.1362` maxDD `-15.9063`
- `market_context_high->commodity_24h` score `-8.7518` n `138` status `ready` deltaP `-5.7117` edge `-0.2124` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
