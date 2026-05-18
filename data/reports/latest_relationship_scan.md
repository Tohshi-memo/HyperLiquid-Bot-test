# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T03:52:14.510448+00:00`
- Price records: `672`
- Market context records: `1080`
- Flow alert records: `5015`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.4491` n `158` status `ready` deltaP `35.2367` edge `1.1822` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.7668` n `158` status `ready` deltaP `12.1005` edge `0.5233` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.5007` n `158` status `ready` deltaP `14.6935` edge `0.4101` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.6053` n `158` status `ready` deltaP `-2.5962` edge `0.5678` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.5381` n `158` status `ready` deltaP `14.817` edge `0.3102` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5269` n `160` status `ready` deltaP `9.0701` edge `0.1456` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.4667` n `160` status `ready` deltaP `13.3689` edge `0.2017` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.8568` n `160` status `ready` deltaP `7.4848` edge `0.0898` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5977` n `171` status `ready` deltaP `7.9796` edge `0.0283` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4543` n `171` status `ready` deltaP `2.6884` edge `0.0577` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1732` n `171` status `ready` deltaP `6.9685` edge `0.0405` maxDD `-3.8021`
- `market_context_high->fx_1h` score `-0.0143` n `171` status `ready` deltaP `6.4914` edge `0.0011` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1708` n `171` status `ready` deltaP `7.0062` edge `0.0001` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2347` n `171` status `ready` deltaP `3.0623` edge `0.0443` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3764` n `160` status `ready` deltaP `7.2104` edge `0.171` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.691` n `160` status `ready` deltaP `1.4939` edge `0.0011` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-1.0518` n `171` status `ready` deltaP `-1.2703` edge `0.0016` maxDD `-3.7959`
- `market_context_high->unknown_4h` score `-1.353` n `160` status `ready` deltaP `9.4207` edge `-0.0539` maxDD `-6.7322`
- `market_context_high->metal_4h` score `-1.9822` n `160` status `ready` deltaP `4.4512` edge `-0.0884` maxDD `-9.2991`
- `market_context_high->fx_24h` score `-3.109` n `158` status `ready` deltaP `4.6861` edge `-0.0222` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
