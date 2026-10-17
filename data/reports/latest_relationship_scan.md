# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T18:22:26.001196+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9598`

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

- `risk_on_high->commodity_24h` score `6.9545` n `54` status `ready` deltaP `38.676` edge `0.3217` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9545` n `54` status `ready` deltaP `38.676` edge `0.3217` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.3662` n `173` status `ready` deltaP `13.6278` edge `0.3451` maxDD `-14.4346`
- `risk_on_high->crypto_major_4h` score `0.5871` n `90` status `ready` deltaP `16.4024` edge `0.2029` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.5871` n `90` status `ready` deltaP `16.4024` edge `0.2029` maxDD `-10.6246`
- `market_context_high->crypto_major_1h` score `0.4753` n `174` status `ready` deltaP `5.2206` edge `0.0937` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.0722` n `174` status `ready` deltaP `7.5917` edge `0.1054` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0387` n `90` status `ready` deltaP `5.4054` edge `0.0056` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0387` n `90` status `ready` deltaP `5.4054` edge `0.0056` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.2046` n `174` status `ready` deltaP `6.5548` edge `0.0049` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2428` n `90` status `ready` deltaP `1.4714` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2428` n `90` status `ready` deltaP `1.4714` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3159` n `174` status `ready` deltaP `5.766` edge `0.008` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3791` n `174` status `ready` deltaP `10.0083` edge `0.0384` maxDD `-7.2977`
- `risk_on_high->equity_1h` score `-0.429` n `90` status `ready` deltaP `9.97` edge `0.0274` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.429` n `90` status `ready` deltaP `9.97` edge `0.0274` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.504` n `90` status `ready` deltaP `0.7086` edge `0.0038` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.504` n `90` status `ready` deltaP `0.7086` edge `0.0038` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5703` n `173` status `ready` deltaP `5.5865` edge `0.0406` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.7164` n `90` status `ready` deltaP `0.0865` edge `-0.0005` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
