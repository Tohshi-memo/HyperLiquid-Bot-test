# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T09:07:27.613159+00:00`
- Price records: `672`
- Market context records: `2547`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->unknown_24h` score `5.5291` n `120` status `ready` deltaP `19.6181` edge `0.3628` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.5034` n `152` status `ready` deltaP `24.1977` edge `0.5652` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `4.608` n `120` status `ready` deltaP `11.1111` edge `0.5715` maxDD `-15.259`
- `market_context_high->crypto_major_4h` score `3.8537` n `152` status `ready` deltaP `17.362` edge `0.3864` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.9452` n `152` status `ready` deltaP `11.0959` edge `0.1931` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.2172` n `152` status `ready` deltaP `10.1954` edge `0.1522` maxDD `-6.1656`
- `market_context_high->equity_24h` score `0.7965` n `120` status `ready` deltaP `17.5` edge `0.0122` maxDD `-2.6657`
- `market_context_high->crypto_major_1h` score `0.745` n `152` status `ready` deltaP `8.5802` edge `0.1243` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6554` n `120` status `ready` deltaP `6.3889` edge `0.1101` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `-0.084` n `152` status `ready` deltaP `3.6165` edge `0.0379` maxDD `-2.8543`
- `market_context_high->index_4h` score `-0.0869` n `152` status `ready` deltaP `6.3463` edge `0.0346` maxDD `-2.3986`
- `market_context_high->crypto_alt_24h` score `-0.0984` n `120` status `ready` deltaP `-1.7361` edge `0.6594` maxDD `-40.8358`
- `market_context_high->index_1h` score `-0.2484` n `152` status `ready` deltaP `2.8049` edge `0.01` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.3229` n `152` status `ready` deltaP `1.1661` edge `0.0043` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.3862` n `152` status `ready` deltaP `1.8555` edge `0.0129` maxDD `-2.9823`
- `market_context_high->commodity_1h` score `-0.3895` n `152` status `ready` deltaP `3.6756` edge `0.0134` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.7686` n `152` status `ready` deltaP `4.1239` edge `0.0472` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.7769` n `152` status `ready` deltaP `0.0473` edge `0.0188` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8489` n `152` status `ready` deltaP `0.4092` edge `0.0125` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.9088` n `120` status `ready` deltaP `0.7986` edge `0.0025` maxDD `-2.2801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
