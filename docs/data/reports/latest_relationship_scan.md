# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T10:22:30.063460+00:00`
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

- `market_context_high->unknown_4h` score `40.4887` n `90` status `ready` deltaP `-2.7981` edge `3.4466` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.1309` n `59` status `ready` deltaP `38.3242` edge `0.6924` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `8.0887` n `59` status `ready` deltaP `26.0386` edge `0.6052` maxDD `-5.0451`
- `news_risk_high->equity_24h` score `7.6832` n `59` status `ready` deltaP `19.8179` edge `0.5181` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `5.6444` n `90` status `ready` deltaP `14.9741` edge `0.9212` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.3336` n `59` status `ready` deltaP `38.5147` edge `0.1877` maxDD `0.0`
- `market_context_high->equity_24h` score `3.2888` n `90` status `ready` deltaP `17.7087` edge `0.1989` maxDD `-1.0977`
- `news_risk_high->index_4h` score `3.2865` n `59` status `ready` deltaP `35.5622` edge `0.063` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.8787` n `59` status `ready` deltaP `20.3984` edge `0.1637` maxDD `-2.7837`
- `news_risk_high->crypto_major_1h` score `2.8208` n `59` status `ready` deltaP `11.7604` edge `0.1922` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5137` n `90` status `ready` deltaP `16.7988` edge `0.1939` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.4428` n `59` status `ready` deltaP `29.7092` edge `0.0195` maxDD `-0.1194`
- `news_risk_high->metal_4h` score `1.4707` n `59` status `ready` deltaP `21.4551` edge `0.0871` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.4592` n `59` status `ready` deltaP `4.4834` edge `0.1419` maxDD `-2.3482`
- `market_context_high->metal_24h` score `1.2982` n `90` status `ready` deltaP `22.0552` edge `0.1679` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.8588` n `90` status `ready` deltaP `19.3868` edge `0.017` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5981` n `90` status `ready` deltaP `10.5988` edge `0.0034` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.4745` n `90` status `ready` deltaP `9.0962` edge `0.594` maxDD `-34.5048`
- `news_risk_high->equity_1h` score `0.3026` n `59` status `ready` deltaP `4.0825` edge `0.057` maxDD `-0.7197`
- `news_risk_high->metal_1h` score `0.2926` n `59` status `ready` deltaP `9.7711` edge `0.0142` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
