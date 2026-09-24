# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T01:22:34.229199+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.2945` n `47` status `ready` deltaP `11.0142` edge `5.9582` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `35.9278` n `46` status `ready` deltaP `23.0828` edge `2.8557` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.8784` n `46` status `ready` deltaP `20.4786` edge `1.6134` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `20.0216` n `46` status `ready` deltaP `18.0556` edge `1.5481` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `9.314` n `98` status `ready` deltaP `-1.1408` edge `1.4696` maxDD `-46.1999`
- `market_context_high->index_24h` score `7.0176` n `46` status `ready` deltaP `29.5064` edge `0.3968` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `5.0618` n `98` status `ready` deltaP `-3.373` edge `0.9324` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.9201` n `103` status `ready` deltaP `14.5365` edge `0.4129` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.5838` n `103` status `ready` deltaP `17.4328` edge `0.3235` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.6301` n `103` status `ready` deltaP `13.9062` edge `0.1755` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4722` n `47` status `ready` deltaP `29.1483` edge `0.0271` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.3778` n `98` status `ready` deltaP `23.6005` edge `0.1587` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.0505` n `103` status `ready` deltaP `15.8523` edge `0.1087` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.9676` n `46` status `ready` deltaP `23.4828` edge `0.0308` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.6234` n `103` status `ready` deltaP `23.6814` edge `0.041` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.4109` n `47` status `ready` deltaP `11.3518` edge `0.0837` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1311` n `98` status `ready` deltaP `27.9797` edge `0.1216` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.7798` n `47` status `ready` deltaP `12.664` edge `0.0084` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.7399` n `98` status `ready` deltaP `18.8244` edge `0.0721` maxDD `-3.8855`
- `news_risk_high->metal_1h` score `0.6637` n `103` status `ready` deltaP `15.502` edge `0.0113` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
