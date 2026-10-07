# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T20:52:33.967707+00:00`
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

- `market_context_high->unknown_4h` score `38.1862` n `90` status `ready` deltaP `-5.3895` edge `3.272` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8495` n `62` status `ready` deltaP `37.9721` edge `0.6713` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0299` n `62` status `ready` deltaP `22.325` edge `0.5714` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.699` n `62` status `ready` deltaP `11.1955` edge `0.3269` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.2678` n `62` status `ready` deltaP `30.6228` edge `0.1515` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.3234` n `90` status `ready` deltaP `9.008` edge `0.6634` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8354` n `62` status `ready` deltaP `31.3926` edge `0.0532` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4432` n `62` status `ready` deltaP `10.0251` edge `0.1723` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3447` n `90` status `ready` deltaP `16.0366` edge `0.1849` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0688` n `62` status `ready` deltaP `17.624` edge `0.1147` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9756` n `62` status `ready` deltaP `24.8745` edge `0.0138` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4832` n `62` status `ready` deltaP `21.0956` edge `0.0911` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.1262` n `62` status `ready` deltaP `3.1582` edge `0.1247` maxDD `-2.4854`
- `market_context_high->metal_24h` score `0.9685` n `90` status `ready` deltaP `19.7347` edge `0.1411` maxDD `-3.5466`
- `news_risk_high->unknown_4h` score `0.9658` n `62` status `ready` deltaP `-8.3645` edge `0.2608` maxDD `-5.6309`
- `market_context_high->fx_4h` score `0.9224` n `90` status `ready` deltaP `20.3015` edge `0.0162` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6663` n `90` status `ready` deltaP `11.497` edge `0.0031` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.1944` n `90` status `ready` deltaP `8.7582` edge `0.0007` maxDD `-1.0977`
- `news_risk_high->metal_1h` score `0.1257` n `62` status `ready` deltaP `6.6013` edge `0.0083` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.123` n `90` status `ready` deltaP `9.9534` edge `0.0383` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
