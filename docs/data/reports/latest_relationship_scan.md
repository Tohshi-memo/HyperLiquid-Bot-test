# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T21:52:27.721112+00:00`
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

- `market_context_high->unknown_1h` score `1.6262` n `143` status `ready` deltaP `6.3053` edge `0.1162` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.815` n `143` status `ready` deltaP `18.7255` edge `-0.013` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1372` n `143` status `ready` deltaP `8.7946` edge `0.0092` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0102` n `143` status `ready` deltaP `7.0925` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1494` n `143` status `ready` deltaP `1.8509` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2876` n `143` status `ready` deltaP `5.5976` edge `0.0328` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.3358` n `143` status `ready` deltaP `7.5921` edge `-0.017` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3818` n `143` status `ready` deltaP `-0.2983` edge `-0.0051` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5723` n `143` status `ready` deltaP `2.8783` edge `0.011` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.9156` n `143` status `ready` deltaP `-4.8524` edge `0.0` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0722` n `143` status `ready` deltaP `-7.5395` edge `-0.0022` maxDD `-1.1328`
- `market_context_high->fx_24h` score `-1.1404` n `127` status `ready` deltaP `0.1463` edge `0.0095` maxDD `-2.2015`
- `market_context_high->crypto_alt_1h` score `-1.5675` n `143` status `ready` deltaP `-2.4883` edge `-0.0349` maxDD `-7.9582`
- `market_context_high->equity_4h` score `-1.6714` n `143` status `ready` deltaP `-0.1439` edge `0.0683` maxDD `-16.1967`
- `market_context_high->crypto_alt_4h` score `-2.1145` n `143` status `ready` deltaP `4.4709` edge `-0.0592` maxDD `-7.0785`
- `market_context_high->commodity_24h` score `-2.1373` n `127` status `ready` deltaP `-5.9069` edge `0.0446` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-2.3706` n `143` status `ready` deltaP `-6.1366` edge `-0.1153` maxDD `-7.8171`
- `market_context_high->metal_24h` score `-5.4286` n `127` status `ready` deltaP `-24.2522` edge `-0.2035` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5979` n `143` status `ready` deltaP `0.7057` edge `-0.3382` maxDD `-5.6395`
- `market_context_high->index_24h` score `-6.8551` n `127` status `ready` deltaP `-7.3559` edge `-0.0415` maxDD `-21.1244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
