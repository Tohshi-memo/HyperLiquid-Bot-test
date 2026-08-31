# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T06:52:23.159973+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11586`

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

- `risk_on_high->crypto_alt_24h` score `21.8392` n `55` status `ready` deltaP `48.4469` edge `1.545` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.8392` n `55` status `ready` deltaP `48.4469` edge `1.545` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `10.1224` n `55` status `ready` deltaP `29.7349` edge `0.7871` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `10.1224` n `55` status `ready` deltaP `29.7349` edge `0.7871` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.2207` n `104` status `ready` deltaP `24.9179` edge `0.5806` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.2207` n `104` status `ready` deltaP `24.9179` edge `0.5806` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5938` n `156` status `ready` deltaP `21.7128` edge `0.4741` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.343` n `55` status `ready` deltaP `71.0069` edge `0.0552` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.343` n `55` status `ready` deltaP `71.0069` edge `0.0552` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2396` n `96` status `ready` deltaP `37.1527` edge `0.2498` maxDD `-1.8678`
- `market_context_high->crypto_alt_24h` score `4.4851` n `96` status `ready` deltaP `22.9166` edge `0.8412` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.42` n `55` status `ready` deltaP `40.5808` edge `0.145` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.42` n `55` status `ready` deltaP `40.5808` edge `0.145` maxDD `-0.7767`
- `market_context_high->crypto_major_24h` score `4.1832` n `96` status `ready` deltaP `20.8334` edge `0.4588` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.5737` n `107` status `ready` deltaP `7.264` edge `0.2237` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.5737` n `107` status `ready` deltaP `7.264` edge `0.2237` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.3511` n `159` status `ready` deltaP `6.6057` edge `0.2149` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0655` n `96` status `ready` deltaP `37.6736` edge `0.0313` maxDD `-1.6688`
- `risk_on_high->equity_24h` score `0.8744` n `55` status `ready` deltaP `19.2361` edge `0.0254` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `0.8744` n `55` status `ready` deltaP `19.2361` edge `0.0254` maxDD `-3.7955`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
