# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T11:22:29.696020+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1254.8806` n `149` status `ready` deltaP `-2.0216` edge `104.6796` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `31.768` n `149` status `ready` deltaP `4.6898` edge `2.6313` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.5169` n `149` status `ready` deltaP `17.9204` edge `-0.0076` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.0907` n `149` status `ready` deltaP `6.3708` edge `0.0009` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.0963` n `149` status `ready` deltaP `10.4027` edge `0.0445` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.1404` n `149` status `ready` deltaP `6.7718` edge `0.003` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1533` n `149` status `ready` deltaP `7.4288` edge `0.0055` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.4763` n `149` status `ready` deltaP `1.3061` edge `0.01` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.5159` n `149` status `ready` deltaP `5.0336` edge `0.0286` maxDD `-6.9306`
- `market_context_high->metal_4h` score `-0.8123` n `149` status `ready` deltaP `7.8368` edge `-0.0023` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8442` n `149` status `ready` deltaP `-5.2707` edge `-0.0048` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.4629` n `149` status `ready` deltaP `4.0385` edge `0.0084` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5604` n `149` status `ready` deltaP `-0.7073` edge `-0.0041` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.7247` n `149` status `ready` deltaP `1.0991` edge `0.0079` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1875` n `149` status `ready` deltaP `-10.5511` edge `-0.0331` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4381` n `149` status `ready` deltaP `2.1373` edge `-0.0231` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.6529` n `149` status `ready` deltaP `-1.9213` edge `0.0302` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.9749` n `149` status `ready` deltaP `-0.5069` edge `-0.0215` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-5.545` n `149` status `ready` deltaP `-4.8494` edge `-0.1552` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9669` n `149` status `ready` deltaP `1.813` edge `-0.2129` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
