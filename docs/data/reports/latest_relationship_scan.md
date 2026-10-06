# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T07:07:27.009872+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `news_risk_high->crypto_major_4h` score `9.6025` n `63` status `ready` deltaP `33.6794` edge `0.596` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.8646` n `63` status `ready` deltaP `20.5236` edge `0.4863` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `4.0322` n `102` status `ready` deltaP `12.1791` edge `0.4033` maxDD `-7.878`
- `news_risk_high->equity_24h` score `3.6392` n `63` status `ready` deltaP `10.8329` edge `0.241` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2676` n `63` status `ready` deltaP `22.6804` edge `0.1211` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.6386` n `117` status `ready` deltaP `13.4108` edge `0.2269` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5836` n `63` status `ready` deltaP `28.9804` edge `0.0483` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.2425` n `63` status `ready` deltaP `8.6423` edge `0.1648` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8366` n `63` status `ready` deltaP `23.1371` edge `0.0138` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8119` n `63` status `ready` deltaP `17.1434` edge `0.0965` maxDD `-2.7837`
- `market_context_high->fx_4h` score `1.2963` n `117` status `ready` deltaP `23.9238` edge `0.0242` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2029` n `117` status `ready` deltaP `16.2967` edge `0.0616` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1959` n `63` status `ready` deltaP `17.3394` edge `0.0793` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `0.9681` n `63` status `ready` deltaP `3.101` edge `0.1119` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9192` n `117` status `ready` deltaP `14.7884` edge `0.0064` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7909` n `117` status `ready` deltaP `12.5045` edge `0.0222` maxDD `-0.5059`
- `news_risk_high->commodity_24h` score `0.4586` n `63` status `ready` deltaP `25.8059` edge `0.0596` maxDD `-9.1608`
- `market_context_high->crypto_alt_4h` score `0.2835` n `117` status `ready` deltaP `-0.7218` edge `0.2008` maxDD `-7.1222`
- `market_context_high->metal_24h` score `0.2159` n `102` status `ready` deltaP `16.1815` edge `0.0573` maxDD `-5.6663`
- `news_risk_high->metal_1h` score `-0.019` n `63` status `ready` deltaP `4.8974` edge `0.0076` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
