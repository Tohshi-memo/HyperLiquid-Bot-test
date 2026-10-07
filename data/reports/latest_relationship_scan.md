# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T22:37:34.385456+00:00`
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

- `market_context_high->unknown_4h` score `38.3352` n `90` status `ready` deltaP `-5.2371` edge `3.2834` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9633` n `62` status `ready` deltaP `38.7343` edge `0.6757` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0335` n `62` status `ready` deltaP `22.325` edge `0.5717` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.1367` n `62` status `ready` deltaP `12.4065` edge `0.3553` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.4235` n `62` status `ready` deltaP `31.8339` edge `0.1564` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.7307` n `90` status `ready` deltaP `10.0461` edge `0.7087` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8378` n `62` status `ready` deltaP `31.3926` edge `0.0534` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5031` n `62` status `ready` deltaP `10.4742` edge `0.1743` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4585` n `90` status `ready` deltaP `16.7988` edge `0.1893` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0456` n `62` status `ready` deltaP `17.3191` edge `0.1148` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9109` n `62` status `ready` deltaP `24.126` edge `0.0134` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.5125` n `62` status `ready` deltaP `21.5529` edge `0.0918` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.1214` n `62` status `ready` deltaP `3.1582` edge `0.1243` maxDD `-2.4854`
- `news_risk_high->unknown_4h` score `1.1148` n `62` status `ready` deltaP `-8.2121` edge `0.2722` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.0512` n `90` status `ready` deltaP `20.0807` edge `0.1494` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.9224` n `90` status `ready` deltaP `20.3015` edge `0.0162` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6795` n `90` status `ready` deltaP `11.6467` edge `0.0032` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.6321` n `90` status `ready` deltaP `9.9692` edge `0.0291` maxDD `-1.0977`
- `market_context_high->crypto_major_1h` score `0.1619` n `90` status `ready` deltaP `10.4025` edge `0.0403` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1401` n `62` status `ready` deltaP `6.751` edge `0.0085` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
