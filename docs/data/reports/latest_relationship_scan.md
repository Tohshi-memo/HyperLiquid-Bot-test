# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T23:07:27.928763+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6574`

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

- `market_context_high->unknown_1h` score `338.5116` n `50` status `ready` deltaP `9.2275` edge `28.1527` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.0282` n `50` status `ready` deltaP `7.622` edge `23.8682` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.0298` n `90` status `ready` deltaP `36.8403` edge `1.4445` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.6474` n `50` status `ready` deltaP `34.9514` edge `0.7959` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3259` n `50` status `ready` deltaP `19.2195` edge `0.5527` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.3003` n `50` status `ready` deltaP `13.0625` edge `0.6089` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0898` n `50` status `ready` deltaP `16.6463` edge `0.4425` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.1219` n `90` status `ready` deltaP `17.3958` edge `0.5429` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.7202` n `50` status `ready` deltaP `19.0417` edge `0.5362` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `3.0575` n `50` status `ready` deltaP `14.8982` edge `0.2005` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0273` n `50` status `ready` deltaP `14.2036` edge `0.2239` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `3.0259` n `103` status `ready` deltaP `26.0493` edge `0.1481` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.0028` n `50` status `ready` deltaP `33.6037` edge `0.0397` maxDD `-0.0791`
- `news_risk_high->equity_24h` score `2.4161` n `90` status `ready` deltaP `16.5973` edge `0.434` maxDD `-9.4579`
- `news_risk_high->metal_24h` score `1.8379` n `90` status `ready` deltaP `20.6597` edge `0.2253` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.7872` n `90` status `ready` deltaP `20.3473` edge `0.0611` maxDD `-0.4916`
- `news_risk_high->commodity_24h` score `1.536` n `90` status `ready` deltaP `25.1736` edge `0.1415` maxDD `-3.9922`
- `market_context_high->fx_1h` score `1.5154` n `50` status `ready` deltaP `21.0898` edge `0.0121` maxDD `-0.113`
- `news_risk_high->crypto_alt_4h` score `1.2485` n `103` status `ready` deltaP `6.8405` edge `0.2213` maxDD `-8.6957`
- `market_context_high->index_24h` score `0.9136` n `50` status `ready` deltaP `14.7917` edge `0.0756` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
