# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T08:52:19.452850+00:00`
- Price records: `672`
- Market context records: `2229`
- Flow alert records: `8310`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `26.0546` n `33` status `ready` deltaP `56.7866` edge `1.8515` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.6631` n `33` status `ready` deltaP `47.1433` edge `0.9516` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `12.9623` n `131` status `ready` deltaP `37.4744` edge `0.924` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `12.831` n `33` status `ready` deltaP `38.1155` edge `0.8466` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.7399` n `131` status `ready` deltaP `42.2129` edge `0.7499` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.65` n `33` status `ready` deltaP `37.6894` edge `0.5755` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.6247` n `33` status `ready` deltaP `19.6339` edge `0.9047` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.5378` n `131` status `ready` deltaP `20.9912` edge `0.378` maxDD `-1.8499`
- `news_risk_high->commodity_4h` score `3.9338` n `43` status `ready` deltaP `32.9197` edge `0.352` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.4724` n `131` status `ready` deltaP `23.1486` edge `0.2342` maxDD `-4.5993`
- `market_context_high->index_4h` score `3.3329` n `131` status `ready` deltaP `26.806` edge `0.161` maxDD `-1.6242`
- `market_context_high->crypto_major_1h` score `3.2107` n `141` status `ready` deltaP `17.7857` edge `0.1967` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.964` n `33` status `ready` deltaP `31.0606` edge `0.0584` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.9041` n `141` status `ready` deltaP `15.9574` edge `0.222` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.4197` n `33` status `ready` deltaP `-1.4205` edge `0.2928` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.1634` n `43` status `ready` deltaP `27.4319` edge `0.0158` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `2.1028` n `131` status `ready` deltaP `23.9027` edge `0.4616` maxDD `-30.3243`
- `market_context_high->index_24h` score `1.7391` n `131` status `ready` deltaP `8.8396` edge `0.2011` maxDD `-3.8749`
- `news_risk_high->index_24h` score `1.4618` n `33` status `ready` deltaP `10.5745` edge `0.0932` maxDD `-1.3507`
- `news_risk_high->unknown_1h` score `1.2849` n `43` status `ready` deltaP `20.596` edge `0.0167` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
