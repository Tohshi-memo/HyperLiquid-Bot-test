# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T20:22:25.517411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `market_context_high->unknown_1h` score `1.4676` n `149` status `ready` deltaP `6.1086` edge `0.1043` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8235` n `149` status `ready` deltaP `18.7418` edge `-0.0124` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.082` n `149` status `ready` deltaP `7.7498` edge `0.0091` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0212` n `149` status `ready` deltaP `6.8973` edge `0.0044` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1433` n `149` status `ready` deltaP `1.9672` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3377` n `149` status `ready` deltaP `4.7241` edge `0.0322` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3561` n `149` status `ready` deltaP `0.1809` edge `-0.005` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3679` n `149` status `ready` deltaP `7.2352` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->index_4h` score `-0.5127` n `149` status `ready` deltaP `3.9347` edge `0.0116` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.9134` n `149` status `ready` deltaP `-4.6908` edge `-0.0008` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1305` n `149` status `ready` deltaP `-8.4716` edge `-0.0027` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.1788` n `133` status `ready` deltaP `-0.081` edge `0.0104` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.7005` n `149` status `ready` deltaP `-0.8226` edge `0.0691` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1171` n `133` status `ready` deltaP `-4.3794` edge `0.0361` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.5388` n `149` status `ready` deltaP `-2.6835` edge `-0.0442` maxDD `-7.9582`
- `market_context_high->crypto_alt_4h` score `-2.7341` n `149` status `ready` deltaP `1.9315` edge `-0.0939` maxDD `-7.0785`
- `market_context_high->crypto_major_1h` score `-3.6855` n `149` status `ready` deltaP `-5.8071` edge `-0.1207` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.3058` n `133` status `ready` deltaP `-5.5204` edge `-0.0345` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.3393` n `133` status `ready` deltaP `-22.5943` edge `-0.2031` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.935` n `149` status `ready` deltaP `-1.3034` edge `-0.3529` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
