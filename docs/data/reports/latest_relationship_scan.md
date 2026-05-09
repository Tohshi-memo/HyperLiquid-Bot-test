# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T03:37:13.071670+00:00`
- Price records: `672`
- Market context records: `825`
- Flow alert records: `2317`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `12.1483` n `148` status `ready` deltaP `30.0676` edge `0.8453` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `4.8009` n `148` status `ready` deltaP `7.1368` edge `0.3573` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4348` n `33` status `ready` deltaP `9.4281` edge `0.2599` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4348` n `33` status `ready` deltaP `9.4281` edge `0.2599` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.6832` n `33` status `ready` deltaP `15.9461` edge `0.1261` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.6832` n `33` status `ready` deltaP `15.9461` edge `0.1261` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.4701` n `33` status `ready` deltaP `18.4405` edge `0.1201` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.4701` n `33` status `ready` deltaP `18.4405` edge `0.1201` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.1382` n `33` status `ready` deltaP `18.653` edge `0.0743` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.1382` n `33` status `ready` deltaP `18.653` edge `0.0743` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0596` n `33` status `ready` deltaP `12.5114` edge `0.0279` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0596` n `33` status `ready` deltaP `12.5114` edge `0.0279` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8727` n `33` status `ready` deltaP `5.8204` edge `0.1562` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8727` n `33` status `ready` deltaP `5.8204` edge `0.1562` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3569` n `33` status `ready` deltaP `9.0365` edge `0.0231` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3569` n `33` status `ready` deltaP `9.0365` edge `0.0231` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2789` n `33` status `ready` deltaP `8.5466` edge `0.0023` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2789` n `33` status `ready` deltaP `8.5466` edge `0.0023` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1853` n `33` status `ready` deltaP `4.1327` edge `-0.0209` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.1853` n `33` status `ready` deltaP `4.1327` edge `-0.0209` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
