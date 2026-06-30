# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T09:22:29.086306+00:00`
- Price records: `672`
- Market context records: `5234`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5602`

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

- `market_context_high->unknown_24h` score `22.7952` n `125` status `ready` deltaP `32.2167` edge `1.7038` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.2801` n `125` status `ready` deltaP `33.2167` edge `1.2514` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `7.2332` n `125` status `ready` deltaP `22.8847` edge `0.7889` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.0651` n `155` status `ready` deltaP `13.5415` edge `0.4084` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9562` n `155` status `ready` deltaP `14.3745` edge `0.4631` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.1792` n `155` status `ready` deltaP `16.9827` edge `0.1706` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8094` n `155` status `ready` deltaP `8.0896` edge `0.161` maxDD `-2.7986`
- `market_context_high->equity_24h` score `0.9567` n `125` status `ready` deltaP `17.4764` edge `0.5261` maxDD `-40.0306`
- `market_context_high->fx_24h` score `0.5688` n `125` status `ready` deltaP `13.2653` edge `0.0485` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4964` n `155` status `ready` deltaP `4.9527` edge `0.1045` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.46` n `155` status `ready` deltaP `7.0021` edge `0.1162` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.0831` n `155` status `ready` deltaP `6.1782` edge `0.1296` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.1384` n `155` status `ready` deltaP `5.6693` edge `0.0472` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1659` n `155` status `ready` deltaP `3.9617` edge `0.0115` maxDD `-2.0682`
- `market_context_high->index_24h` score `-0.1782` n `125` status `ready` deltaP `16.8222` edge `0.0285` maxDD `-7.413`
- `market_context_high->index_1h` score `-0.2038` n `155` status `ready` deltaP `3.6875` edge `0.0088` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3188` n `155` status `ready` deltaP `0.7611` edge `-0.0007` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.667` n `155` status `ready` deltaP `-0.3226` edge `-0.0025` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7299` n `155` status `ready` deltaP `1.0523` edge `0.0028` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8971` n `155` status `ready` deltaP `3.1619` edge `0.0159` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
