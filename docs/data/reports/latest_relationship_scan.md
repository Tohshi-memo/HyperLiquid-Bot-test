# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T02:52:16.871161+00:00`
- Price records: `672`
- Market context records: `1280`
- Flow alert records: `5595`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.8201` n `128` status `ready` deltaP `41.5798` edge `1.321` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.0855` n `128` status `ready` deltaP `7.2917` edge `1.0419` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.9153` n `128` status `ready` deltaP `25.7812` edge `0.7727` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.4243` n `128` status `ready` deltaP `28.2986` edge `0.372` maxDD `-5.3574`
- `market_context_high->unknown_4h` score `4.3851` n `138` status `ready` deltaP `4.0761` edge `0.4724` maxDD `-6.7322`
- `market_context_high->equity_24h` score `3.907` n `128` status `ready` deltaP `25.3472` edge `0.5646` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.9207` n `138` status `ready` deltaP `14.5833` edge `0.2125` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3634` n `128` status `ready` deltaP `1.5625` edge `0.4595` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.5469` n `128` status `ready` deltaP `-13.3681` edge `0.3662` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.2851` n `138` status `ready` deltaP `9.9285` edge `0.1092` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.613` n `138` status `ready` deltaP `16.2115` edge `0.0861` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.5148` n `150` status `ready` deltaP `5.507` edge `0.0489` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.4437` n `150` status `ready` deltaP `7.6028` edge `0.024` maxDD `-1.0166`
- `market_context_high->metal_1h` score `0.3431` n `150` status `ready` deltaP `11.0739` edge `0.0158` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.2356` n `128` status `ready` deltaP `4.948` edge `0.0331` maxDD `-0.3831`
- `market_context_high->crypto_alt_1h` score `-0.2594` n `150` status `ready` deltaP `1.7545` edge `0.0421` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.3912` n `150` status `ready` deltaP `-0.0279` edge `-0.0044` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.4145` n `138` status `ready` deltaP `5.7153` edge `0.1461` maxDD `-11.9879`
- `market_context_high->crypto_major_1h` score `-0.6882` n `150` status `ready` deltaP `0.6806` edge `0.0093` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8441` n `138` status `ready` deltaP `8.2405` edge `0.1688` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
