# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T00:07:40.826423+00:00`
- Price records: `672`
- Market context records: `4039`
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

- `risk_on_high->unknown_4h` score `145.6701` n `40` status `ready` deltaP `-7.439` edge `12.3704` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.6701` n `40` status `ready` deltaP `-7.439` edge `12.3704` maxDD `-10.864`
- `market_context_high->unknown_24h` score `46.6503` n `134` status `ready` deltaP `-7.4123` edge `4.3398` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `22.9561` n `156` status `ready` deltaP `2.3687` edge `2.4395` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.6423` n `40` status `ready` deltaP `35.5286` edge `0.15` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.6423` n `40` status `ready` deltaP `35.5286` edge `0.15` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2853` n `40` status `ready` deltaP `36.5244` edge `0.035` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2853` n `40` status `ready` deltaP `36.5244` edge `0.035` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.5853` n `134` status `ready` deltaP `22.4773` edge `0.0868` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.5655` n `156` status `ready` deltaP `15.3065` edge `0.1565` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.3677` n `134` status `ready` deltaP `10.6612` edge `0.1416` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.0603` n `160` status `ready` deltaP `7.6385` edge `0.0934` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.9041` n `40` status `ready` deltaP `18.689` edge `0.0173` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9041` n `40` status `ready` deltaP `18.689` edge `0.0173` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.444` n `40` status `ready` deltaP `2.1231` edge `0.251` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.444` n `40` status `ready` deltaP `2.1231` edge `0.251` maxDD `-12.9187`
- `market_context_high->metal_1h` score `0.3928` n `160` status `ready` deltaP `9.9476` edge `0.0466` maxDD `-3.0049`
- `risk_on_high->equity_1h` score `0.3776` n `40` status `ready` deltaP `10.7635` edge `-0.0012` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.3776` n `40` status `ready` deltaP `10.7635` edge `-0.0012` maxDD `-0.7937`
- `market_context_high->crypto_major_1h` score `0.2743` n `160` status `ready` deltaP `7.1295` edge `0.0475` maxDD `-3.7739`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
