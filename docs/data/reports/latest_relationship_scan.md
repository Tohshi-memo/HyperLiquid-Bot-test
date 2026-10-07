# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T23:07:25.979408+00:00`
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

- `market_context_high->unknown_4h` score `38.3642` n `90` status `ready` deltaP `-5.0846` edge `3.2848` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9645` n `62` status `ready` deltaP `38.7343` edge `0.6758` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0215` n `62` status `ready` deltaP `22.325` edge `0.5707` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.2579` n `62` status `ready` deltaP `12.7526` edge `0.3631` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.4668` n `62` status `ready` deltaP `32.1799` edge `0.1577` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.8219` n `90` status `ready` deltaP `10.0461` edge `0.7204` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8256` n `62` status `ready` deltaP `31.2402` edge `0.0534` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4851` n `62` status `ready` deltaP `10.3245` edge `0.1738` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4597` n `90` status `ready` deltaP `16.7988` edge `0.1894` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0262` n `62` status `ready` deltaP `17.1666` edge `0.1142` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.8846` n `62` status `ready` deltaP `23.8266` edge `0.0132` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.5014` n `62` status `ready` deltaP `21.4004` edge `0.0914` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.1438` n `62` status `ready` deltaP `-8.0596` edge `0.2736` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.0692` n `90` status `ready` deltaP `20.0807` edge `0.1517` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0687` n `62` status `ready` deltaP `2.8588` edge `0.1219` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.926` n `90` status `ready` deltaP `20.3015` edge `0.0165` maxDD `-0.3077`
- `market_context_high->equity_24h` score `0.7534` n `90` status `ready` deltaP `10.3153` edge `0.0369` maxDD `-1.0977`
- `market_context_high->fx_1h` score `0.6915` n `90` status `ready` deltaP `11.7964` edge `0.0032` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1503` n `90` status `ready` deltaP `10.2528` edge `0.0398` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1401` n `62` status `ready` deltaP `6.751` edge `0.0085` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
