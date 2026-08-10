# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T20:26:45.697403+00:00`
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

- `market_context_high->fx_24h` score `0.9489` n `145` status `ready` deltaP `20.4064` edge `0.0238` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9356` n `179` status `ready` deltaP `12.5137` edge `0.066` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6716` n `188` status `ready` deltaP `9.205` edge `0.0289` maxDD `-0.7439`
- `market_context_high->equity_24h` score `0.5935` n `145` status `ready` deltaP `2.4072` edge `0.3843` maxDD `-21.0709`
- `market_context_high->fx_1h` score `-0.1063` n `188` status `ready` deltaP `4.6853` edge `0.0003` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1354` n `179` status `ready` deltaP `6.2687` edge `0.0069` maxDD `-0.4647`
- `market_context_high->index_24h` score `-0.4096` n `145` status `ready` deltaP `2.2519` edge `0.104` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.597` n `188` status `ready` deltaP `-3.8763` edge `-0.0028` maxDD `-0.832`
- `market_context_high->metal_24h` score `-0.6762` n `145` status `ready` deltaP `2.5482` edge `0.0591` maxDD `-2.9283`
- `market_context_high->index_4h` score `-0.815` n `179` status `ready` deltaP `-2.5685` edge `-0.0088` maxDD `-1.2849`
- `market_context_high->equity_1h` score `-1.043` n `188` status `ready` deltaP `-3.4144` edge `-0.0073` maxDD `-5.9591`
- `market_context_high->metal_1h` score `-1.1968` n `188` status `ready` deltaP `-4.1438` edge `-0.0085` maxDD `-2.0884`
- `market_context_high->metal_4h` score `-1.952` n `179` status `ready` deltaP `-6.026` edge `-0.0337` maxDD `-6.1111`
- `market_context_high->crypto_alt_1h` score `-2.7046` n `188` status `ready` deltaP `-9.6955` edge `-0.041` maxDD `-6.5795`
- `market_context_high->equity_4h` score `-3.3197` n `179` status `ready` deltaP `-11.5581` edge `-0.0899` maxDD `-11.6916`
- `market_context_high->crypto_major_1h` score `-3.6023` n `188` status `ready` deltaP `-9.0107` edge `-0.0497` maxDD `-11.9002`
- `market_context_high->crypto_major_24h` score `-3.6779` n `145` status `ready` deltaP `-0.8498` edge `-0.0514` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.159` n `145` status `ready` deltaP `-12.8226` edge `-0.1557` maxDD `-8.0985`
- `market_context_high->crypto_alt_4h` score `-6.022` n `179` status `ready` deltaP `-11.7106` edge `-0.1302` maxDD `-16.8181`
- `market_context_high->commodity_24h` score `-8.3524` n `145` status `ready` deltaP `-4.616` edge `-0.1685` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
