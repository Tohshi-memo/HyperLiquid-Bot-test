# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T10:37:18.368076+00:00`
- Price records: `672`
- Market context records: `1109`
- Flow alert records: `5098`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8704`

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

- `market_context_high->crypto_major_24h` score `17.7241` n `150` status `ready` deltaP `38.4236` edge `1.2672` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `7.2836` n `150` status `ready` deltaP `14.7847` edge `0.6318` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.3006` n `150` status `ready` deltaP `15.8264` edge `0.4692` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.4326` n `150` status `ready` deltaP `-2.4097` edge `0.6355` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.0193` n `150` status `ready` deltaP `15.1319` edge `0.3482` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.719` n `168` status `ready` deltaP `10.032` edge `0.1427` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.9142` n `168` status `ready` deltaP `8.4422` edge `0.0882` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4702` n `168` status `ready` deltaP `7.4957` edge `0.0209` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2824` n `168` status `ready` deltaP `2.7302` edge `0.0431` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1101` n `168` status `ready` deltaP `7.4316` edge `0.0362` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.11` n `168` status `ready` deltaP `8.0161` edge `0.0013` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0504` n `168` status `ready` deltaP `8.4567` edge `0.1422` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1956` n `168` status `ready` deltaP `6.9504` edge `-0.0016` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2034` n `168` status `ready` deltaP `3.2435` edge `0.0457` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.6875` n `168` status `ready` deltaP `1.5461` edge `0.0012` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7162` n `168` status `ready` deltaP `-1.4756` edge `-0.0012` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.02` n `168` status `ready` deltaP `5.5387` edge `0.1288` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.3657` n `168` status `ready` deltaP `6.7` edge `-0.0464` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1282` n `168` status `ready` deltaP `-10.6635` edge `-0.0132` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.324` n `150` status `ready` deltaP `1.3472` edge `-0.0275` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
