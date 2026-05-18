# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T04:48:08.169542+00:00`
- Price records: `672`
- Market context records: `1084`
- Flow alert records: `5026`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8786`

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

- `market_context_high->crypto_major_24h` score `16.556` n `157` status `ready` deltaP `35.4782` edge `1.1895` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.8131` n `157` status `ready` deltaP `12.1836` edge `0.5266` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.5304` n `157` status `ready` deltaP `14.7945` edge `0.4119` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.6263` n `157` status `ready` deltaP `-2.6044` edge `0.5696` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.5571` n `157` status `ready` deltaP `14.9187` edge `0.3111` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.7147` n `162` status `ready` deltaP `9.7279` edge `0.1527` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.3004` n `162` status `ready` deltaP `12.5358` edge `0.1934` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.9047` n `162` status `ready` deltaP `7.7086` edge `0.0923` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.664` n `174` status `ready` deltaP `8.7187` edge `0.0289` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.469` n `174` status `ready` deltaP `2.7978` edge `0.0582` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1787` n `174` status `ready` deltaP `7.5246` edge `0.0413` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0429` n `174` status `ready` deltaP `7.177` edge `0.0013` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.0655` n `174` status `ready` deltaP `7.4816` edge `0.0057` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2203` n `174` status `ready` deltaP `3.333` edge `0.0437` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.345` n `162` status `ready` deltaP `7.5731` edge `0.1712` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.655` n `162` status `ready` deltaP `2.0495` edge `0.002` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6939` n `174` status `ready` deltaP `-1.2269` edge `0.0` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.9162` n `162` status `ready` deltaP `4.7463` edge `-0.0819` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.0363` n `162` status `ready` deltaP `8.6645` edge `-0.1058` maxDD `-6.7322`
- `market_context_high->fx_24h` score `-3.108` n `157` status `ready` deltaP `4.7362` edge `-0.0224` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
