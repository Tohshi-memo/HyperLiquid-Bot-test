# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T02:22:39.056565+00:00`
- Price records: `672`
- Market context records: `4049`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10528`

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

- `risk_on_high->unknown_4h` score `144.8747` n `40` status `ready` deltaP `-8.2012` edge `12.3092` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.8747` n `40` status `ready` deltaP `-8.2012` edge `12.3092` maxDD `-10.864`
- `market_context_high->unknown_24h` score `42.803` n `138` status `ready` deltaP `-7.9986` edge `4.0231` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `21.7844` n `157` status `ready` deltaP `1.1778` edge `2.3498` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `3.9907` n `40` status `ready` deltaP `33.9688` edge `0.1061` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.9907` n `40` status `ready` deltaP `33.9688` edge `0.1061` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.641` n `40` status `ready` deltaP `37.8963` edge `0.0555` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.641` n `40` status `ready` deltaP `37.8963` edge `0.0555` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.2463` n `138` status `ready` deltaP `20.9392` edge `0.0688` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.8403` n `157` status `ready` deltaP `16.1925` edge `0.1735` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.1573` n `40` status `ready` deltaP `19.6037` edge `0.0323` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1573` n `40` status `ready` deltaP `19.6037` edge `0.0323` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8356` n `169` status `ready` deltaP `6.4345` edge `0.0827` maxDD `-2.144`
- `market_context_high->metal_24h` score `0.4598` n `138` status `ready` deltaP `8.4332` edge `0.0808` maxDD `-4.8962`
- `risk_on_high->equity_1h` score `0.4496` n `40` status `ready` deltaP `11.2126` edge `0.0018` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4496` n `40` status `ready` deltaP `11.2126` edge `0.0018` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.1694` n `40` status `ready` deltaP `12.3054` edge `-0.0061` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1694` n `40` status `ready` deltaP `12.3054` edge `-0.0061` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `0.1081` n `40` status `ready` deltaP `0.5633` edge `0.2334` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.1081` n `40` status `ready` deltaP `0.5633` edge `0.2334` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
