# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T05:07:28.305852+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10534`

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

- `risk_on_high->commodity_24h` score `4.4068` n `62` status `ready` deltaP `26.4696` edge `0.2364` maxDD `-0.9837`
- `risk_on_and_context->commodity_24h` score `4.4068` n `62` status `ready` deltaP `26.4696` edge `0.2364` maxDD `-0.9837`
- `market_context_high->commodity_24h` score `1.9371` n `116` status `ready` deltaP `15.2349` edge `0.1628` maxDD `-3.9021`
- `market_context_high->crypto_major_4h` score `1.5682` n `156` status `ready` deltaP `15.3495` edge `0.3688` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.5206` n `156` status `ready` deltaP `4.4219` edge `0.1028` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.1479` n `156` status `ready` deltaP `7.5234` edge `0.1188` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1413` n `91` status `ready` deltaP `13.1517` edge `0.1785` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1413` n `91` status `ready` deltaP `13.1517` edge `0.1785` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0629` n `91` status `ready` deltaP `4.1052` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0629` n `91` status `ready` deltaP `4.1052` edge `0.0058` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1701` n `156` status `ready` deltaP `7.2188` edge `0.0049` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3917` n `156` status `ready` deltaP `6.8402` edge `0.0087` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4512` n `91` status `ready` deltaP `9.2582` edge `0.0303` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4512` n `91` status `ready` deltaP `9.2582` edge `0.0303` maxDD `-5.3696`
- `market_context_high->fx_1h` score `-0.5107` n `156` status `ready` deltaP `-1.7326` edge `-0.0018` maxDD `-0.503`
- `risk_on_high->metal_1h` score `-0.5257` n `91` status `ready` deltaP `0.2467` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5257` n `91` status `ready` deltaP `0.2467` edge `0.0041` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5503` n `156` status `ready` deltaP `6.7112` edge `0.0431` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
