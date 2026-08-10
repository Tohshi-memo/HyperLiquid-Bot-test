# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T11:22:34.034245+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->commodity_4h` score `1.0465` n `169` status `ready` deltaP `13.061` edge `0.0716` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7791` n `136` status `ready` deltaP `18.7634` edge `0.0206` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7165` n `169` status `ready` deltaP `9.8705` edge `0.0282` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0538` n `169` status `ready` deltaP `8.3192` edge `0.009` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1335` n `169` status `ready` deltaP `4.1172` edge `0.0006` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6003` n `136` status `ready` deltaP `1.6528` edge `0.0921` maxDD `-5.9181`
- `market_context_high->equity_24h` score `-0.744` n `136` status `ready` deltaP `0.8232` edge `0.2459` maxDD `-21.0709`
- `market_context_high->index_1h` score `-0.7655` n `169` status `ready` deltaP `-2.1277` edge `-0.0019` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7751` n `169` status `ready` deltaP `-4.0596` edge `-0.0087` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-1.1168` n `136` status `ready` deltaP `-1.5611` edge `0.0455` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.1775` n `169` status `ready` deltaP `-1.4571` edge `-0.0019` maxDD `-4.5876`
- `market_context_high->index_4h` score `-1.2013` n `169` status `ready` deltaP `-1.8843` edge `-0.0093` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.5552` n `169` status `ready` deltaP `-8.8288` edge `-0.0384` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9242` n `169` status `ready` deltaP `-6.0002` edge `-0.0303` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.1996` n `169` status `ready` deltaP `-11.4059` edge `-0.1225` maxDD `-7.9331`
- `market_context_high->crypto_major_1h` score `-3.5971` n `169` status `ready` deltaP `-10.091` edge `-0.0591` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-4.0178` n `169` status `ready` deltaP `-12.6073` edge `-0.1553` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.3811` n `136` status `ready` deltaP `-11.9075` edge `-0.1414` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.4786` n `136` status `ready` deltaP `-2.0236` edge `-0.1103` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5893` n `136` status `ready` deltaP `-5.3752` edge `-0.1938` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
