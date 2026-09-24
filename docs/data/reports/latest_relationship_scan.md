# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T00:52:33.637551+00:00`
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

- `market_context_high->unknown_1h` score `72.2802` n `47` status `ready` deltaP `10.8645` edge `5.958` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `35.6408` n `46` status `ready` deltaP `22.7355` edge `2.8341` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.7198` n `46` status `ready` deltaP `20.1314` edge `1.6025` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `19.6411` n `46` status `ready` deltaP `17.7083` edge `1.5187` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `9.027` n `98` status `ready` deltaP `-1.4881` edge `1.448` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.9694` n `46` status `ready` deltaP `29.1591` edge `0.3951` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.907` n `103` status `ready` deltaP `14.5365` edge `0.4118` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `4.6812` n `98` status `ready` deltaP `-3.7203` edge `0.903` maxDD `-32.7147`
- `news_risk_high->crypto_major_4h` score `4.5874` n `103` status `ready` deltaP `17.4328` edge `0.3238` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.6133` n `103` status `ready` deltaP `13.7565` edge `0.1751` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4722` n `47` status `ready` deltaP `29.1483` edge `0.0271` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.426` n `98` status `ready` deltaP `23.9477` edge `0.1604` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.0313` n `103` status `ready` deltaP `15.7026` edge `0.1081` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.8918` n `46` status `ready` deltaP `23.1356` edge `0.0268` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.6234` n `103` status `ready` deltaP `23.6814` edge `0.041` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.3781` n `47` status `ready` deltaP `11.0469` edge `0.083` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1311` n `98` status `ready` deltaP `27.9797` edge `0.1216` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8061` n `47` status `ready` deltaP `12.9634` edge `0.0086` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6925` n `103` status `ready` deltaP `15.8014` edge `0.0117` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.6907` n `98` status `ready` deltaP `18.4772` edge `0.0681` maxDD `-3.8855`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
