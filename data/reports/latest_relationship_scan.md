# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T23:32:22.771510+00:00`
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

- `news_risk_high->unknown_1h` score `2.3985` n `32` status `ready` deltaP `28.9484` edge `0.0187` maxDD `-0.2787`
- `market_context_high->unknown_1h` score `1.6761` n `138` status `ready` deltaP `5.7147` edge `0.1243` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.6095` n `32` status `ready` deltaP `21.5569` edge `0.0074` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.1138` n `138` status `ready` deltaP `19.8082` edge `-0.0054` maxDD `-0.3736`
- `news_risk_high->commodity_1h` score `1.0991` n `32` status `ready` deltaP `24.8316` edge `-0.0063` maxDD `-0.4666`
- `news_risk_high->equity_1h` score `0.8253` n `32` status `ready` deltaP `18.881` edge `0.0081` maxDD `-0.9204`
- `market_context_high->fx_4h` score `0.1155` n `138` status `ready` deltaP `8.393` edge `0.0091` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0566` n `138` status `ready` deltaP `6.2462` edge `0.0042` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1224` n `138` status `ready` deltaP `2.354` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.356` n `138` status `ready` deltaP `4.2524` edge `0.033` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4063` n `138` status `ready` deltaP `6.6808` edge `-0.0168` maxDD `-1.5942`
- `news_risk_high->metal_1h` score `-0.469` n `32` status `ready` deltaP `-4.1729` edge `-0.01` maxDD `-0.1184`
- `market_context_high->metal_1h` score `-0.5278` n `138` status `ready` deltaP `0.4014` edge `-0.0048` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6062` n `138` status `ready` deltaP `2.2866` edge `0.0106` maxDD `-2.618`
- `news_risk_high->crypto_major_1h` score `-0.6622` n `32` status `ready` deltaP `7.9903` edge `-0.0504` maxDD `-5.0209`
- `news_risk_high->index_1h` score `-0.9075` n `32` status `ready` deltaP `-12.0509` edge `-0.0007` maxDD `-0.1583`
- `market_context_high->fx_24h` score `-0.9528` n `122` status `ready` deltaP `0.6091` edge `0.0087` maxDD `-2.1268`
- `market_context_high->commodity_4h` score `-1.0084` n `138` status `ready` deltaP `-6.398` edge `-0.0016` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.1162` n `138` status `ready` deltaP `-8.3659` edge `-0.0025` maxDD `-1.1193`
- `market_context_high->crypto_alt_4h` score `-1.4502` n `138` status `ready` deltaP `7.0299` edge `-0.0209` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
