# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T04:07:30.619341+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->equity_24h` score `1.9361` n `79` status `ready` deltaP `2.8817` edge `1.061` maxDD `-55.843`
- `market_context_high->commodity_24h` score `1.2671` n `79` status `ready` deltaP `14.0165` edge `0.0973` maxDD `-1.8119`
- `market_context_high->crypto_major_24h` score `1.1864` n `79` status `ready` deltaP `4.4392` edge `0.7322` maxDD `-35.1086`
- `risk_on_high->equity_1h` score `0.8272` n `46` status `ready` deltaP `15.5307` edge `0.0253` maxDD `-2.1255`
- `risk_on_and_context->equity_1h` score `0.8272` n `46` status `ready` deltaP `15.5307` edge `0.0253` maxDD `-2.1255`
- `market_context_high->crypto_major_4h` score `0.6606` n `79` status `ready` deltaP `6.4854` edge `0.3819` maxDD `-15.2359`
- `risk_on_high->equity_24h` score `0.5009` n `46` status `ready` deltaP `-15.9131` edge `0.7731` maxDD `-37.6881`
- `risk_on_and_context->equity_24h` score `0.5009` n `46` status `ready` deltaP `-15.9131` edge `0.7731` maxDD `-37.6881`
- `market_context_high->crypto_major_1h` score `0.4585` n `80` status `ready` deltaP `5.2021` edge `0.113` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.4274` n `46` status `ready` deltaP `9.9034` edge `0.0006` maxDD `-0.4804`
- `risk_on_and_context->index_1h` score `0.4274` n `46` status `ready` deltaP `9.9034` edge `0.0006` maxDD `-0.4804`
- `risk_on_high->fx_1h` score `-0.1114` n `46` status `ready` deltaP `3.7472` edge `0.0004` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.1114` n `46` status `ready` deltaP `3.7472` edge `0.0004` maxDD `-0.1065`
- `risk_on_high->equity_4h` score `-0.2442` n `46` status `ready` deltaP `5.0991` edge `0.0993` maxDD `-6.2918`
- `risk_on_and_context->equity_4h` score `-0.2442` n `46` status `ready` deltaP `5.0991` edge `0.0993` maxDD `-6.2918`
- `risk_on_high->fx_4h` score `-0.2682` n `46` status `ready` deltaP `-0.0332` edge `0.0044` maxDD `-0.1223`
- `risk_on_and_context->fx_4h` score `-0.2682` n `46` status `ready` deltaP `-0.0332` edge `0.0044` maxDD `-0.1223`
- `risk_on_high->commodity_24h` score `-0.3112` n `46` status `ready` deltaP `10.5217` edge `-0.0163` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.3112` n `46` status `ready` deltaP `10.5217` edge `-0.0163` maxDD `-1.7154`
- `market_context_high->fx_4h` score `-0.5108` n `79` status `ready` deltaP `-1.0239` edge `0.0044` maxDD `-0.7115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
