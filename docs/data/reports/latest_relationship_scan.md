# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T15:22:33.997259+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8042`

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

- `market_context_high->crypto_major_24h` score `10.8487` n `80` status `ready` deltaP `29.7569` edge `0.7193` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.5468` n `65` status `ready` deltaP `33.3138` edge `0.5938` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.9276` n `65` status `ready` deltaP `20.3963` edge `0.4924` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.727` n `80` status `ready` deltaP `25.9375` edge `0.3663` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.4494` n `65` status `ready` deltaP `24.6528` edge `0.1231` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1325` n `65` status `ready` deltaP `9.8184` edge `0.2056` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8771` n `65` status `ready` deltaP `31.9137` edge `0.0532` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4845` n `65` status `ready` deltaP `9.7167` edge `0.1778` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4256` n `65` status `ready` deltaP `20.272` edge `0.128` maxDD `-2.881`
- `market_context_high->crypto_major_4h` score `2.4213` n `119` status `ready` deltaP `12.4347` edge `0.2153` maxDD `-4.047`
- `news_risk_high->index_1h` score `1.9955` n `65` status `ready` deltaP `24.8687` edge `0.0155` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8596` n `65` status `ready` deltaP `17.7064` edge `0.0785` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5076` n `119` status `ready` deltaP `26.2951` edge `0.026` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1541` n `65` status `ready` deltaP `3.6711` edge `0.1236` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9802` n `119` status `ready` deltaP `15.5361` edge `0.0065` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.8577` n `119` status `ready` deltaP `13.5569` edge `0.0511` maxDD `-1.6002`
- `market_context_high->metal_24h` score `0.8071` n `80` status `ready` deltaP `25.4514` edge `0.0729` maxDD `-5.7943`
- `market_context_high->equity_24h` score `0.7851` n `80` status `ready` deltaP `13.4722` edge `-0.0183` maxDD `-0.1536`
- `market_context_high->commodity_1h` score `0.4469` n `119` status `ready` deltaP `10.4941` edge `0.0136` maxDD `-1.0387`
- `news_risk_high->commodity_24h` score `0.3935` n `65` status `ready` deltaP `24.9119` edge `0.0875` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
