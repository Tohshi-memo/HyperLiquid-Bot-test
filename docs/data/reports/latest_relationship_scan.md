# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T09:07:28.116137+00:00`
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

- `market_context_high->unknown_24h` score `500.0565` n `102` status `ready` deltaP `8.8644` edge `41.6503` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `34.5337` n `102` status `ready` deltaP `-2.971` edge `2.9515` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.955` n `62` status `ready` deltaP `34.7709` edge `0.6181` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.6817` n `62` status `ready` deltaP `22.1725` edge `0.5434` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4935` n `62` status `ready` deltaP `25.1736` edge `0.1233` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.1253` n `102` status `ready` deltaP `15.3844` edge `0.2543` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8566` n `62` status `ready` deltaP `32.0024` edge `0.0509` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.5249` n `62` status `ready` deltaP `5.8748` edge `0.1812` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.1039` n `62` status `ready` deltaP `7.9293` edge `0.158` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0067` n `62` status `ready` deltaP `25.3236` edge `0.0134` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9179` n `62` status `ready` deltaP `17.9288` edge `0.1001` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.4146` n `62` status `ready` deltaP `20.1809` edge `0.0884` maxDD `-0.993`
- `market_context_high->fx_1h` score `1.08` n `102` status `ready` deltaP `16.2029` edge `0.0062` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.9871` n `62` status `ready` deltaP `2.5594` edge `0.1171` maxDD `-2.4854`
- `market_context_high->crypto_major_24h` score `0.8487` n `102` status `ready` deltaP `6.6585` edge `0.3618` maxDD `-16.7906`
- `market_context_high->crypto_alt_4h` score `0.7834` n `102` status `ready` deltaP `-1.9578` edge `0.2507` maxDD `-7.1222`
- `market_context_high->fx_4h` score `0.7242` n `102` status `ready` deltaP `17.928` edge `0.0165` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.4816` n `62` status `ready` deltaP `26.1537` edge `0.044` maxDD `-8.196`
- `market_context_high->commodity_1h` score `0.4053` n `102` status `ready` deltaP `8.4419` edge `0.0151` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `0.2427` n `102` status `ready` deltaP `10.0799` edge `0.0528` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
