# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T08:37:29.323905+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_24h` score `628.9943` n `104` status `ready` deltaP `9.2414` edge `52.3926` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `33.6177` n `104` status `ready` deltaP `-2.5562` edge `2.8724` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.9104` n `62` status `ready` deltaP `34.6184` edge `0.6154` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.6323` n `62` status `ready` deltaP `22.0201` edge `0.5403` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4525` n `62` status `ready` deltaP `24.8264` edge `0.1222` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.2993` n `104` status `ready` deltaP `15.7598` edge `0.2663` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8578` n `62` status `ready` deltaP `32.0024` edge `0.051` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.4395` n `62` status `ready` deltaP `5.5276` edge `0.1764` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.0632` n `62` status `ready` deltaP `7.6299` edge `0.1566` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0055` n `62` status `ready` deltaP `25.3236` edge `0.0133` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9107` n `62` status `ready` deltaP `17.9288` edge `0.0995` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.413` n `62` status `ready` deltaP `20.1809` edge `0.0882` maxDD `-0.993`
- `market_context_high->fx_1h` score `0.99` n `104` status `ready` deltaP `15.1082` edge `0.006` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.9894` n `104` status `ready` deltaP `-1.243` edge `0.2631` maxDD `-7.1222`
- `news_risk_high->crypto_alt_1h` score `0.926` n `62` status `ready` deltaP `2.26` edge `0.114` maxDD `-2.4854`
- `market_context_high->crypto_major_24h` score `0.8993` n `104` status `ready` deltaP `6.9712` edge `0.3662` maxDD `-16.7906`
- `market_context_high->fx_4h` score `0.7667` n `104` status `ready` deltaP `18.3395` edge `0.0173` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.5026` n `62` status `ready` deltaP `26.1537` edge `0.0467` maxDD `-8.196`
- `market_context_high->commodity_1h` score `0.3897` n `104` status `ready` deltaP `8.1414` edge `0.0158` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `0.2667` n `104` status `ready` deltaP `10.4215` edge `0.0536` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
