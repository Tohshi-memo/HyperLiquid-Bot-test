# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T09:22:57.692465+00:00`
- Price records: `672`
- Market context records: `6484`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.6391` n `32` status `ready` deltaP `34.2014` edge `0.84` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.6131` n `159` status `ready` deltaP `16.4275` edge `0.7716` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4529` n `32` status `ready` deltaP `53.6458` edge `0.1801` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3677` n `32` status `ready` deltaP `17.0139` edge `0.5245` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9666` n `38` status `ready` deltaP `42.2176` edge `0.0537` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.0423` n `32` status `ready` deltaP `28.6458` edge `0.0831` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.5877` n `180` status `ready` deltaP `-4.2981` edge `0.3344` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.843` n `38` status `ready` deltaP `23.0618` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.566` n `38` status `ready` deltaP `4.9007` edge `0.0936` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4817` n `171` status `ready` deltaP `11.8912` edge `0.0285` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.3173` n `159` status `ready` deltaP `6.535` edge `0.1697` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.2589` n `171` status `ready` deltaP `8.4822` edge `0.1204` maxDD `-6.7632`
- `market_context_high->metal_4h` score `0.1924` n `171` status `ready` deltaP `12.1131` edge `0.0441` maxDD `-2.7056`
- `market_context_high->unknown_4h` score `0.1882` n `171` status `ready` deltaP `-15.802` edge `0.3616` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0664` n `38` status `ready` deltaP `1.434` edge `0.0499` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.4505` n `171` status `ready` deltaP `8.4795` edge `0.0556` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.4556` n `32` status `ready` deltaP `4.6875` edge `-0.0025` maxDD `-2.3058`
- `market_context_high->crypto_alt_1h` score `-0.4955` n `180` status `ready` deltaP `7.1357` edge `0.0202` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5466` n `180` status `ready` deltaP `7.006` edge `0.0098` maxDD `-6.7936`
- `market_context_high->metal_1h` score `-0.5538` n `180` status `ready` deltaP `0.835` edge `0.0012` maxDD `-1.8877`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
