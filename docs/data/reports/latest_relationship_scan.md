# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T14:07:26.587424+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `market_context_high->commodity_24h` score `2.2173` n `131` status `ready` deltaP `19.443` edge `0.1403` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.854` n `90` status `ready` deltaP `20.6813` edge `0.0964` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.854` n `90` status `ready` deltaP `20.6813` edge `0.0964` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `1.6529` n `135` status `ready` deltaP `16.2285` edge `0.37` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.868` n `135` status `ready` deltaP `6.2885` edge `0.1193` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.4312` n `91` status `ready` deltaP `14.8285` edge `0.2045` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.4312` n `91` status `ready` deltaP `14.8285` edge `0.2045` maxDD `-11.1788`
- `risk_on_high->index_1h` score `0.0344` n `91` status `ready` deltaP `5.3064` edge `0.0059` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0344` n `91` status `ready` deltaP `5.3064` edge `0.0059` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.0556` n `135` status `ready` deltaP `4.5542` edge `0.1125` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.3899` n `91` status `ready` deltaP `9.8588` edge `0.0314` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.3899` n `91` status `ready` deltaP `9.8588` edge `0.0314` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.435` n `135` status `ready` deltaP `3.3721` edge `0.0087` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.4739` n `135` status `ready` deltaP `4.7448` edge `0.0037` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.4852` n `91` status `ready` deltaP `0.9952` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4852` n `91` status `ready` deltaP `0.9952` edge `0.0043` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.6969` n `135` status `ready` deltaP `4.6387` edge `0.0447` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.7502` n `91` status `ready` deltaP `-1.298` edge `0.0044` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
