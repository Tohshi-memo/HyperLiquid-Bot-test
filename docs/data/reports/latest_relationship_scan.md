# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T07:37:26.068148+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10450`

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

- `market_context_high->commodity_24h` score `2.5747` n `116` status `ready` deltaP `17.9863` edge `0.1798` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `2.554` n `72` status `ready` deltaP `19.2316` edge `0.1644` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `2.554` n `72` status `ready` deltaP `19.2316` edge `0.1644` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `2.0642` n `146` status `ready` deltaP `17.8145` edge `0.3937` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.7663` n `146` status `ready` deltaP `6.0372` edge `0.1125` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.2488` n `146` status `ready` deltaP `7.4891` edge `0.1208` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1704` n `91` status `ready` deltaP `13.4566` edge `0.1802` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1704` n `91` status `ready` deltaP `13.4566` edge `0.1802` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0521` n `91` status `ready` deltaP `4.2553` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0521` n `91` status `ready` deltaP `4.2553` edge `0.0057` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3445` n `146` status `ready` deltaP `5.1124` edge `0.0087` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.3523` n `146` status `ready` deltaP `6.1747` edge `0.0043` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4548` n `91` status `ready` deltaP `9.2582` edge `0.03` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4548` n `91` status `ready` deltaP `9.2582` edge `0.03` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4852` n `91` status `ready` deltaP `0.9952` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4852` n `91` status `ready` deltaP `0.9952` edge `0.0043` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5082` n `146` status `ready` deltaP `-1.6702` edge `-0.0019` maxDD `-0.503`
- `market_context_high->metal_4h` score `-0.6413` n `146` status `ready` deltaP `5.4085` edge `0.0442` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
