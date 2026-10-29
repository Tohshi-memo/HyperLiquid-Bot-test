# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T11:37:27.085229+00:00`
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

- `market_context_high->unknown_24h` score `1255.6342` n `149` status `ready` deltaP `-2.0216` edge `104.7424` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `31.6886` n `149` status `ready` deltaP `4.5374` edge `2.6257` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.5145` n `149` status `ready` deltaP `17.9204` edge `-0.0078` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.0919` n `149` status `ready` deltaP `6.3708` edge `0.001` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.0963` n `149` status `ready` deltaP `10.4027` edge `0.0445` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.1392` n `149` status `ready` deltaP `6.7718` edge `0.0031` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1447` n `149` status `ready` deltaP `7.5785` edge `0.0056` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.4631` n `149` status `ready` deltaP `1.4558` edge `0.0101` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.5323` n `149` status `ready` deltaP `4.8839` edge `0.0275` maxDD `-6.9306`
- `market_context_high->metal_4h` score `-0.8115` n `149` status `ready` deltaP `7.8368` edge `-0.0022` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8356` n `149` status `ready` deltaP `-5.121` edge `-0.0047` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.4641` n `149` status `ready` deltaP `4.0385` edge `0.0083` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5597` n `149` status `ready` deltaP `-0.7073` edge `-0.004` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.7364` n `149` status `ready` deltaP `0.9494` edge `0.0074` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.2009` n `149` status `ready` deltaP `-10.7035` edge `-0.0332` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4679` n `149` status `ready` deltaP `1.9848` edge `-0.0259` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.6412` n `149` status `ready` deltaP `-1.9213` edge `0.0317` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.9701` n `149` status `ready` deltaP `-0.5069` edge `-0.0211` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-5.5725` n `149` status `ready` deltaP `-5.0018` edge `-0.1577` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9693` n `149` status `ready` deltaP `1.813` edge `-0.2131` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
