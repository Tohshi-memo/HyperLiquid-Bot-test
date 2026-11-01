# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T04:07:27.301147+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6373`

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

- `market_context_high->unknown_24h` score `5508.8199` n `66` status `ready` deltaP `-3.1881` edge `459.1145` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `261.3797` n `66` status `ready` deltaP `1.5614` edge `21.7828` maxDD `-0.2588`
- `news_risk_high->unknown_1h` score `81.5524` n `108` status `ready` deltaP `-5.0454` edge `6.8583` maxDD `-0.9571`
- `market_context_high->equity_24h` score `16.5713` n `66` status `ready` deltaP `32.1654` edge `1.2789` maxDD `-5.325`
- `news_risk_high->crypto_alt_24h` score `13.8059` n `95` status `ready` deltaP `32.3118` edge `1.0707` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.2712` n `66` status `ready` deltaP `54.0088` edge `0.1762` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.3535` n `108` status `ready` deltaP `20.2744` edge `0.4496` maxDD `-7.4246`
- `market_context_high->unknown_1h` score `4.4119` n `66` status `ready` deltaP `2.867` edge `0.3596` maxDD `-0.2178`
- `market_context_high->commodity_4h` score `2.8361` n `66` status `ready` deltaP `27.8917` edge `0.0838` maxDD `-0.3387`
- `market_context_high->commodity_24h` score `1.9882` n `66` status `ready` deltaP `32.8914` edge `0.1634` maxDD `-6.5553`
- `market_context_high->metal_4h` score `1.1629` n `66` status `ready` deltaP `14.2646` edge `0.0443` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.0208` n `66` status `ready` deltaP `-1.8201` edge `0.229` maxDD `-3.2132`
- `news_risk_high->crypto_alt_1h` score `0.8588` n `108` status `ready` deltaP `9.0264` edge `0.1068` maxDD `-3.9659`
- `market_context_high->fx_1h` score `0.628` n `66` status `ready` deltaP `14.8703` edge `-0.0002` maxDD `-0.1407`
- `market_context_high->metal_1h` score `0.5839` n `66` status `ready` deltaP `8.4558` edge `0.0213` maxDD `-0.3209`
- `market_context_high->crypto_major_4h` score `0.4617` n `66` status `ready` deltaP `17.7153` edge `0.1118` maxDD `-9.6571`
- `market_context_high->crypto_major_24h` score `0.1928` n `66` status `ready` deltaP `3.2039` edge `0.1662` maxDD `-10.0529`
- `market_context_high->fx_4h` score `0.1923` n `66` status `ready` deltaP `8.0146` edge `0.0017` maxDD `-0.1285`
- `market_context_high->crypto_alt_24h` score `0.1513` n `66` status `ready` deltaP `-10.5272` edge `0.294` maxDD `-13.2304`
- `market_context_high->equity_1h` score `0.1391` n `66` status `ready` deltaP `-2.4315` edge `0.1216` maxDD `-2.3383`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
