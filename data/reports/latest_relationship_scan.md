# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T18:52:33.201837+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10804`

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

- `risk_on_high->unknown_4h` score `19.5716` n `133` status `ready` deltaP `7.1692` edge `1.645` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5716` n `133` status `ready` deltaP `7.1692` edge `1.645` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.5293` n `133` status `ready` deltaP `-1.8021` edge `1.0305` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.5293` n `133` status `ready` deltaP `-1.8021` edge `1.0305` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.244` n `212` status `ready` deltaP `8.9709` edge `0.8634` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.9266` n `216` status `ready` deltaP `-0.5489` edge `0.8106` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `3.5548` n `46` status `ready` deltaP `18.6292` edge `0.199` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.1913` n `46` status `ready` deltaP `9.4247` edge `0.1681` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.1091` n `46` status `ready` deltaP `12.9076` edge `0.1069` maxDD `-0.042`
- `news_risk_high->equity_1h` score `1.671` n `46` status `ready` deltaP `16.1286` edge `0.0708` maxDD `-0.7924`
- `news_risk_high->metal_4h` score `1.5669` n `46` status `ready` deltaP `16.4037` edge `0.0475` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.563` n `46` status `ready` deltaP `11.1811` edge `0.0758` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.172` n `46` status `ready` deltaP `14.9961` edge `0.0111` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7448` n `46` status `ready` deltaP `9.5223` edge `0.0179` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.3323` n `46` status `ready` deltaP `10.8629` edge `0.0005` maxDD `-0.9514`
- `news_risk_high->crypto_alt_1h` score `0.1711` n `46` status `ready` deltaP `3.9053` edge `0.0185` maxDD `-1.0885`
- `news_risk_high->commodity_1h` score `0.155` n `46` status `ready` deltaP `8.1815` edge `0.003` maxDD `-0.9036`
- `risk_on_high->metal_1h` score `0.1085` n `133` status `ready` deltaP `12.5625` edge `0.0014` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1085` n `133` status `ready` deltaP `12.5625` edge `0.0014` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.0788` n `46` status `ready` deltaP `-0.2213` edge `0.0408` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
