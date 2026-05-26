# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T19:22:21.072302+00:00`
- Price records: `672`
- Market context records: `1967`
- Flow alert records: `7558`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7583`

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

- `market_context_high->crypto_alt_4h` score `7.3124` n `234` status `ready` deltaP `22.5649` edge `0.5734` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7302` n `234` status `ready` deltaP `26.1987` edge `0.5108` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4193` n `234` status `ready` deltaP `13.5906` edge `0.3134` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.3586` n `234` status `ready` deltaP `14.8205` edge `0.2072` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.455` n `199` status `ready` deltaP `16.9339` edge `0.5404` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.101` n `199` status `ready` deltaP `14.2132` edge `0.2396` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `1.0112` n `234` status `ready` deltaP `9.4017` edge `0.1202` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.8243` n `234` status `ready` deltaP `8.3948` edge `0.1241` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.6156` n `199` status `ready` deltaP `12.8916` edge `0.4552` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.3865` n `199` status `ready` deltaP `4.1922` edge `0.1271` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.2672` n `234` status `ready` deltaP `8.4402` edge `0.0749` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0407` n `234` status `ready` deltaP `5.3982` edge `0.04` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2024` n `199` status `ready` deltaP `10.446` edge `0.0184` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5837` n `234` status `ready` deltaP `0.6347` edge `0.0103` maxDD `-1.7205`
- `market_context_high->crypto_major_24h` score `-0.6523` n `199` status `ready` deltaP `17.4331` edge `0.688` maxDD `-62.3533`
- `market_context_high->fx_1h` score `-0.6849` n `234` status `ready` deltaP `-3.612` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1183` n `234` status `ready` deltaP `-7.6871` edge `-0.0033` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2065` n `234` status `ready` deltaP `3.8462` edge `0.0074` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.6019` n `234` status `ready` deltaP `0.5093` edge `-0.0417` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.87` n `234` status `ready` deltaP `6.6227` edge `0.0692` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
