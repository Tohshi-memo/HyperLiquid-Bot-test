# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T07:22:31.156453+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10438`

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

- `risk_on_high->commodity_24h` score `2.6012` n `71` status `ready` deltaP `19.1319` edge `0.169` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `2.6012` n `71` status `ready` deltaP `19.1319` edge `0.169` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `2.4873` n `116` status `ready` deltaP `17.2985` edge `0.1771` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `2.0429` n `147` status `ready` deltaP `17.909` edge `0.3913` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.7666` n `147` status `ready` deltaP `6.1764` edge `0.1116` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.2034` n `147` status `ready` deltaP `7.1164` edge `0.1195` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1554` n `91` status `ready` deltaP `13.3041` edge `0.1793` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1554` n `91` status `ready` deltaP `13.3041` edge `0.1793` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0401` n `91` status `ready` deltaP `4.4055` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0401` n `91` status `ready` deltaP `4.4055` edge `0.0057` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.3683` n `147` status `ready` deltaP `5.9754` edge `0.0043` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4668` n `91` status `ready` deltaP `9.1081` edge `0.03` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4668` n `91` status `ready` deltaP `9.1081` edge `0.03` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.493` n `91` status `ready` deltaP `0.8455` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.493` n `91` status `ready` deltaP `0.8455` edge `0.0043` maxDD `-0.8513`
- `market_context_high->metal_1h` score `-0.5155` n `147` status `ready` deltaP `5.2935` edge `0.0087` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.5254` n `147` status `ready` deltaP `-2.001` edge `-0.0019` maxDD `-0.503`
- `market_context_high->equity_1h` score `-0.6396` n `147` status `ready` deltaP `9.579` edge `0.0368` maxDD `-7.3168`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
