# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T08:07:38.194714+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9897`

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

- `market_context_high->unknown_1h` score `66.1254` n `47` status `ready` deltaP `10.5651` edge `5.4471` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `40.3912` n `46` status `ready` deltaP `27.7703` edge `3.1964` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `25.5002` n `46` status `ready` deltaP `22.7431` edge `1.9734` maxDD `0.0`
- `market_context_high->equity_24h` score `23.4038` n `46` status `ready` deltaP `25.1661` edge `1.7926` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.761` n `46` status `ready` deltaP `34.1939` edge `0.4275` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `6.65` n `103` status `ready` deltaP `0.0793` edge `1.4579` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.7434` n `103` status `ready` deltaP `14.2316` edge `0.4002` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.653` n `103` status `ready` deltaP `18.0426` edge `0.3252` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `3.2381` n `103` status `ready` deltaP `-2.4996` edge `0.9878` maxDD `-49.7699`
- `market_context_high->metal_24h` score `2.9726` n `46` status `ready` deltaP `28.1703` edge `0.0833` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.7969` n `47` status `ready` deltaP `32.5019` edge `0.0318` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.3434` n `114` status `ready` deltaP `12.9478` edge `0.158` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.082` n `47` status `ready` deltaP `15.3152` edge `0.1132` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.9678` n `114` status `ready` deltaP `15.0436` edge `0.1072` maxDD `-1.8141`
- `news_risk_high->commodity_24h` score `1.8195` n `103` status `ready` deltaP `20.1018` edge `0.1355` maxDD `-2.431`
- `news_risk_high->fx_4h` score `1.616` n `103` status `ready` deltaP `23.5289` edge `0.0414` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2723` n `103` status `ready` deltaP `30.1847` edge `0.125` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8744` n `47` status `ready` deltaP `13.7119` edge `0.0093` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.7868` n `47` status `ready` deltaP `10.2688` edge `0.0374` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.6216` n `114` status `ready` deltaP `14.8256` edge `0.0123` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
