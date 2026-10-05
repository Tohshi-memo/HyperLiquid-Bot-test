# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T10:22:28.646347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8312`

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

- `market_context_high->unknown_1h` score `72.7014` n `124` status `ready` deltaP `-0.6422` edge `6.1042` maxDD `-0.9839`
- `market_context_high->crypto_major_24h` score `10.7684` n `81` status `ready` deltaP `29.8032` edge `0.7123` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3839` n `65` status `ready` deltaP `32.5516` edge `0.5853` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.687` n `81` status `ready` deltaP `25.3666` edge `0.4501` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8788` n `65` status `ready` deltaP `19.7866` edge `0.4924` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.3632` n `65` status `ready` deltaP `23.7847` edge `0.1217` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.3321` n `112` status `ready` deltaP `15.2439` edge `0.2558` maxDD `-4.047`
- `news_risk_high->equity_24h` score `3.1354` n `65` status `ready` deltaP `10.8601` edge `0.1989` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.957` n `65` status `ready` deltaP `32.5235` edge `0.0558` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5664` n `65` status `ready` deltaP `20.5769` edge `0.1377` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4641` n `65` status `ready` deltaP `9.8664` edge `0.1751` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0602` n `65` status `ready` deltaP `25.4675` edge `0.0169` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8666` n `65` status `ready` deltaP `17.554` edge `0.0801` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5593` n `112` status `ready` deltaP `26.851` edge `0.0266` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1049` n `65` status `ready` deltaP `3.3717` edge `0.1215` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.8097` n `124` status `ready` deltaP `13.5696` edge `0.0054` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.5753` n `124` status `ready` deltaP `9.0352` edge `0.0766` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.5222` n `65` status `ready` deltaP `24.9119` edge `0.104` maxDD `-10.9169`
- `market_context_high->equity_24h` score `0.4853` n `81` status `ready` deltaP `8.3719` edge `-0.0015` maxDD `-0.4427`
- `market_context_high->crypto_alt_4h` score `0.3628` n `112` status `ready` deltaP `2.2866` edge `0.1939` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
