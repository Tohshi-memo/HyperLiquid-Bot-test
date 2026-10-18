# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T07:52:31.614011+00:00`
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

- `market_context_high->commodity_24h` score `2.6717` n `116` status `ready` deltaP `18.6741` edge `0.1833` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `2.5026` n `73` status `ready` deltaP `19.3236` edge `0.1595` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `2.5026` n `73` status `ready` deltaP `19.3236` edge `0.1595` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `2.0887` n `145` status `ready` deltaP `17.7166` edge `0.3964` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.7608` n `145` status `ready` deltaP `5.8941` edge `0.113` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.2358` n `145` status `ready` deltaP `7.3271` edge `0.1208` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1877` n `91` status `ready` deltaP `13.609` edge `0.1814` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1877` n `91` status `ready` deltaP `13.609` edge `0.1814` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0521` n `91` status `ready` deltaP `4.2553` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0521` n `91` status `ready` deltaP `4.2553` edge `0.0057` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.326` n `145` status `ready` deltaP `5.4666` edge `0.0087` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.3804` n `145` status `ready` deltaP `5.8393` edge `0.0042` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4548` n `91` status `ready` deltaP `9.2582` edge `0.03` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4548` n `91` status `ready` deltaP `9.2582` edge `0.03` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4852` n `91` status `ready` deltaP `0.9952` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4852` n `91` status `ready` deltaP `0.9952` edge `0.0043` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.4994` n `145` status `ready` deltaP `-1.485` edge `-0.002` maxDD `-0.503`
- `market_context_high->metal_4h` score `-0.6102` n `145` status `ready` deltaP `5.7675` edge `0.0444` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
