# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T19:22:27.213687+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9674`

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

- `risk_on_high->commodity_24h` score `6.99` n `54` status `ready` deltaP `38.8502` edge `0.3235` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.99` n `54` status `ready` deltaP `38.8502` edge `0.3235` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.2739` n `174` status `ready` deltaP `13.7564` edge `0.3438` maxDD `-14.6817`
- `risk_on_high->crypto_major_4h` score `0.6219` n `90` status `ready` deltaP `16.8598` edge `0.2043` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.6219` n `90` status `ready` deltaP `16.8598` edge `0.2043` maxDD `-10.6246`
- `market_context_high->crypto_major_1h` score `0.4669` n `174` status `ready` deltaP `5.2206` edge `0.093` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.0434` n `174` status `ready` deltaP `7.5917` edge `0.103` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0255` n `90` status `ready` deltaP `5.2553` edge `0.0055` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0255` n `90` status `ready` deltaP `5.2553` edge `0.0055` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.2132` n `174` status `ready` deltaP `6.4047` edge `0.0048` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.235` n `90` status `ready` deltaP `1.6216` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.235` n `90` status `ready` deltaP `1.6216` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3237` n `174` status `ready` deltaP `5.6163` edge `0.008` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3845` n `174` status `ready` deltaP `10.0083` edge `0.0377` maxDD `-7.2977`
- `risk_on_high->equity_1h` score `-0.4374` n `90` status `ready` deltaP `9.97` edge `0.0267` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4374` n `90` status `ready` deltaP `9.97` edge `0.0267` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5118` n `90` status `ready` deltaP `0.5589` edge `0.0038` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5118` n `90` status `ready` deltaP `0.5589` edge `0.0038` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5974` n `174` status `ready` deltaP `5.8873` edge `0.0405` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.7219` n `90` status `ready` deltaP `0.0865` edge `-0.0012` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
