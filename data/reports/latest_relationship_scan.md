# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T23:22:18.555334+00:00`
- Price records: `672`
- Market context records: `2506`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.3001` n `122` status `ready` deltaP `19.7547` edge `0.3428` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.6313` n `151` status `ready` deltaP `21.5756` edge `0.51` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8611` n `151` status `ready` deltaP `17.8596` edge `0.3837` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1494` n `122` status `ready` deltaP `12.1983` edge `0.5835` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.9639` n `151` status `ready` deltaP `11.0745` edge `0.1948` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.8179` n `158` status `ready` deltaP `7.7996` edge `0.1349` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.5839` n `158` status `ready` deltaP `7.6158` edge `0.1173` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.2441` n `122` status `ready` deltaP `2.1801` edge `0.7125` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.064` n `122` status `ready` deltaP `3.9019` edge `0.0774` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1497` n `122` status `ready` deltaP `18.1837` edge `0.019` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1665` n `151` status `ready` deltaP `6.4166` edge `0.0275` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.2928` n `158` status `ready` deltaP `1.7149` edge `0.0045` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.3624` n `158` status `ready` deltaP `2.4843` edge `0.0252` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.4398` n `158` status `ready` deltaP `3.3825` edge `0.0089` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5322` n `158` status `ready` deltaP `-0.1421` edge `0.006` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.6855` n `151` status `ready` deltaP `-1.6081` edge `0.0088` maxDD `-0.8774`
- `market_context_high->metal_1h` score `-0.7546` n `158` status `ready` deltaP `0.5647` edge `0.0093` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.8221` n `158` status `ready` deltaP `0.3828` edge `0.0128` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.838` n `122` status `ready` deltaP `3.6174` edge `0.005` maxDD `-2.5908`
- `market_context_high->metal_4h` score `-1.1067` n `151` status `ready` deltaP `1.8929` edge `0.0339` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
