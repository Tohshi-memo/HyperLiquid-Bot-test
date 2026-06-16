# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T10:22:37.056647+00:00`
- Price records: `672`
- Market context records: `4082`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10232`

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

- `risk_on_high->unknown_4h` score `144.7513` n `40` status `ready` deltaP `-8.0488` edge `12.2979` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7513` n `40` status `ready` deltaP `-8.0488` edge `12.2979` maxDD `-10.864`
- `market_context_high->unknown_1h` score `49.6319` n `175` status `ready` deltaP `2.2284` edge `4.2789` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.098` n `144` status `ready` deltaP `-9.0663` edge `3.5548` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.7856` n `172` status `ready` deltaP `-2.1767` edge `1.9556` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.6034` n `40` status `ready` deltaP `37.5915` edge `0.0544` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.6034` n `40` status `ready` deltaP `37.5915` edge `0.0544` maxDD `-0.0446`
- `market_context_high->equity_4h` score `1.2282` n `172` status `ready` deltaP `14.5101` edge `0.1587` maxDD `-6.9137`
- `market_context_high->index_24h` score `0.8238` n `144` status `ready` deltaP `16.1179` edge `-0.0388` maxDD `0.0`
- `market_context_high->equity_1h` score `0.5989` n `175` status `ready` deltaP `4.5561` edge `0.0755` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.5763` n `40` status `ready` deltaP `17.622` edge `-0.0029` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.5763` n `40` status `ready` deltaP `17.622` edge `-0.0029` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.4316` n `40` status `ready` deltaP `10.9132` edge `0.0023` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4316` n `40` status `ready` deltaP `10.9132` edge `0.0023` maxDD `-0.7937`
- `risk_on_high->equity_24h` score `0.3022` n `40` status `ready` deltaP `28.4229` edge `-0.1643` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.3022` n `40` status `ready` deltaP `28.4229` edge `-0.1643` maxDD `0.0`
- `risk_on_high->fx_4h` score `0.1919` n `40` status `ready` deltaP `11.9207` edge `0.0042` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1919` n `40` status `ready` deltaP `11.9207` edge `0.0042` maxDD `-0.3925`
- `risk_on_high->metal_4h` score `0.1777` n `40` status `ready` deltaP `11.7073` edge `-0.0217` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1777` n `40` status `ready` deltaP `11.7073` edge `-0.0217` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
