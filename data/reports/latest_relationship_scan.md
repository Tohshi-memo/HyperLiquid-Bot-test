# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T09:22:33.261850+00:00`
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

- `market_context_high->unknown_24h` score `433.7242` n `101` status `ready` deltaP `8.6702` edge `36.1239` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `34.9378` n `101` status `ready` deltaP `-3.1846` edge `2.9866` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.9876` n `62` status `ready` deltaP `34.9233` edge `0.6198` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.7155` n `62` status `ready` deltaP `22.325` edge `0.5452` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.5122` n `62` status `ready` deltaP `25.3472` edge `0.1237` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.0654` n `101` status `ready` deltaP `15.265` edge `0.2501` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8566` n `62` status `ready` deltaP `32.0024` edge `0.0509` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.5616` n `62` status `ready` deltaP `6.0484` edge `0.1831` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.1063` n `62` status `ready` deltaP `7.9293` edge `0.1582` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0079` n `62` status `ready` deltaP `25.3236` edge `0.0135` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.9239` n `62` status `ready` deltaP `17.9288` edge `0.1006` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.4154` n `62` status `ready` deltaP `20.1809` edge `0.0885` maxDD `-0.993`
- `market_context_high->fx_1h` score `1.0496` n `101` status `ready` deltaP `15.8534` edge `0.006` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.9955` n `62` status `ready` deltaP `2.5594` edge `0.1178` maxDD `-2.4854`
- `market_context_high->crypto_major_24h` score `0.8814` n `101` status `ready` deltaP `6.4923` edge `0.3671` maxDD `-16.7906`
- `market_context_high->crypto_alt_4h` score `0.7203` n `101` status `ready` deltaP `-2.2519` edge `0.2474` maxDD `-7.1222`
- `market_context_high->fx_4h` score `0.6997` n `101` status `ready` deltaP `17.7116` edge `0.0159` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.4722` n `62` status `ready` deltaP `26.1537` edge `0.0428` maxDD `-8.196`
- `market_context_high->commodity_1h` score `0.3611` n `101` status `ready` deltaP `8.0245` edge `0.0142` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `0.3066` n `101` status `ready` deltaP `10.7399` edge `0.0566` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
