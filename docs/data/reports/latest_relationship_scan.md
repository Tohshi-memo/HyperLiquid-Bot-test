# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T14:07:34.956396+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11693`

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

- `risk_on_high->crypto_alt_24h` score `15.4359` n `63` status `ready` deltaP `38.2937` edge `1.2567` maxDD `-14.72`
- `risk_on_and_context->crypto_alt_24h` score `15.4359` n `63` status `ready` deltaP `38.2937` edge `1.2567` maxDD `-14.72`
- `risk_on_high->unknown_4h` score `8.1432` n `107` status `ready` deltaP `25.4032` edge `0.5709` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.1432` n `107` status `ready` deltaP `25.4032` edge `0.5709` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5972` n `159` status `ready` deltaP `22.0998` edge `0.4718` maxDD `-2.5493`
- `market_context_high->crypto_alt_24h` score `3.4166` n `105` status `ready` deltaP `18.9286` edge `0.7308` maxDD `-27.517`
- `risk_on_high->fx_24h` score `3.2837` n `63` status `ready` deltaP `62.8224` edge `0.0463` maxDD `-0.8637`
- `risk_on_and_context->fx_24h` score `3.2837` n `63` status `ready` deltaP `62.8224` edge `0.0463` maxDD `-0.8637`
- `risk_on_high->crypto_major_24h` score `3.0961` n `63` status `ready` deltaP `23.5119` edge `0.6031` maxDD `-24.0331`
- `risk_on_and_context->crypto_major_24h` score `3.0961` n `63` status `ready` deltaP `23.5119` edge `0.6031` maxDD `-24.0331`
- `risk_on_high->unknown_1h` score `2.4442` n `107` status `ready` deltaP `6.8149` edge `0.2159` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4442` n `107` status `ready` deltaP `6.8149` edge `0.2159` maxDD `-1.9453`
- `market_context_high->metal_24h` score `2.2664` n `105` status `ready` deltaP `30.2777` edge `0.2086` maxDD `-3.5914`
- `market_context_high->unknown_1h` score `2.2216` n `159` status `ready` deltaP `6.1566` edge `0.2071` maxDD `-2.041`
- `market_context_high->crypto_major_24h` score `1.891` n `105` status `ready` deltaP `18.75` edge `0.4139` maxDD `-25.1718`
- `news_risk_high->unknown_1h` score `1.5407` n `61` status `ready` deltaP `3.9192` edge `0.1369` maxDD `-1.1043`
- `risk_on_high->metal_24h` score `1.3957` n `63` status `ready` deltaP `29.9603` edge `0.0937` maxDD `-3.4934`
- `risk_on_and_context->metal_24h` score `1.3957` n `63` status `ready` deltaP `29.9603` edge `0.0937` maxDD `-3.4934`
- `market_context_high->fx_24h` score `0.989` n `105` status `ready` deltaP `36.4732` edge `0.0295` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.7236` n `63` status `ready` deltaP `8.8294` edge `0.1327` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
