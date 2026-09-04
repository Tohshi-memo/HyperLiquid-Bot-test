# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T17:52:29.961785+00:00`
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

- `risk_on_high->unknown_4h` score `19.5032` n `133` status `ready` deltaP `7.1692` edge `1.6393` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5032` n `133` status `ready` deltaP `7.1692` edge `1.6393` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.443` n `133` status `ready` deltaP `-2.1015` edge `1.0253` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.443` n `133` status `ready` deltaP `-2.1015` edge `1.0253` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.1756` n `212` status `ready` deltaP `8.9709` edge `0.8577` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.9622` n `215` status `ready` deltaP `-1.0034` edge `0.8166` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `3.3609` n `47` status `ready` deltaP `18.3511` edge `0.1847` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.2097` n `47` status `ready` deltaP `10.1647` edge `0.1647` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.0582` n `47` status `ready` deltaP `13.2314` edge `0.1005` maxDD `-0.042`
- `news_risk_high->commodity_4h` score `1.6148` n `47` status `ready` deltaP `11.8287` edge `0.0758` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.4768` n `47` status `ready` deltaP `14.4063` edge `0.0661` maxDD `-0.7924`
- `news_risk_high->metal_4h` score `1.4134` n `47` status `ready` deltaP `14.725` edge `0.0459` maxDD `-0.7692`
- `news_risk_high->index_1h` score `1.0513` n `47` status `ready` deltaP `13.5622` edge `0.0106` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.4043` n `47` status `ready` deltaP `8.2272` edge `0.0163` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.2947` n `47` status `ready` deltaP `10.3626` edge `0.0007` maxDD `-0.9514`
- `news_risk_high->crypto_alt_1h` score `0.2739` n `47` status `ready` deltaP `4.4847` edge `0.0232` maxDD `-1.0885`
- `news_risk_high->crypto_major_1h` score `0.1239` n `47` status `ready` deltaP `0.6466` edge `0.0408` maxDD `-1.0047`
- `risk_on_high->metal_1h` score `0.107` n `133` status `ready` deltaP `12.5625` edge `0.0012` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.107` n `133` status `ready` deltaP `12.5625` edge `0.0012` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.0523` n `47` status `ready` deltaP `6.9436` edge `0.0027` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
