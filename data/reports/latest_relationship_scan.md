# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T07:07:26.314506+00:00`
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

- `risk_on_high->commodity_24h` score `2.6502` n `70` status `ready` deltaP `19.0244` edge `0.1738` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `2.6502` n `70` status `ready` deltaP `19.0244` edge `0.1738` maxDD `-1.7154`
- `market_context_high->commodity_24h` score `2.3975` n `116` status `ready` deltaP `16.6106` edge `0.1742` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.9712` n `148` status `ready` deltaP `17.4769` edge `0.3882` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.7305` n `148` status `ready` deltaP `5.9354` edge `0.1102` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.1631` n `148` status `ready` deltaP `6.8984` edge `0.1176` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1546` n `91` status `ready` deltaP `13.3041` edge `0.1792` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1546` n `91` status `ready` deltaP `13.3041` edge `0.1792` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0269` n `91` status `ready` deltaP `4.5556` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0269` n `91` status `ready` deltaP `4.5556` edge `0.0058` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.3827` n `148` status `ready` deltaP `5.7808` edge `0.0044` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4524` n `91` status `ready` deltaP `9.2582` edge `0.0302` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4524` n `91` status `ready` deltaP `9.2582` edge `0.0302` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.4894` n `148` status `ready` deltaP `5.6198` edge `0.0087` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.493` n `91` status `ready` deltaP `0.8455` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.493` n `91` status `ready` deltaP `0.8455` edge `0.0043` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5151` n `148` status `ready` deltaP `-1.8019` edge `-0.0019` maxDD `-0.503`
- `market_context_high->equity_1h` score `-0.6528` n `148` status `ready` deltaP `9.3844` edge `0.037` maxDD `-7.3168`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
