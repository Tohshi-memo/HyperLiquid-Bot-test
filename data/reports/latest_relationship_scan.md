# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T20:52:37.884834+00:00`
- Price records: `672`
- Market context records: `4025`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10720`

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

- `risk_on_high->unknown_4h` score `145.9428` n `40` status `ready` deltaP `-6.2195` edge `12.385` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.9428` n `40` status `ready` deltaP `-6.2195` edge `12.385` maxDD `-10.864`
- `market_context_high->unknown_24h` score `47.6447` n `134` status `ready` deltaP `-5.3325` edge `4.4088` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `25.6087` n `148` status `ready` deltaP `1.821` edge `2.6642` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `5.8869` n `40` status `ready` deltaP `37.7816` edge `0.2387` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.8869` n `40` status `ready` deltaP `37.7816` edge `0.2387` maxDD `0.0`
- `market_context_high->index_24h` score `3.2756` n `134` status `ready` deltaP `24.7303` edge `0.1293` maxDD `-1.3629`
- `risk_on_high->equity_4h` score `3.2387` n `40` status `ready` deltaP `35.7622` edge `0.0362` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2387` n `40` status `ready` deltaP `35.7622` edge `0.0362` maxDD `-0.0446`
- `market_context_high->metal_24h` score `2.1424` n `134` status `ready` deltaP `12.7409` edge `0.1923` maxDD `-4.8962`
- `market_context_high->equity_4h` score `2.0996` n `148` status `ready` deltaP `18.6676` edge `0.1786` maxDD `-6.9137`
- `market_context_high->equity_1h` score `1.2073` n `155` status `ready` deltaP `8.6209` edge `0.0991` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.0397` n `40` status `ready` deltaP `18.689` edge `0.0286` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0397` n `40` status `ready` deltaP `18.689` edge `0.0286` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.8984` n `40` status `ready` deltaP `4.2028` edge `0.275` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.8984` n `40` status `ready` deltaP `4.2028` edge `0.275` maxDD `-12.9187`
- `risk_on_high->index_24h` score `0.8333` n `40` status `ready` deltaP `25.4766` edge `-0.1004` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.8333` n `40` status `ready` deltaP `25.4766` edge `-0.1004` maxDD `0.0`
- `market_context_high->crypto_major_1h` score `0.6335` n `155` status `ready` deltaP `7.7545` edge `0.056` maxDD `-2.3923`
- `market_context_high->metal_1h` score `0.4544` n `155` status `ready` deltaP `10.2067` edge `0.0506` maxDD `-2.8309`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
