# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T18:07:28.322409+00:00`
- Price records: `672`
- Market context records: `7378`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `6.3056` n `32` status `ready` deltaP `35.8994` edge `0.3054` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.3056` n `32` status `ready` deltaP `35.8994` edge `0.3054` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `5.0271` n `32` status `ready` deltaP `16.0061` edge `0.3552` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.0271` n `32` status `ready` deltaP `16.0061` edge `0.3552` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.9752` n `32` status `ready` deltaP `28.7348` edge `0.2474` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.9752` n `32` status `ready` deltaP `28.7348` edge `0.2474` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.0967` n `32` status `ready` deltaP `19.1804` edge `0.0372` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.0967` n `32` status `ready` deltaP `19.1804` edge `0.0372` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.3628` n `32` status `ready` deltaP `5.0488` edge `0.0245` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.3628` n `32` status `ready` deltaP `5.0488` edge `0.0245` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1039` n `32` status `ready` deltaP `3.4535` edge `0.028` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1039` n `32` status `ready` deltaP `3.4535` edge `0.028` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0083` n `32` status `ready` deltaP `-0.2994` edge `0.038` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0083` n `32` status `ready` deltaP `-0.2994` edge `0.038` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1535` n `129` status `ready` deltaP `4.3893` edge `0.0` maxDD `-0.5821`
- `risk_on_high->metal_4h` score `-0.2798` n `32` status `ready` deltaP `-1.5244` edge `0.0692` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.2798` n `32` status `ready` deltaP `-1.5244` edge `0.0692` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.6402` n `129` status `ready` deltaP `-2.364` edge `-0.0091` maxDD `-1.5775`
- `market_context_high->commodity_4h` score `-0.7128` n `129` status `ready` deltaP `-0.1707` edge `0.0066` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-0.7753` n `129` status `ready` deltaP `3.9421` edge `0.1102` maxDD `-6.2031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
