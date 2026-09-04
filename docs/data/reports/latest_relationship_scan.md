# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T21:22:29.522029+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10632`

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

- `risk_on_high->unknown_4h` score `19.8061` n `133` status `ready` deltaP `8.5412` edge `1.6554` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.8061` n `133` status `ready` deltaP `8.5412` edge `1.6554` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `10.6077` n `133` status `ready` deltaP `-1.8021` edge `0.9537` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `10.6077` n `133` status `ready` deltaP `-1.8021` edge `0.9537` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.7997` n `215` status `ready` deltaP `9.7023` edge `0.8215` maxDD `-2.563`
- `market_context_high->unknown_1h` score `7.8292` n `217` status `ready` deltaP `-0.8562` edge `0.7212` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `4.2061` n `46` status `ready` deltaP `20.3654` edge `0.2417` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.2819` n `46` status `ready` deltaP `9.882` edge `0.1726` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `1.9963` n `46` status `ready` deltaP `11.6923` edge `0.1056` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.6923` n `46` status `ready` deltaP `17.7757` edge `0.0488` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6207` n `46` status `ready` deltaP `15.6795` edge `0.0696` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.4523` n `46` status `ready` deltaP `9.9615` edge `0.0747` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1205` n `46` status `ready` deltaP `14.3973` edge `0.0108` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.74` n `46` status `ready` deltaP `9.5223` edge `0.0175` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.2933` n `46` status `ready` deltaP `10.4056` edge `0.0003` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.2376` n `46` status `ready` deltaP `9.0797` edge `0.0039` maxDD `-0.9036`
- `news_risk_high->crypto_alt_1h` score `0.1568` n `46` status `ready` deltaP `3.7556` edge `0.0183` maxDD `-1.0885`
- `risk_on_high->metal_1h` score `0.1054` n `133` status `ready` deltaP `12.5625` edge `0.001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1054` n `133` status `ready` deltaP `12.5625` edge `0.001` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.0757` n `46` status `ready` deltaP `-0.2213` edge `0.0404` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
