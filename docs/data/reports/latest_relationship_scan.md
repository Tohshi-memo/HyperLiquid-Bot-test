# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T21:22:24.973648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.7937` n `60` status `ready` deltaP `31.8082` edge `432.2295` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.6583` n `53` status `ready` deltaP `57.4441` edge `1.1283` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8511` n `68` status `ready` deltaP `16.9835` edge `0.3674` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7704` n `53` status `ready` deltaP `27.4844` edge `0.2296` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.7148` n `68` status `ready` deltaP `16.3737` edge `0.0718` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.7561` n `53` status `ready` deltaP `9.5001` edge `0.1293` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6864` n `68` status `ready` deltaP `9.4928` edge `0.0762` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2391` n `53` status `ready` deltaP `14.1682` edge `0.0158` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1305` n `68` status `ready` deltaP `5.165` edge `0.0299` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1232` n `68` status `ready` deltaP `6.4812` edge `0.0408` maxDD `-3.1233`
- `market_context_high->fx_1h` score `-0.0029` n `53` status `ready` deltaP `7.3523` edge `0.001` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `-0.0101` n `68` status `ready` deltaP `10.9218` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.0512` n `68` status `ready` deltaP `2.6154` edge `0.0083` maxDD `-0.5845`
- `market_context_high->fx_24h` score `-0.0657` n `53` status `ready` deltaP `7.0599` edge `0.0425` maxDD `-2.506`
- `market_context_high->commodity_1h` score `-0.0792` n `53` status `ready` deltaP `4.1775` edge `0.0161` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.1035` n `68` status `ready` deltaP `2.2191` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1419` n `68` status `ready` deltaP `2.316` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1952` n `68` status `ready` deltaP `2.0694` edge `0.0332` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.3094` n `53` status `ready` deltaP `2.81` edge `0.0291` maxDD `-3.0005`
- `market_context_high->crypto_alt_1h` score `-0.5879` n `53` status `ready` deltaP `-4.1182` edge `0.0148` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
