# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T20:37:29.628979+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8416`

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

- `market_context_high->unknown_24h` score `1232.5095` n `148` status `ready` deltaP `-2.135` edge `102.8161` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.3552` n `149` status `ready` deltaP `4.385` edge `1.7656` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.2602` n `148` status `ready` deltaP `22.8463` edge `0.0215` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.159` n `149` status `ready` deltaP `7.1193` edge `0.0016` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1237` n `149` status `ready` deltaP `7.8779` edge `0.0063` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1832` n `149` status `ready` deltaP `6.162` edge `0.0035` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.3884` n `149` status `ready` deltaP `7.2015` edge `0.0415` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4247` n `149` status `ready` deltaP `5.9318` edge `0.0343` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5793` n `149` status `ready` deltaP `0.2582` edge `0.0084` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.5842` n `148` status `ready` deltaP `12.2326` edge `0.027` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.7788` n `149` status `ready` deltaP `-4.2228` edge `-0.0034` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8256` n `149` status `ready` deltaP `7.8368` edge `-0.004` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.442` n `149` status `ready` deltaP `0.7897` edge `0.0011` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6601` n `149` status `ready` deltaP `1.9973` edge `0.0102` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1659` n `149` status `ready` deltaP `-10.5511` edge `-0.0313` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.4274` n `148` status `ready` deltaP `-0.5396` edge `0.0499` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4737` n `149` status `ready` deltaP `3.5092` edge `-0.0368` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.4953` n `148` status `ready` deltaP `-0.2393` edge `0.0123` maxDD `-10.1587`
- `market_context_high->equity_24h` score `-3.5239` n `148` status `ready` deltaP `5.396` edge `-0.0332` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.527` n `149` status `ready` deltaP `-4.6969` edge `-0.1539` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
