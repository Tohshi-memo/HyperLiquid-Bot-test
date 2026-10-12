# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T02:07:31.316355+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9528`

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

- `market_context_high->unknown_24h` score `868.8726` n `48` status `ready` deltaP `-18.4027` edge `72.5651` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `37.1329` n `113` status `ready` deltaP `-8.3154` edge `3.2204` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.4512` n `48` status `ready` deltaP `31.4236` edge `0.621` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.0143` n `48` status `ready` deltaP `50.5209` edge `0.1687` maxDD `-0.012`
- `risk_on_high->crypto_alt_4h` score `5.0505` n `34` status `ready` deltaP `22.5072` edge `0.3156` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0505` n `34` status `ready` deltaP `22.5072` edge `0.3156` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `5.0486` n `34` status `ready` deltaP `28.4074` edge `0.3166` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.0486` n `34` status `ready` deltaP `28.4074` edge `0.3166` maxDD `-4.1548`
- `market_context_high->crypto_major_24h` score `5.036` n `48` status `ready` deltaP `-7.2916` edge `0.7831` maxDD `-17.8526`
- `risk_on_high->metal_4h` score `3.0641` n `34` status `ready` deltaP `28.1923` edge `0.0906` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.0641` n `34` status `ready` deltaP `28.1923` edge `0.0906` maxDD `-0.1896`
- `risk_on_high->metal_1h` score `1.3794` n `46` status `ready` deltaP `17.0203` edge `0.0254` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.3794` n `46` status `ready` deltaP `17.0203` edge `0.0254` maxDD `-0.2466`
- `market_context_high->fx_24h` score `1.2911` n `48` status `ready` deltaP `18.2291` edge `0.0227` maxDD `-0.2642`
- `risk_on_high->crypto_major_1h` score `1.0078` n `46` status `ready` deltaP `10.2708` edge `0.0808` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.0078` n `46` status `ready` deltaP `10.2708` edge `0.0808` maxDD `-3.2233`
- `market_context_high->unknown_1h` score `0.7732` n `125` status `ready` deltaP `-3.4395` edge `0.121` maxDD `-1.024`
- `risk_on_high->equity_4h` score `0.6843` n `34` status `ready` deltaP `6.2769` edge `0.084` maxDD `-1.0489`
- `risk_on_and_context->equity_4h` score `0.6843` n `34` status `ready` deltaP `6.2769` edge `0.084` maxDD `-1.0489`
- `risk_on_high->crypto_alt_1h` score `0.5563` n `46` status `ready` deltaP `6.9774` edge `0.0845` maxDD `-2.4421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
