# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T19:22:29.031386+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `risk_on_high->unknown_4h` score `7.8634` n `107` status `ready` deltaP `23.7264` edge `0.5588` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.8634` n `107` status `ready` deltaP `23.7264` edge `0.5588` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3162` n `159` status `ready` deltaP `20.423` edge `0.4596` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.4678` n `107` status `ready` deltaP `6.8149` edge `0.2179` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.4678` n `107` status `ready` deltaP `6.8149` edge `0.2179` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.244` n `159` status `ready` deltaP `6.1566` edge `0.209` maxDD `-2.0436`
- `risk_on_high->crypto_alt_24h` score `2.0984` n `83` status `ready` deltaP `18.0221` edge `0.7557` maxDD `-38.5459`
- `risk_on_and_context->crypto_alt_24h` score `2.0984` n `83` status `ready` deltaP `18.0221` edge `0.7557` maxDD `-38.5459`
- `risk_on_high->commodity_24h` score `2.0311` n `83` status `ready` deltaP `13.5982` edge `0.1774` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `2.0311` n `83` status `ready` deltaP `13.5982` edge `0.1774` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.5622` n `61` status `ready` deltaP `3.9192` edge `0.1387` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `1.3974` n `83` status `ready` deltaP `45.4318` edge `0.0272` maxDD `-2.7403`
- `risk_on_and_context->fx_24h` score `1.3974` n `83` status `ready` deltaP `45.4318` edge `0.0272` maxDD `-2.7403`
- `market_context_high->fx_24h` score `0.6318` n `126` status `ready` deltaP `29.9604` edge `0.0205` maxDD `-3.4066`
- `news_risk_high->commodity_4h` score `0.2581` n `61` status `ready` deltaP `7.492` edge `0.0248` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.2366` n `159` status `ready` deltaP `9.9292` edge `0.0185` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1585` n `61` status `ready` deltaP `10.8057` edge `0.0005` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `0.0387` n `107` status `ready` deltaP `6.2203` edge `0.0157` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0387` n `107` status `ready` deltaP `6.2203` edge `0.0157` maxDD `-0.8428`
- `news_risk_high->commodity_24h` score `0.0319` n `44` status `ready` deltaP `3.7406` edge `0.0107` maxDD `-1.1904`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
