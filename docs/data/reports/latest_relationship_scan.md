# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T09:22:26.691566+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8073`

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

- `market_context_high->unknown_24h` score `1271.2179` n `148` status `ready` deltaP `-2.135` edge `106.0418` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `29.2596` n `149` status `ready` deltaP `4.385` edge `2.4243` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.5962` n `148` status `ready` deltaP `18.506` edge `-0.0049` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1566` n `149` status `ready` deltaP `7.1193` edge `0.0014` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.1315` n `149` status `ready` deltaP `10.0978` edge `0.0436` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1408` n `149` status `ready` deltaP `7.5785` edge `0.0061` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.149` n `149` status `ready` deltaP `6.6193` edge `0.0033` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.4559` n `149` status `ready` deltaP `5.333` edge `0.0343` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4799` n `149` status `ready` deltaP `1.3061` edge `0.0097` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.8123` n `149` status `ready` deltaP `7.8368` edge `-0.0023` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.859` n `149` status `ready` deltaP `-5.5701` edge `-0.0047` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.3751` n `148` status `ready` deltaP `4.9409` edge `0.0097` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5589` n `149` status `ready` deltaP `-0.7073` edge `-0.0039` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6624` n `149` status `ready` deltaP `1.5482` edge `0.0129` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.145` n `149` status `ready` deltaP `-10.0937` edge `-0.0326` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3722` n `149` status `ready` deltaP `2.5946` edge `-0.0177` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.7616` n `148` status `ready` deltaP `-2.7965` edge `0.0221` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.8697` n `148` status `ready` deltaP `-0.2393` edge `-0.0189` maxDD `-10.1587`
- `market_context_high->equity_4h` score `-5.4721` n `149` status `ready` deltaP `-4.3921` edge `-0.1489` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.8115` n `148` status `ready` deltaP `2.271` edge `-0.203` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
