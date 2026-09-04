# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T20:22:26.313047+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10796`

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

- `risk_on_high->unknown_4h` score `19.6998` n `133` status `ready` deltaP `7.9314` edge `1.6506` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.6998` n `133` status `ready` deltaP `7.9314` edge `1.6506` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.2942` n `133` status `ready` deltaP `-2.1015` edge `1.0129` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.2942` n `133` status `ready` deltaP `-2.1015` edge `1.0129` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.6934` n `215` status `ready` deltaP `9.0925` edge `0.8167` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.5157` n `217` status `ready` deltaP `-1.1556` edge `0.7804` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `3.9609` n `46` status `ready` deltaP `19.6709` edge `0.2259` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.2153` n `46` status `ready` deltaP `9.4247` edge `0.1701` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.0566` n `46` status `ready` deltaP `12.3868` edge `0.106` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.6521` n `46` status `ready` deltaP `17.3184` edge `0.0485` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6471` n `46` status `ready` deltaP `15.9789` edge `0.0698` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.4937` n `46` status `ready` deltaP `10.4189` edge `0.0751` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1205` n `46` status `ready` deltaP `14.3973` edge `0.0108` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7017` n `46` status `ready` deltaP `9.0732` edge `0.0173` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.2799` n `46` status `ready` deltaP `10.2532` edge `0.0002` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.2113` n `46` status `ready` deltaP `8.7803` edge `0.0037` maxDD `-0.9036`
- `news_risk_high->crypto_alt_1h` score `0.1604` n `46` status `ready` deltaP `3.7556` edge `0.0186` maxDD `-1.0885`
- `risk_on_high->metal_1h` score `0.0805` n `133` status `ready` deltaP `12.1134` edge `0.0008` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0805` n `133` status `ready` deltaP `12.1134` edge `0.0008` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.0663` n `46` status `ready` deltaP `-0.371` edge `0.0402` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
