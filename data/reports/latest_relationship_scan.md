# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T03:07:27.047145+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7535`

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

- `market_context_high->unknown_24h` score `7438.2151` n `48` status `ready` deltaP `1.3889` edge `619.842` maxDD `0.0`
- `market_context_high->unknown_4h` score `416.071` n `48` status `ready` deltaP `7.2155` edge `34.6288` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `40.382` n `53` status `ready` deltaP `4.0984` edge `3.3489` maxDD `-0.2178`
- `market_context_high->equity_24h` score `20.0348` n `48` status `ready` deltaP `42.5348` edge `1.4096` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.7299` n `94` status `ready` deltaP `33.566` edge `1.056` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.6144` n `48` status `ready` deltaP `45.3125` edge `0.2802` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.2634` n `48` status `ready` deltaP `49.1319` edge `0.1944` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.0745` n `48` status `ready` deltaP `24.6951` edge `0.371` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.1757` n `48` status `ready` deltaP `29.6748` edge `0.2671` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `3.9116` n `48` status `ready` deltaP `36.5854` edge `0.0988` maxDD `-0.3387`
- `market_context_high->equity_4h` score `2.8108` n `48` status `ready` deltaP `0.9655` edge `0.298` maxDD `-2.283`
- `news_risk_high->crypto_alt_4h` score `2.2918` n `126` status `ready` deltaP `9.3181` edge `0.2675` maxDD `-7.4246`
- `market_context_high->equity_1h` score `2.2621` n `53` status `ready` deltaP `8.0415` edge `0.1874` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.7102` n `53` status `ready` deltaP `7.8918` edge `0.1408` maxDD `-1.4048`
- `market_context_high->crypto_alt_1h` score `1.6406` n `53` status `ready` deltaP `4.8667` edge `0.1655` maxDD `-2.2314`
- `market_context_high->crypto_major_24h` score `1.5434` n `48` status `ready` deltaP `5.5555` edge `0.2285` maxDD `-3.0799`
- `market_context_high->fx_1h` score `1.4064` n `53` status `ready` deltaP `18.9131` edge `0.0087` maxDD `-0.0736`
- `market_context_high->crypto_alt_24h` score `1.3399` n `48` status `ready` deltaP `-8.8542` edge `0.3826` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.2759` n `48` status `ready` deltaP `15.7521` edge `0.0438` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.4309` n `53` status `ready` deltaP `7.0218` edge `0.0148` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
