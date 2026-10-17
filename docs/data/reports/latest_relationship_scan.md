# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T22:22:29.970433+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9622`

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

- `risk_on_high->commodity_24h` score `7.0688` n `54` status `ready` deltaP `39.0244` edge `0.3289` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0688` n `54` status `ready` deltaP `39.0244` edge `0.3289` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.1055` n `174` status `ready` deltaP `12.5368` edge `0.3379` maxDD `-14.6817`
- `market_context_high->crypto_major_1h` score `0.5372` n `175` status `ready` deltaP `5.1839` edge `0.0991` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.5124` n `90` status `ready` deltaP `15.6402` edge `0.1984` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.5124` n `90` status `ready` deltaP `15.6402` edge `0.1984` maxDD `-10.6246`
- `market_context_high->crypto_alt_1h` score `0.1925` n `175` status `ready` deltaP `8.0008` edge `0.1127` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0644` n `91` status `ready` deltaP `5.6067` edge `0.0064` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0644` n `91` status `ready` deltaP `5.6067` edge `0.0064` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1737` n `175` status `ready` deltaP `7.0133` edge `0.0058` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2572` n `175` status `ready` deltaP `6.7904` edge `0.0087` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `market_context_high->equity_1h` score `-0.2877` n `175` status `ready` deltaP `10.767` edge `0.0453` maxDD `-7.3168`
- `risk_on_high->equity_1h` score `-0.3059` n `91` status `ready` deltaP `10.4594` edge `0.0344` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.3059` n `91` status `ready` deltaP `10.4594` edge `0.0344` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4284` n `91` status `ready` deltaP `2.0431` edge `0.0046` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4284` n `91` status `ready` deltaP `2.0431` edge `0.0046` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5305` n `174` status `ready` deltaP `6.6495` edge `0.041` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.6427` n `91` status `ready` deltaP `0.3487` edge `0.0072` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
