# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T00:52:31.921623+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.5596` n `90` status `ready` deltaP `-4.3224` edge `3.296` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8943` n `62` status `ready` deltaP `38.277` edge `0.673` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.9577` n `62` status `ready` deltaP `22.1725` edge `0.5664` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.7052` n `62` status `ready` deltaP `13.9636` edge `0.3923` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.6273` n `62` status `ready` deltaP `33.391` edge `0.163` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.0934` n `90` status `ready` deltaP `10.0461` edge `0.7552` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8632` n `62` status `ready` deltaP `31.5451` edge `0.0545` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4647` n `62` status `ready` deltaP `10.1748` edge `0.1731` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3895` n `90` status `ready` deltaP `16.3415` edge `0.1866` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0478` n `62` status `ready` deltaP `17.1666` edge `0.116` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9409` n `62` status `ready` deltaP `24.4254` edge `0.0139` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4817` n `62` status `ready` deltaP `21.0956` edge `0.0909` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.3392` n `62` status `ready` deltaP `-7.2974` edge `0.2848` maxDD `-5.6309`
- `market_context_high->equity_24h` score `1.2006` n `90` status `ready` deltaP `11.5263` edge `0.0661` maxDD `-1.0977`
- `market_context_high->metal_24h` score `1.1308` n `90` status `ready` deltaP `20.0807` edge `0.1596` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0603` n `62` status `ready` deltaP `2.7091` edge `0.1222` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.9903` n `90` status `ready` deltaP `20.9112` edge `0.0178` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6951` n `90` status `ready` deltaP `11.7964` edge `0.0035` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.137` n `90` status `ready` deltaP `10.1031` edge `0.0391` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.0898` n `62` status `ready` deltaP `6.1522` edge `0.0083` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
