# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T04:37:32.562208+00:00`
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

- `market_context_high->unknown_24h` score `1169.604` n `113` status `ready` deltaP `10.7731` edge `97.4332` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.4129` n `113` status `ready` deltaP `-0.8714` edge `2.5941` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.8064` n `62` status `ready` deltaP `34.9233` edge `0.6047` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.2089` n `62` status `ready` deltaP `21.2579` edge `0.5101` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.5469` n `113` status `ready` deltaP `17.3241` edge `0.2765` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.1259` n `62` status `ready` deltaP `22.0486` edge `0.1135` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7142` n `62` status `ready` deltaP `30.478` edge `0.0492` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1111` n `62` status `ready` deltaP `7.7796` edge `0.1596` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.9048` n `62` status `ready` deltaP `2.9234` edge `0.1492` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9001` n `62` status `ready` deltaP `24.126` edge `0.0125` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6974` n `62` status `ready` deltaP `16.252` edge `0.0929` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.3939` n `113` status `ready` deltaP `1.5176` edge `0.2784` maxDD `-7.1222`
- `news_risk_high->metal_4h` score `1.264` n `62` status `ready` deltaP `18.1992` edge `0.0823` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.2629` n `113` status `ready` deltaP `6.8737` edge `0.3568` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `0.9727` n `62` status `ready` deltaP `2.7091` edge `0.1149` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.8803` n `62` status `ready` deltaP `28.9315` edge `0.0766` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8152` n `113` status `ready` deltaP `18.8107` edge `0.0182` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7206` n `113` status `ready` deltaP `12.5457` edge `0.0048` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.4804` n `113` status `ready` deltaP `11.7648` edge `0.0316` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.2825` n `113` status `ready` deltaP `9.6352` edge `0.0482` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
