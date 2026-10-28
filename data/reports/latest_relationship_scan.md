# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T20:52:32.884477+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8456`

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

- `market_context_high->unknown_24h` score `1234.4451` n `148` status `ready` deltaP `-2.135` edge `102.9774` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.2604` n `149` status `ready` deltaP `4.385` edge `1.7577` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.2355` n `148` status `ready` deltaP `22.6727` edge `0.0206` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1721` n `149` status `ready` deltaP `7.269` edge `0.0017` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1252` n `149` status `ready` deltaP `7.8779` edge `0.0061` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1698` n `149` status `ready` deltaP `6.3145` edge `0.0036` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.3702` n `149` status `ready` deltaP `7.3539` edge `0.042` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4247` n `149` status `ready` deltaP `5.9318` edge `0.0343` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5638` n `149` status `ready` deltaP `0.4079` edge `0.0087` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.589` n `148` status `ready` deltaP `12.2326` edge `0.0266` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.7772` n `149` status `ready` deltaP `-4.2228` edge `-0.0032` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8366` n `149` status `ready` deltaP `7.6844` edge `-0.0044` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4296` n `149` status `ready` deltaP `0.7897` edge `0.0027` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6585` n `149` status `ready` deltaP `1.9973` edge `0.0104` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1659` n `149` status `ready` deltaP `-10.5511` edge `-0.0313` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.4552` n `148` status `ready` deltaP `-0.7132` edge `0.0475` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4791` n `149` status `ready` deltaP `3.5092` edge `-0.0375` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5049` n `148` status `ready` deltaP `-0.2393` edge `0.0115` maxDD `-10.1587`
- `market_context_high->equity_24h` score `-3.6026` n `148` status `ready` deltaP `5.2224` edge `-0.0386` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.5262` n `149` status `ready` deltaP `-4.6969` edge `-0.1538` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
