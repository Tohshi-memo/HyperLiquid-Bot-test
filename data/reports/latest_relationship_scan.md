# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T00:16:11.178821+00:00`
- Price records: `672`
- Market context records: `4040`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.6471` n `40` status `ready` deltaP `-7.5915` edge `12.3695` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.6471` n `40` status `ready` deltaP `-7.5915` edge `12.3695` maxDD `-10.864`
- `market_context_high->unknown_24h` score `46.5968` n `134` status `ready` deltaP `-7.5856` edge `4.3365` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `22.9331` n `156` status `ready` deltaP `2.2162` edge `2.4386` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.554` n `40` status `ready` deltaP `35.3553` edge `0.1438` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.554` n `40` status `ready` deltaP `35.3553` edge `0.1438` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.3095` n `40` status `ready` deltaP `36.6768` edge `0.036` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.3095` n `40` status `ready` deltaP `36.6768` edge `0.036` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.5379` n `134` status `ready` deltaP `22.304` edge `0.084` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.5897` n `156` status `ready` deltaP `15.4589` edge `0.1575` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.3317` n `134` status `ready` deltaP `10.6612` edge `0.1386` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.048` n `161` status `ready` deltaP `7.7101` edge `0.0919` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.8981` n `40` status `ready` deltaP `18.689` edge `0.0168` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.8981` n `40` status `ready` deltaP `18.689` edge `0.0168` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.4026` n `40` status `ready` deltaP `1.9497` edge `0.2487` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.4026` n `40` status `ready` deltaP `1.9497` edge `0.2487` maxDD `-12.9187`
- `market_context_high->metal_1h` score `0.3652` n `161` status `ready` deltaP `9.5827` edge `0.0455` maxDD `-3.0049`
- `risk_on_high->equity_1h` score `0.356` n `40` status `ready` deltaP `10.6138` edge `-0.002` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.356` n `40` status `ready` deltaP `10.6138` edge `-0.002` maxDD `-0.7937`
- `market_context_high->crypto_major_1h` score `0.2789` n `161` status `ready` deltaP `7.2321` edge `0.0472` maxDD `-3.7739`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
