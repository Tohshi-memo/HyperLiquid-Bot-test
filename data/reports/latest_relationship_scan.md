# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T00:52:29.471778+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8622`

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

- `market_context_high->commodity_24h` score `1.8522` n `92` status `ready` deltaP `15.8696` edge `0.1337` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.5115` n `92` status `ready` deltaP `13.8189` edge `0.4421` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.23` n `59` status `ready` deltaP `15.4459` edge `0.0793` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.23` n `59` status `ready` deltaP `15.4459` edge `0.0793` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `0.6105` n `59` status `ready` deltaP `10.9265` edge `0.2535` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.6105` n `59` status `ready` deltaP `10.9265` edge `0.2535` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.4118` n `92` status `ready` deltaP `4.0484` edge `0.1147` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.3098` n `59` status `ready` deltaP `8.8487` edge `0.0032` maxDD `-0.5766`
- `risk_on_and_context->index_1h` score `0.3098` n `59` status `ready` deltaP `8.8487` edge `0.0032` maxDD `-0.5766`
- `risk_on_high->fx_1h` score `-0.0976` n `59` status `ready` deltaP `3.4865` edge `-0.0006` maxDD `-0.1456`
- `risk_on_and_context->fx_1h` score `-0.0976` n `59` status `ready` deltaP `3.4865` edge `-0.0006` maxDD `-0.1456`
- `market_context_high->index_1h` score `-0.4227` n `92` status `ready` deltaP `3.0454` edge `-0.0017` maxDD `-1.1567`
- `market_context_high->crypto_alt_1h` score `-0.4855` n `92` status `ready` deltaP `0.1432` edge `0.0868` maxDD `-7.3329`
- `market_context_high->fx_1h` score `-0.5083` n `92` status `ready` deltaP `-1.8378` edge `-0.0008` maxDD `-0.503`
- `risk_on_high->fx_4h` score `-0.5657` n `59` status `ready` deltaP `-3.3328` edge `0.0023` maxDD `-0.1781`
- `risk_on_and_context->fx_4h` score `-0.5657` n `59` status `ready` deltaP `-3.3328` edge `0.0023` maxDD `-0.1781`
- `market_context_high->fx_4h` score `-0.6159` n `92` status `ready` deltaP `-2.8354` edge `0.003` maxDD `-0.7115`
- `risk_on_high->equity_1h` score `-0.6538` n `59` status `ready` deltaP `7.9681` edge `-0.0035` maxDD `-4.6617`
- `risk_on_and_context->equity_1h` score `-0.6538` n `59` status `ready` deltaP `7.9681` edge `-0.0035` maxDD `-4.6617`
- `market_context_high->metal_1h` score `-0.7783` n `92` status `ready` deltaP `-2.4798` edge `0.0037` maxDD `-0.9556`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
