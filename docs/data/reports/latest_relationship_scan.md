# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T17:07:50.733161+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14761`

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

- `news_risk_high->unknown_24h` score `52.0386` n `50` status `ready` deltaP `11.6319` edge `4.259` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.0498` n `50` status `ready` deltaP `37.8403` edge `1.546` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `13.0877` n `50` status `ready` deltaP `27.5366` edge `0.917` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.7344` n `50` status `ready` deltaP `46.0903` edge `0.0915` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.5583` n `50` status `ready` deltaP `25.8403` edge `0.3004` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0101` n `50` status `ready` deltaP `46.7256` edge `0.0317` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.087` n `50` status `ready` deltaP `17.4251` edge `0.1767` maxDD `-0.8495`
- `market_context_high->unknown_4h` score `2.6447` n `148` status `ready` deltaP `20.6988` edge `0.1231` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.6371` n `50` status `ready` deltaP `29.8403` edge `0.0359` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.6142` n `128` status `ready` deltaP `5.3819` edge `0.2552` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5695` n `50` status `ready` deltaP `20.9521` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1762` n `50` status `ready` deltaP `16.9641` edge `0.0128` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.9636` n `148` status `ready` deltaP `9.7224` edge `0.0605` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7359` n `50` status `ready` deltaP `18.5305` edge `0.0141` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.53` n `50` status `ready` deltaP `14.5988` edge `0.0019` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1468` n `50` status `ready` deltaP `7.8084` edge `0.0007` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0703` n `50` status `ready` deltaP `4.9521` edge `-0.0014` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0691` n `50` status `ready` deltaP `7.4634` edge `-0.0024` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1159` n `50` status `ready` deltaP `4.7988` edge `-0.002` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4261` n `148` status `ready` deltaP `6.3283` edge `-0.0051` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
