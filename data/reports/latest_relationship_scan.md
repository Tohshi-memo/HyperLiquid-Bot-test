# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T07:07:36.109169+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6958`

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

- `market_context_high->unknown_1h` score `87.0378` n `115` status `ready` deltaP `0.8722` edge `7.2888` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `60.7292` n `103` status `ready` deltaP `2.7188` edge `5.0738` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.4494` n `72` status `ready` deltaP `29.3402` edge `0.6888` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3203` n `65` status `ready` deltaP `32.5516` edge `0.58` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1378` n `72` status `ready` deltaP `24.132` edge `0.4959` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.866` n `65` status `ready` deltaP `20.0915` edge `0.4893` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.4461` n `65` status `ready` deltaP `12.9434` edge `0.2109` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.3457` n `65` status `ready` deltaP `23.6111` edge `0.1214` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.9125` n `103` status `ready` deltaP `13.0594` edge `0.2354` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8731` n `65` status `ready` deltaP `31.6088` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.512` n `65` status `ready` deltaP `20.272` edge `0.1352` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4509` n `65` status `ready` deltaP `9.8664` edge `0.174` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0602` n `65` status `ready` deltaP `25.4675` edge `0.0169` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9294` n `65` status `ready` deltaP `17.8588` edge `0.0833` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.2091` n `103` status `ready` deltaP `22.6542` edge `0.0254` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1373` n `65` status `ready` deltaP `3.5214` edge `0.1232` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `0.8801` n `115` status `ready` deltaP `10.6691` edge `0.0911` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.555` n `65` status `ready` deltaP `24.9119` edge `0.1082` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.4783` n `115` status `ready` deltaP `12.7519` edge `0.0047` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.3573` n `72` status `ready` deltaP `5.2083` edge `0.0153` maxDD `-0.6196`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
