# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T21:37:27.589852+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8464`

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

- `market_context_high->unknown_24h` score `1237.6527` n `148` status `ready` deltaP `-2.135` edge `103.2447` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.0252` n `149` status `ready` deltaP `4.385` edge `1.7381` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.1615` n `148` status `ready` deltaP `22.1519` edge `0.0179` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1841` n `149` status `ready` deltaP `7.4187` edge `0.0017` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.126` n `149` status `ready` deltaP `7.8779` edge `0.006` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.132` n `149` status `ready` deltaP `6.7718` edge `0.0037` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.3267` n `149` status `ready` deltaP `7.6588` edge `0.0436` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4138` n `149` status `ready` deltaP `6.0815` edge `0.0347` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.6045` n `149` status `ready` deltaP `-0.0412` edge `0.0083` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.6474` n `148` status `ready` deltaP `11.7117` edge `0.0252` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.7577` n `149` status `ready` deltaP `-3.9234` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8682` n `149` status `ready` deltaP `7.227` edge `-0.0054` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.407` n `149` status `ready` deltaP `0.9394` edge `0.0046` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6437` n `149` status `ready` deltaP `2.147` edge `0.0113` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1647` n `149` status `ready` deltaP `-10.5511` edge `-0.0312` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5049` n `149` status `ready` deltaP `3.5092` edge `-0.0408` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5313` n `148` status `ready` deltaP `-0.2393` edge `0.0093` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.54` n `148` status `ready` deltaP `-1.234` edge `0.0401` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-3.847` n `148` status `ready` deltaP `4.7015` edge `-0.0555` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.5379` n `149` status `ready` deltaP `-4.6969` edge `-0.1553` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
