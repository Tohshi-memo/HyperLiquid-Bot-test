# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T01:07:26.970851+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8202`

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

- `market_context_high->commodity_24h` score `2.0732` n `69` status `ready` deltaP `20.3125` edge `0.1225` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `1.045` n `39` status `ready` deltaP `18.4247` edge `0.0535` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `1.045` n `39` status `ready` deltaP `18.4247` edge `0.0535` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.657` n `39` status `ready` deltaP `15.281` edge `0.0094` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.657` n `39` status `ready` deltaP `15.281` edge `0.0094` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.0822` n `39` status `ready` deltaP `15.1843` edge `-0.0146` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0822` n `39` status `ready` deltaP `15.1843` edge `-0.0146` maxDD `-1.7154`
- `risk_on_high->index_4h` score `-0.0967` n `39` status `ready` deltaP `8.2669` edge `0.017` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0967` n `39` status `ready` deltaP `8.2669` edge `0.017` maxDD `-0.7604`
- `market_context_high->index_1h` score `-0.1028` n `88` status `ready` deltaP `3.7425` edge `0.002` maxDD `-0.5082`
- `risk_on_high->equity_4h` score `-0.1473` n `39` status `ready` deltaP `5.2728` edge `0.0714` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.1473` n `39` status `ready` deltaP `5.2728` edge `0.0714` maxDD `-4.0351`
- `market_context_high->metal_1h` score `-0.1747` n `88` status `ready` deltaP `1.3201` edge `0.0063` maxDD `-0.6669`
- `risk_on_high->fx_1h` score `-0.252` n `39` status `ready` deltaP `0.3839` edge `-0.0003` maxDD `-0.0985`
- `risk_on_and_context->fx_1h` score `-0.252` n `39` status `ready` deltaP `0.3839` edge `-0.0003` maxDD `-0.0985`
- `risk_on_high->metal_1h` score `-0.2857` n `39` status `ready` deltaP `-2.8175` edge `0.0082` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.2857` n `39` status `ready` deltaP `-2.8175` edge `0.0082` maxDD `-0.0831`
- `risk_on_high->fx_4h` score `-0.3922` n `39` status `ready` deltaP `-3.2364` edge `-0.0023` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3922` n `39` status `ready` deltaP `-3.2364` edge `-0.0023` maxDD `-0.1126`
- `market_context_high->crypto_major_1h` score `-0.4004` n `88` status `ready` deltaP `1.1908` edge `0.0424` maxDD `-4.8007`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
