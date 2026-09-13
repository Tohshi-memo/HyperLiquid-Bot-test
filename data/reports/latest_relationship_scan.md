# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T19:37:26.537779+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12738`

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

- `market_context_high->unknown_24h` score `17708.8224` n `56` status `ready` deltaP `10.2093` edge `1475.6873` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7812.1971` n `37` status `ready` deltaP `11.0298` edge `650.9494` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7812.1971` n `37` status `ready` deltaP `11.0298` edge `650.9494` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `426.9591` n `82` status `ready` deltaP `-5.1008` edge `35.6561` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6763` n `82` status `ready` deltaP `36.2027` edge `1.3638` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3508` n `82` status `ready` deltaP `38.0236` edge `1.4228` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.5231` n `82` status `ready` deltaP `27.9605` edge `0.7852` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.2086` n `82` status `ready` deltaP `51.7325` edge `0.2735` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7693` n `82` status `ready` deltaP `26.4845` edge `0.2663` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.7114` n `37` status `ready` deltaP `39.8276` edge `0.1271` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7114` n `37` status `ready` deltaP `39.8276` edge `0.1271` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.5326` n `56` status `ready` deltaP `39.8276` edge `0.1122` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `2.5784` n `37` status `ready` deltaP `4.6273` edge `0.4333` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.5784` n `37` status `ready` deltaP `4.6273` edge `0.4333` maxDD `-7.0204`
- `market_context_high->crypto_alt_24h` score `2.5196` n `56` status `ready` deltaP `5.0616` edge `0.4554` maxDD `-9.6226`
- `risk_on_high->fx_24h` score `1.4656` n `37` status `ready` deltaP `36.8779` edge `0.0111` maxDD `-1.5242`
- `risk_on_and_context->fx_24h` score `1.4656` n `37` status `ready` deltaP `36.8779` edge `0.0111` maxDD `-1.5242`
- `risk_on_high->commodity_4h` score `0.7814` n `59` status `ready` deltaP `13.8332` edge `0.0098` maxDD `-0.286`
- `risk_on_and_context->commodity_4h` score `0.7814` n `59` status `ready` deltaP `13.8332` edge `0.0098` maxDD `-0.286`
- `market_context_high->commodity_4h` score `0.6475` n `131` status `ready` deltaP `13.2122` edge `0.0121` maxDD `-0.3645`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
