# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T11:22:34.440532+00:00`
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

- `market_context_high->unknown_4h` score `40.6939` n `90` status `ready` deltaP `-2.7981` edge `3.4637` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.2335` n `55` status `ready` deltaP `38.3176` edge `0.701` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `9.5154` n `55` status `ready` deltaP `31.7738` edge `0.659` maxDD `-4.2301`
- `news_risk_high->equity_24h` score `7.2706` n `55` status `ready` deltaP `20.0157` edge `0.4824` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `5.9198` n `90` status `ready` deltaP `15.6649` edge `0.9519` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.3732` n `55` status `ready` deltaP `39.2055` edge `0.1864` maxDD `0.0`
- `market_context_high->equity_24h` score `3.5877` n `90` status `ready` deltaP `18.3995` edge `0.2192` maxDD `-1.0977`
- `news_risk_high->index_4h` score `3.2546` n `55` status `ready` deltaP `35.4324` edge `0.0612` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.9141` n `55` status `ready` deltaP `19.7755` edge `0.1708` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.6488` n `90` status `ready` deltaP `17.4085` edge `0.2011` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.6067` n `55` status `ready` deltaP `9.8939` edge `0.1868` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.3559` n `55` status `ready` deltaP `28.9521` edge `0.0173` maxDD `-0.1194`
- `news_risk_high->crypto_alt_1h` score `1.4753` n `55` status `ready` deltaP `3.669` edge `0.1434` maxDD `-2.2599`
- `market_context_high->metal_24h` score `1.3583` n `90` status `ready` deltaP `22.7461` edge `0.171` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2847` n `55` status `ready` deltaP `19.7228` edge `0.0748` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.804` n `90` status `ready` deltaP `18.7771` edge `0.0165` maxDD `-0.3077`
- `news_risk_high->commodity_24h` score `0.7442` n `55` status `ready` deltaP `26.7326` edge `-0.0065` maxDD `-4.1049`
- `market_context_high->crypto_alt_24h` score `0.5771` n `90` status `ready` deltaP `9.2689` edge `0.606` maxDD `-34.5048`
- `market_context_high->fx_1h` score `0.5729` n `90` status `ready` deltaP `10.2994` edge `0.0033` maxDD `-0.271`
- `news_risk_high->metal_1h` score `0.2668` n `55` status `ready` deltaP `9.08` edge `0.0155` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
