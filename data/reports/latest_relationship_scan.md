# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T16:52:30.063865+00:00`
- Price records: `672`
- Market context records: `7688`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `2.8701` n `135` status `ready` deltaP `17.5442` edge `0.2564` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `0.897` n `136` status `ready` deltaP `14.123` edge `0.1524` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.7965` n `136` status `ready` deltaP `11.7647` edge `0.0389` maxDD `-2.0766`
- `market_context_high->equity_1h` score `0.5136` n `136` status `ready` deltaP `7.5031` edge `0.0787` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.4902` n `136` status `ready` deltaP `7.0749` edge `0.1054` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.4392` n `136` status `ready` deltaP `2.7298` edge `0.2621` maxDD `-8.5862`
- `market_context_high->index_1h` score `0.2738` n `136` status `ready` deltaP `7.6842` edge `0.0146` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `-0.1307` n `136` status `ready` deltaP `2.5185` edge `0.026` maxDD `-2.2947`
- `market_context_high->fx_24h` score `-0.137` n `135` status `ready` deltaP `10.56` edge `0.0208` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.1857` n `136` status `ready` deltaP `11.6118` edge `0.0446` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.3159` n `136` status `ready` deltaP `2.4863` edge `0.003` maxDD `-0.6722`
- `market_context_high->fx_1h` score `-0.4265` n `136` status `ready` deltaP `0.6161` edge `-0.0009` maxDD `-0.4331`
- `market_context_high->commodity_4h` score `-0.4648` n `136` status `ready` deltaP `1.5335` edge `0.0104` maxDD `-1.0817`
- `market_context_high->metal_1h` score `-0.5717` n `136` status `ready` deltaP `1.2372` edge `0.0188` maxDD `-0.6936`
- `market_context_high->metal_24h` score `-0.8483` n `136` status `ready` deltaP `1.2051` edge `0.1118` maxDD `-2.9535`
- `market_context_high->unknown_1h` score `-1.2997` n `136` status `ready` deltaP `-0.2994` edge `-0.0473` maxDD `-1.054`
- `market_context_high->fx_4h` score `-1.5494` n `136` status `ready` deltaP `-4.8547` edge `-0.0033` maxDD `-1.7046`
- `market_context_high->commodity_24h` score `-1.5666` n `135` status `ready` deltaP `6.0898` edge `-0.0128` maxDD `-7.0012`
- `market_context_high->metal_4h` score `-1.6431` n `136` status `ready` deltaP `0.7891` edge `0.0706` maxDD `-2.0226`
- `market_context_high->unknown_4h` score `-2.7355` n `136` status `ready` deltaP `13.9257` edge `-0.1748` maxDD `-2.3464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
