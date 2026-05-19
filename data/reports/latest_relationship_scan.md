# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T04:52:19.210048+00:00`
- Price records: `672`
- Market context records: `1187`
- Flow alert records: `5323`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5982` n `142` status `ready` deltaP `44.376` edge `1.3672` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `8.0906` n `142` status `ready` deltaP `22.1929` edge `0.7279` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.3437` n `142` status `ready` deltaP `-3.0908` edge `0.5493` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `3.0013` n `142` status `ready` deltaP `4.9296` edge `0.3389` maxDD `-6.7322`
- `market_context_high->equity_4h` score `2.7836` n `142` status `ready` deltaP `14.8939` edge `0.199` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.4559` n `142` status `ready` deltaP `15.3144` edge `0.2112` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4287` n `142` status `ready` deltaP `15.6421` edge `0.3308` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.0965` n `142` status `ready` deltaP `10.6321` edge `0.0888` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6854` n `142` status `ready` deltaP `9.7663` edge `0.0237` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3456` n `142` status `ready` deltaP `3.3398` edge `0.0443` maxDD `-1.3546`
- `market_context_high->fx_1h` score `-0.0631` n `142` status `ready` deltaP `5.7118` edge `-0.0006` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1493` n `142` status `ready` deltaP `6.9113` edge `0.1269` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.2527` n `142` status `ready` deltaP `7.7971` edge `-0.012` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3197` n `142` status `ready` deltaP `3.732` edge `0.0107` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.505` n `142` status `ready` deltaP `-0.7147` edge `0.0243` maxDD `-3.4088`
- `market_context_high->fx_24h` score `-0.5883` n `142` status `ready` deltaP `6.4285` edge `0.0316` maxDD `-7.3234`
- `market_context_high->commodity_1h` score `-0.9895` n `142` status `ready` deltaP `-3.3714` edge `0.0015` maxDD `-2.252`
- `market_context_high->fx_4h` score `-0.9899` n `142` status `ready` deltaP `-4.5366` edge `-0.0052` maxDD `-0.984`
- `market_context_high->commodity_24h` score `-1.0516` n `142` status `ready` deltaP `-4.888` edge `0.4473` maxDD `-38.9628`
- `market_context_high->crypto_alt_4h` score `-1.3197` n `142` status `ready` deltaP `3.4352` edge `0.1044` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
