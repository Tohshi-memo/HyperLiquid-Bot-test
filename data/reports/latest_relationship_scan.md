# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T20:37:36.854227+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10802`

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

- `risk_on_high->unknown_4h` score `19.7275` n `133` status `ready` deltaP `8.0838` edge `1.6519` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.7275` n `133` status `ready` deltaP `8.0838` edge `1.6519` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.317` n `133` status `ready` deltaP `-1.9518` edge `1.0138` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.317` n `133` status `ready` deltaP `-1.9518` edge `1.0138` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.7211` n `215` status `ready` deltaP `9.2449` edge `0.818` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.5384` n `217` status `ready` deltaP `-1.0059` edge `0.7813` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `4.0216` n `46` status `ready` deltaP `19.8445` edge `0.2298` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.2371` n `46` status `ready` deltaP `9.5772` edge `0.1709` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `2.0416` n `46` status `ready` deltaP `12.2132` edge `0.1059` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.6655` n `46` status `ready` deltaP `17.4708` edge `0.0486` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6327` n `46` status `ready` deltaP `15.8292` edge `0.0696` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.4791` n `46` status `ready` deltaP `10.2664` edge `0.0749` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1193` n `46` status `ready` deltaP `14.3973` edge `0.0107` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7017` n `46` status `ready` deltaP `9.0732` edge `0.0173` maxDD `-0.2118`
- `news_risk_high->fx_4h` score `0.2799` n `46` status `ready` deltaP `10.2532` edge `0.0002` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.2257` n `46` status `ready` deltaP `8.93` edge `0.0039` maxDD `-0.9036`
- `news_risk_high->crypto_alt_1h` score `0.1759` n `46` status `ready` deltaP `3.9053` edge `0.0189` maxDD `-1.0885`
- `risk_on_high->metal_1h` score `0.0805` n `133` status `ready` deltaP `12.1134` edge `0.0008` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0805` n `133` status `ready` deltaP `12.1134` edge `0.0008` maxDD `-1.699`
- `news_risk_high->crypto_major_1h` score `0.0686` n `46` status `ready` deltaP `-0.371` edge `0.0405` maxDD `-1.0047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
