# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T13:52:30.791021+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7070`

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

- `market_context_high->unknown_1h` score `335.1879` n `50` status `ready` deltaP `7.7305` edge `27.8857` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.5792` n `50` status `ready` deltaP `6.8598` edge `23.4192` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.0088` n `114` status `ready` deltaP `32.447` edge `1.3887` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.6003` n `50` status `ready` deltaP `31.1319` edge `0.7341` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2229` n `50` status `ready` deltaP `19.372` edge `0.5431` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8524` n `50` status `ready` deltaP `15.8841` edge `0.4278` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.7344` n `114` status `ready` deltaP `21.0617` edge `0.5695` maxDD `-15.8971`
- `news_risk_high->equity_4h` score `3.8304` n `125` status `ready` deltaP `27.4463` edge `0.1851` maxDD `-1.2436`
- `market_context_high->equity_24h` score `3.8169` n `50` status `ready` deltaP `17.8264` edge `0.5567` maxDD `-11.8957`
- `market_context_high->crypto_alt_24h` score `3.7802` n `50` status `ready` deltaP `8.2014` edge `0.4313` maxDD `-11.6768`
- `news_risk_high->equity_24h` score `3.1025` n `114` status `ready` deltaP `21.7562` edge `0.4876` maxDD `-9.4579`
- `market_context_high->fx_4h` score `3.0532` n `50` status `ready` deltaP `34.5183` edge `0.0378` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0083` n `50` status `ready` deltaP `14.8982` edge `0.1964` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8678` n `50` status `ready` deltaP `13.3054` edge `0.2166` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.3736` n `114` status `ready` deltaP `23.2365` edge `0.0907` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2487` n `114` status `ready` deltaP `26.3249` edge `0.2402` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4831` n `50` status `ready` deltaP `20.7904` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.816` n `127` status `ready` deltaP `8.2736` edge `0.0665` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7205` n `50` status `ready` deltaP `12.5347` edge `0.0659` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5704` n `50` status `ready` deltaP `14.7778` edge `0.0764` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
