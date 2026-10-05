# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T02:52:36.663436+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5368`

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

- `market_context_high->unknown_1h` score `120.1121` n `98` status `ready` deltaP `-1.274` edge `10.0593` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `71.7208` n `95` status `ready` deltaP `2.4743` edge `5.9914` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `11.0429` n `55` status `ready` deltaP `30.3094` edge `0.7318` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `9.9211` n `55` status `ready` deltaP `25.2935` edge `0.7201` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.3755` n `65` status `ready` deltaP `32.5516` edge `0.5846` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.2276` n `65` status `ready` deltaP `20.3963` edge `0.5174` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.479` n `65` status `ready` deltaP `15.8948` edge `0.2773` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.2682` n `95` status `ready` deltaP `18.1386` edge `0.3051` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.4045` n `65` status `ready` deltaP `23.6111` edge `0.1263` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8889` n `65` status `ready` deltaP `31.7613` edge `0.0552` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.819` n `65` status `ready` deltaP `21.0342` edge `0.1557` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.5216` n `65` status `ready` deltaP `10.1658` edge `0.1779` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.2177` n `98` status `ready` deltaP `15.4406` edge `0.1269` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.071` n `65` status `ready` deltaP `25.6172` edge `0.0168` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `2.0493` n `65` status `ready` deltaP `18.7735` edge `0.0872` maxDD `-0.993`
- `market_context_high->fx_24h` score `1.7207` n `55` status `ready` deltaP `21.2122` edge `0.0941` maxDD `-1.703`
- `market_context_high->equity_24h` score `1.5772` n `55` status `ready` deltaP `3.8668` edge `0.1259` maxDD `-0.6196`
- `market_context_high->fx_4h` score `1.4709` n `95` status `ready` deltaP `25.4766` edge `0.0284` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2824` n `65` status `ready` deltaP `3.9705` edge `0.1323` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.1074` n `95` status `ready` deltaP `3.5542` edge `0.2475` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
