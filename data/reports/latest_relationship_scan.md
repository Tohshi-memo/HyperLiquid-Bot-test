# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T03:22:27.068382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6630`

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

- `market_context_high->unknown_1h` score `338.8116` n `50` status `ready` deltaP `9.5269` edge `28.1757` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0055` n `50` status `ready` deltaP `8.9939` edge `23.9405` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.5765` n `73` status `ready` deltaP `38.7534` edge `1.2273` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0627` n `50` status `ready` deltaP `36.1667` edge `0.8224` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.6359` n `50` status `ready` deltaP `15.4931` edge `0.704` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9891` n `50` status `ready` deltaP `17.6951` edge `0.5348` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7681` n `50` status `ready` deltaP `15.5793` edge `0.4228` maxDD `-7.6792`
- `news_risk_high->equity_24h` score `3.6577` n `73` status `ready` deltaP `22.9309` edge `0.457` maxDD `-5.9411`
- `news_risk_high->crypto_alt_4h` score `3.549` n `87` status `ready` deltaP `13.3954` edge `0.3408` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.3669` n `50` status `ready` deltaP `16.9583` edge `0.5048` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `2.916` n `50` status `ready` deltaP `14.1497` edge `0.1937` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8985` n `50` status `ready` deltaP `32.689` edge `0.0371` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8187` n `50` status `ready` deltaP `13.1557` edge `0.2135` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3495` n `87` status `ready` deltaP `22.2736` edge `0.1169` maxDD `-2.9013`
- `news_risk_high->commodity_24h` score `1.4587` n `73` status `ready` deltaP `23.9131` edge `0.14` maxDD `-3.9922`
- `market_context_high->fx_1h` score `1.434` n `50` status `ready` deltaP `20.1916` edge `0.0113` maxDD `-0.113`
- `news_risk_high->crypto_major_24h` score `1.2074` n `73` status `ready` deltaP `10.3311` edge `0.4013` maxDD `-15.8971`
- `news_risk_high->metal_24h` score `1.1862` n `73` status `ready` deltaP `10.752` edge `0.2078` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.0018` n `73` status `ready` deltaP `14.6547` edge `0.0336` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9245` n `50` status `ready` deltaP `14.7917` edge `0.077` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
