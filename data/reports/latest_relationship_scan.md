# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T08:07:32.948796+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `753.4885` n `106` status `ready` deltaP `9.6043` edge `62.7647` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `32.8756` n `106` status `ready` deltaP `-2.1571` edge `2.8079` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.8816` n `62` status `ready` deltaP `34.6184` edge `0.613` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5951` n `62` status `ready` deltaP `22.0201` edge `0.5372` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.5296` n `106` status `ready` deltaP `16.2678` edge `0.2821` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.4079` n `62` status `ready` deltaP `24.4792` edge `0.1208` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8554` n `62` status `ready` deltaP `32.0024` edge `0.0508` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.3458` n `62` status `ready` deltaP `5.1803` edge `0.1709` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.0176` n `62` status `ready` deltaP `7.3305` edge `0.1548` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9792` n `62` status `ready` deltaP `25.0242` edge `0.0131` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.872` n `62` status `ready` deltaP `17.624` edge `0.0983` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.402` n `62` status `ready` deltaP `20.0285` edge `0.0878` maxDD `-0.993`
- `market_context_high->crypto_alt_4h` score `1.3058` n `106` status `ready` deltaP `-0.4084` edge `0.2839` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `1.0008` n `106` status `ready` deltaP `7.2589` edge `0.3773` maxDD `-16.7906`
- `market_context_high->fx_1h` score `0.8846` n `106` status `ready` deltaP `13.9109` edge `0.0052` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.8696` n `62` status `ready` deltaP `1.9606` edge `0.1113` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8047` n `106` status `ready` deltaP `18.7241` edge `0.0179` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.5472` n `62` status `ready` deltaP `26.5009` edge `0.0501` maxDD `-8.196`
- `market_context_high->crypto_major_1h` score `0.33` n `106` status `ready` deltaP `10.7389` edge `0.0596` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `0.2846` n `106` status `ready` deltaP `7.2026` edge `0.0133` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
